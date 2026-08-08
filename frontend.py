import streamlit as st
from orchestrator import run_agent, get_topic_memory, get_topic_list, delete_topic_memory

st.set_page_config(
    page_title="AthenaCore",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 AthenaCore: Multi-Agent Memory System")
st.markdown("*Collaborative AI agents with shared persistent memory*")

# Session state
if "topic" not in st.session_state:
    st.session_state.topic = None

# Sidebar
with st.sidebar:
    st.header("📂 Topics")
    topics = get_topic_list()
    
    if topics:
        for t in topics:
            col1, col2 = st.columns([4, 1])
            with col1:
                if st.button(f"📁 {t['name']} ({t['message_count']})", key=f"topic_{t['name']}"):
                    st.session_state.topic = t['name']
                    st.rerun()
            with col2:
                if st.button("🗑️", key=f"delete_{t['name']}"):
                    delete_topic_memory(t['name'])
                    st.rerun()
    else:
        st.info("No topics yet. Create one!")
    
    st.markdown("---")
    st.header("➕ New Topic")
    new_topic = st.text_input("Enter new topic name:")
    if st.button("Create Topic"):
        if new_topic:
            st.session_state.topic = new_topic
            st.rerun()
    
    st.markdown("---")
    st.header("🤖 Agents")
    st.write("""
    - 🔍 **Research** - Answers factual questions
    - 📝 **Summarizer** - Condenses knowledge
    - ⚠️ **Devil's Advocate** - Challenges assumptions
    - 💡 **Insight** - Extracts key takeaways
    """)

# Main content
if st.session_state.topic:
    st.subheader(f"📚 Topic: {st.session_state.topic}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        agent_choice = st.selectbox(
            "Select Agent",
            ["Research", "Summarizer", "Devil", "Insight"]
        )
    
    with col2:
        run_button = st.button("🚀 Run Agent", type="primary", use_container_width=True)
    
    query = ""
    if agent_choice == "Research":
        query = st.text_area("Enter research question:", placeholder="e.g., What are the latest AI trends?")
    
    if run_button:
        if not st.session_state.topic:
            st.warning("Please select or create a topic")
        elif agent_choice == "Research" and not query:
            st.warning("Please enter a research question")
        else:
            with st.spinner(f"🧠 Running {agent_choice}..."):
                result = run_agent(agent_choice, st.session_state.topic, query)
                st.subheader(f"📝 {agent_choice} Output")
                st.write(result)
            
            st.rerun()
    
    # Display memory log
    st.subheader("📜 Shared Memory Log")
    log = get_topic_memory(st.session_state.topic)
    
    if log:
        for entry in reversed(log):
            with st.expander(f"**{entry['agent']}** - 🕐 {entry.get('timestamp', 'Unknown')}"):
                st.write(entry['content'])
    else:
        st.info("No contributions yet. Run an agent to build memory!")

else:
    st.info("👈 Create a new topic or select an existing one")
    
    st.markdown("""
    ### 🧠 AthenaCore
    
    **Multi-Agent Collaboration with Persistent Memory**
    
    **How it works:**
    1. Create a research topic
    2. Run agents independently
    3. Each agent reads from and writes to shared memory
    4. Build collective knowledge over time
    """)

st.caption("🧠 AthenaCore | Powered by TinyLlama via Ollama")