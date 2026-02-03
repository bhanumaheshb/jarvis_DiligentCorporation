import streamlit as st
from huggingface_hub import InferenceClient

# -------------------------------
# App Configuration
# -------------------------------
st.set_page_config(page_title="Diligent Jarvis", page_icon="🤖")

# -------------------------------
# HuggingFace API Key
# -------------------------------
HF_TOKEN = "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"

# -------------------------------
# Create AI Client (cached)
# -------------------------------
@st.cache_resource
def create_client():
    client = InferenceClient(token=HF_TOKEN)
    return client

# -------------------------------
# AI Response Logic
# -------------------------------
def get_ai_response(question, company_context):
    client = create_client()

    messages = [
        {
            "role": "system",
            "content": "You are a helpful enterprise assistant. "
                       "Use the given company data to answer user questions.\n\n"
                       "Company Data:\n" + company_context
        },
        {
            "role": "user",
            "content": question
        }
    ]

    try:
        response = client.chat_completion(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=messages,
            max_tokens=500,
            temperature=0.5
        )

        answer = response.choices[0].message.content
        return answer

    except Exception as error:
        return "AI connection error: " + str(error)

# -------------------------------
# UI Layout
# -------------------------------
st.title("🤖 Diligent Enterprise Jarvis")

# Store company knowledge
if "knowledge_base" not in st.session_state:
    st.session_state.knowledge_base = ""

# Sidebar for training data
with st.sidebar:
    st.header("Knowledge Base")
    company_data = st.text_area("Paste Company Data Here:", height=150)

    if st.button("Train Jarvis"):
        st.session_state.knowledge_base = company_data
        st.success("Knowledge base updated successfully!")

# Store chat messages
if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"role": "assistant", "content": "System ready. Ask your questions."}
    ]

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_question = st.chat_input("Ask a question...")

if user_question:
    # Show user message
    st.session_state.chat_history.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.write(user_question)

    # Generate AI reply
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if st.session_state.knowledge_base:
                context_data = st.session_state.knowledge_base
            else:
                context_data = "No company data provided."

            ai_reply = get_ai_response(user_question, context_data)
            st.write(ai_reply)

    # Save AI reply
    st.session_state.chat_history.append(
        {"role": "assistant", "content": ai_reply}
    )
