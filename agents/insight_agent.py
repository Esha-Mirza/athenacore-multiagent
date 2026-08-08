from .base import call_llm, log_agent_response, get_topic_log

def run(topic: str) -> str:
    log = get_topic_log(topic)
    if not log:
        return "No content to analyze yet."
    
    memory = "\n".join([f"{m['agent']}: {m['content']}" for m in log])
    prompt = f"Extract key insights and takeaways:\n{memory}"
    
    insight = call_llm(prompt)
    log_agent_response(topic, "Insight Agent", insight)
    return insight