import requests
from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB("memory/memory_store.json")
Topic = Query()

MODEL = "tinyllama"
OLLAMA_URL = "http://localhost:11434/api/generate"

def call_llm(prompt: str) -> str:
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "max_tokens": 300
            },
            timeout=30
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Error: {str(e)}"

def log_agent_response(topic: str, agent: str, content: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if db.contains(Topic.name == topic):
        db.update(
            lambda t: t["log"].append({"agent": agent, "content": content, "timestamp": timestamp}),
            Topic.name == topic
        )
    else:
        db.insert({
            "name": topic,
            "log": [{"agent": agent, "content": content, "timestamp": timestamp}]
        })

def get_topic_log(topic: str):
    result = db.search(Topic.name == topic)
    return result[0]["log"] if result else []

def get_all_topics():
    return [item["name"] for item in db.all()]

def delete_topic(topic: str):
    db.remove(Topic.name == topic)