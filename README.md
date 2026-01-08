

# AI Search Engine (A Search Engine with Langchain Tools and Agents)

A simple AI-powered search engine built with **Streamlit** and **LangChain**, using **OpenAI** models to answer user questions clearly and accurately.

# Features

* Ask any question and get AI-generated answers
* Clean and minimal Streamlit UI
* powered by OpenAI (`gpt-4o-mini`)

# Tech Stack

* **Frontend**: Streamlit
* **AI Framework**: LangChain
* **LLM**: OpenAI (ChatOpenAI)
* **Language**: Python 3.10+

# Project Structure
.
├── app.py
├── requirements.txt
├── .env
└── README.md

# Environment Setup

Create a `.env` file in the root directory and add your OpenAI API key:

OPENAI_API_KEY=your_openai_api_key_here


# Installation

1. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

2. Activate the virtual environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

# Run the Application

```bash
streamlit run app.py
```

Open your browser and go to:

```
http://localhost:8501
```

# How It Works

1. User enters a question in the input box
2. The question is sent directly to OpenAI via LangChain
3. The AI processes the request and returns a clear answer
4. The answer is displayed instantly in the UI



# Author

**Prince Raut**
A Search Engine with Langchain Tools and Agents

