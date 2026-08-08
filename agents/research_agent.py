from .base import call_llm, log_agent_response

def run(topic: str, query: str) -> str:
    prompt = f"Research question: {query}\nProvide a factual, concise answer."
    answer = call_llm(prompt)
    log_agent_response(topic, "Research Agent", f"Q: {query}\nA: {answer}")
    return answer