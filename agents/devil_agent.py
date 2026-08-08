from .base import call_llm, log_agent_response, get_topic_log

def run(topic: str) -> str:
    log = get_topic_log(topic)
    if not log:
        return "No content to analyze yet."
    
    memory = "\n".join([f"{m['agent']}: {m['content']}" for m in log])
    prompt = f"Challenge assumptions and raise risks:\n{memory}"
    
    challenge = call_llm(prompt)
    log_agent_response(topic, "Devil's Advocate", challenge)
    return challenge