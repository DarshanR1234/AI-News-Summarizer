# AI News Summarizer 📰🤖

AI News Summarizer is a Python-based application that fetches the latest news on any topic from the web using Tavily Search and generates concise bullet-point summaries using Mistral AI and LangChain.

The project helps users quickly understand important news without reading lengthy articles.

---

## Features

* 🔍 Search the latest news on any topic
* 🤖 Summarize news using Mistral AI
* 📝 Generate concise bullet-point summaries
* ⚡ Built with LangChain Expression Language (LCEL)
* 💬 Interactive command-line interface
* 🌐 Real-time web search with Tavily

---

## Tech Stack

* Python
* LangChain
* Mistral AI
* Tavily Search API
* python-dotenv

---

## Project Structure

```text
AI-News-Summarizer/
│
├── newsSummary.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/DarshanR1234/AI-News-Summarizer.git

cd AI-News-Summarizer
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain
pip install langchain-community
pip install langchain-mistralai
pip install tavily-python
pip install python-dotenv
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Getting API Keys

### Mistral AI

1. Create an account at https://console.mistral.ai
2. Generate an API key
3. Add it to your `.env` file

### Tavily

1. Create an account at https://tavily.com
2. Generate an API key
3. Add it to your `.env` file

---

## How It Works

### Step 1: User Enters a Topic

Example:

```text
Artificial Intelligence
```

### Step 2: Tavily Searches the Web

The application retrieves the latest news articles related to the topic.

### Step 3: Mistral AI Summarizes the News

The retrieved content is sent to Mistral AI through LangChain.

### Step 4: Summary is Displayed

The model generates concise bullet-point summaries.

---

## Running the Application

```bash
python newsSummary.py
```

---

## Example Usage

```text
📰 AI News Summarizer
Type 'exit' to quit

Enter a topic: artificial intelligence

🔍 Searching latest news about: artificial intelligence...

📝 Generating summary...

============================================================
NEWS SUMMARY
============================================================

• Open-source AI models continue gaining popularity.

• Several AI startups secured major funding rounds.

• Governments are discussing AI regulations.

• New advancements in reasoning and multimodal AI were announced.

============================================================
```

---

## Core Components

### Tavily Search Tool

```python
search_tool = TavilySearchResults(max_results=5)
```

Retrieves the latest news articles from the web.

### Mistral AI Model

```python
llm = ChatMistralAI(
    model="mistral-small-2506"
)
```

Generates summaries from search results.

### LangChain Pipeline

```python
chain = prompt | llm | StrOutputParser()
```

Processes the news and returns a clean text summary.

---

## Requirements

```txt
langchain
langchain-community
langchain-mistralai
tavily-python
python-dotenv
```

---

## Future Improvements

* News category filtering
* Multiple article summarization
* Streamlit web interface
* PDF export
* Daily news digest
* Email notifications
* Support for multiple languages

---

## Sample Workflow

```text
User Topic
     │
     ▼
Tavily Search
     │
     ▼
Latest News Results
     │
     ▼
Prompt Template
     │
     ▼
Mistral AI
     │
     ▼
Bullet Point Summary
     │
     ▼
Terminal Output
```

---

## License

MIT License

Feel free to use, modify, and distribute this project.

---

## Author

**Darshan Repale**

GitHub: https://github.com/DarshanR1234
