# 🎬 Movie AI Assistant

A premium, dark-themed cinematic web application that uses **Retrieval-Augmented Generation (RAG)** to answer questions about movies. By combining **Weaviate's** vector search with **Cohere's** LLM capabilities, this agent provides context-aware answers based on your specific movie database.

---

## ✨ Features

*   **Natural Language Search:** Move beyond keywords. Ask things like *"What's a good 80s horror movie?"* or *"Movies involving space travel and loneliness."*
*   **RAG Architecture:** The AI doesn't just guess; it retrieves the most relevant movie metadata from Weaviate and uses it to formulate a precise response.
*   **Cinematic UI:** A high-end "Premium Dark Red" interface built with **Tailwind CSS**, featuring:
    *   Glassmorphic search containers.
    *   Smooth scroll behavior and custom scrollbars.
    *   Dynamic background glows and iconic movie quotes.
*   **Asynchronous UX:** Real-time feedback and non-blocking searches using the JavaScript Fetch API.

---

## 🛠️ Technical Stack

| Component | Technology |
| :--- | :--- |
| **Frontend** | HTML5, Tailwind CSS, JavaScript (ES6+) |
| **Backend** | Python, Flask |
| **Vector Database** | Weaviate Cloud (WCS) |
| **LLM / Embeddings** | Cohere (Command R / Embed-English) |
| **Environment** | Python-Dotenv |

---

## 🚀 Getting Started

### 1. Prerequisites
*   Python 3.9+
*   A Weaviate Cloud Instance URL & API Key
*   A Cohere API Key

### 2. Installation
Clone the repository and install the required Python packages:

```bash
git clone [https://github.com/your-username/movie-ai-agent.git](https://github.com/your-username/movie-ai-agent.git)
cd movie-ai-agent
pip install flask weaviate-client cohere python-dotenv
