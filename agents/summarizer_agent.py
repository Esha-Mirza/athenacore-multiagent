from .base import call_llm, log_agent_response, get_topic_log

def run(topic: str) -> str:
    log = get_topic_log(topic)
    if not log:
        return "No content to summarize yet."
    
    memory = "\n".join([f"{m['agent']}: {m['content']}" for m in log])
    prompt = f"Summarize this research in 3 bullet points:\n{memory}"
    
    summary = call_llm(prompt)
    log_agent_response(topic, "Summarizer Agent", summary)
    return summary