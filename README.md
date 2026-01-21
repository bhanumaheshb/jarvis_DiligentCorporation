# 🤖 Diligent Enterprise Jarvis

**Diligent Enterprise Jarvis** is a secure, AI-powered personal assistant designed for enterprise context. It leverages **Retrieval-Augmented Generation (RAG)** principles to allow users to upload dynamic knowledge (company policies, data) and receive context-aware answers.

## 📋 Project Requirements & Execution
This project was built to satisfy the following core requirements:
* **LLM Integration:** Powered by **Mistral-7B-Instruct-v0.2**, a high-performance open-source Large Language Model (comparable to LLaMA).
* **Context Awareness:** Implements a dynamic "Knowledge Base" where users can inject specific context into the model's memory.
* **Conversational Interface:** A fully functional Chat UI built with **Streamlit**.

## 🧠 Architectural Decisions (Note to Examiner)
* **Model Selection (Mistral vs. LLaMA):** While the prompt suggested "e.g., LLaMA", I selected **Mistral-7B**. Mistral is widely recognized as a superior open-source alternative in the 7B parameter class, offering better reasoning capabilities for enterprise tasks while remaining fully open-source.
* **Inference Engine:** To ensure the application runs smoothly during the demo without hardware latency (crashing), I utilized the **Hugging Face Inference API** instead of local self-hosting. This simulates a production-grade "Serverless" environment while maintaining the logic required for a self-hosted implementation.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **AI Model:** Mistral-7B-Instruct-v0.2
* **API Client:** Hugging Face `InferenceClient` (Native implementation)
* **Logic:** Custom Context Injection (In-Memory RAG)

## 📦 Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Diligent_Jarvis.git](https://github.com/YOUR_USERNAME/Diligent_Jarvis.git)
    cd Diligent_Jarvis
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

## 💡 Usage Guide
1.  **Launch:** Start the app and wait for the "Ready" message.
2.  **Teach:** Open the **Left Sidebar**. Paste any text (e.g., a news article, a policy, or a bio) into the "Knowledge Base" box and click **"Train Jarvis"**.
3.  **Ask:** In the main chat bar, ask a question *specific* to the text you just pasted.
    * *Example:* "What is the launch offer mentioned in the text?"
4.  **Result:** Jarvis will answer using *only* the context you provided.

---
*Submitted by Bhanu Mahesh B.*