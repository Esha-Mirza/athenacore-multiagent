from agents import research_agent, summarizer_agent, devil_agent, insight_agent
from agents.base import get_topic_log, get_all_topics, delete_topic

def run_agent(agent: str, topic: str, query: str = "") -> str:
    if agent == "Research":
        return research_agent.run(topic, query)
    elif agent == "Summarizer":
        return summarizer_agent.run(topic)
    elif agent == "Devil":
        return devil_agent.run(topic)
    elif agent == "Insight":
        return insight_agent.run(topic)
    return "Unknown agent."

def get_topic_memory(topic: str) -> list:
    return get_topic_log(topic)

def get_topic_list() -> list:
    all_topics = get_all_topics()
    topic_info = []
    for topic in all_topics:
        log = get_topic_log(topic)
        topic_info.append({
            "name": topic,
            "message_count": len(log)
        })
    return topic_info

def delete_topic_memory(topic: str) -> None:
    delete_topic(topic)