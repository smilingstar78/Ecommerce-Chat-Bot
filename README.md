# 🛍️ Eco-Agent: AI-Powered Shopping Assistant

<div align="center">

### *An intelligent e-commerce chatbot powered by Generative AI, product retrieval, and conversational memory.*

🚀 Built with Python • Streamlit • Groq • Pandas • BeautifulSoup

</div>

---

## 🌟 Overview

Eco-Agent is an intelligent shopping assistant designed to simulate a real-world e-commerce support experience.

Instead of a traditional keyword-based search system, Eco-Agent combines:

✅ Product data retrieval  
✅ Conversational memory  
✅ Guided order workflow  
✅ AI-powered recommendations  
✅ Smart user interaction  

to create a personalized shopping experience.

Users can:

- 🔍 Search for books naturally
- 💬 Chat with an AI shopping assistant
- 🎯 Get personalized recommendations
- 🛒 Place orders through conversation
- 📦 Provide shipping details interactively
- 🧠 Continue conversations with memory

---

# ✨ Features

## 🤖 Conversational AI
Natural language shopping conversations powered by Groq LLM.

Examples:

> “Recommend me a beginner Python book.”

> “I need something under £20.”

> “Do you have highly rated fiction books?”

---

## 📚 Smart Product Retrieval
Instead of hallucinating products, Eco-Agent searches a real scraped product database.

Features:

- Product matching
- Product filtering
- Top recommendation retrieval
- Context-aware product suggestions

---

## 🧠 Conversation Memory
Eco-Agent remembers previous interactions.

Example:

User:

> Show me cheap books.

Then:

> What about highly rated ones?

The assistant understands the context.

---

## 🛒 Guided Order Workflow

Eco-Agent follows a structured purchase flow:

```text
Search Product
      ↓
Recommendation
      ↓
Order Confirmation
      ↓
Shipping Details
      ↓
Order Placement
```

The assistant only confirms orders when the user explicitly says:

> Confirm my order

---

## 📍 Smart Address Collection

After order confirmation, Eco-Agent collects:

- Address
- City
- Postcode
- Country

If information is missing, the assistant asks again.

---

## 💻 Beautiful Interactive UI

Built using Streamlit with:

- Left/right aligned chat messages
- Persistent chat history
- Responsive design
- Clean user experience

---

# 🏗️ Project Architecture

```text
                 User Query
                     │
                     ▼
            Streamlit Frontend
                     │
                     ▼
          Conversational Engine
                     │
      ┌──────────────┼──────────────┐
      ▼                              ▼
 Product Retrieval              Memory Engine
 (Pandas Dataset)             (Session State)
      │                              │
      └──────────────┬──────────────┘
                     ▼
                 Groq LLM
                     │
                     ▼
              AI Response
```

---

# 🛠️ Tech Stack

## Backend

- Python

## AI

- Groq API
- Llama 3.1

## Data Processing

- Pandas

## Web Scraping

- BeautifulSoup
- Requests

## Frontend

- Streamlit

## Environment Management

- python-dotenv

---

# 📂 Project Structure

```text
Eco-Agent/
│
├── scraper.py
├── chatbot.py
├── books_data.csv
├── .env
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## 1 Clone repository

```bash
git clone <your-repository-url>
cd Eco-Agent
```

---

## 2 Create virtual environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Setup environment variables

Create `.env`

```env
GROQ_API_KEY=your_api_key_here
```

---

## 5 Run scraper

```bash
python scraper.py
```

*(Only needed once)*

---

## 6 Launch application

```bash
streamlit run app.py
```

---

# 💬 Example Conversation

```text
👤 User:
Recommend me beginner Python books.

🤖 Eco-Agent:
I found some excellent beginner-friendly options for you.

👤 User:
I want something under £20.

🤖 Eco-Agent:
Here are the best matches within your budget.

👤 User:
Confirm my order.

🤖 Eco-Agent:
Great! Please provide your shipping address.
```

---

# 🧠 AI Design Philosophy

Eco-Agent follows a hybrid architecture:

### Rule-Based Logic
For:

- Order confirmation
- Address collection
- Workflow control

### LLM Intelligence
For:

- Natural conversations
- Product explanations
- Personalized recommendations

This creates a reliable and production-friendly conversational system.

---

# 🔮 Future Improvements

- Semantic search with embeddings
- Vector database integration
- Product image recommendations
- Multi-category shopping
- Payment gateway integration
- Order tracking system

---

# 👩‍💻 Author

**Muskan Tariq**

AI Engineer • Machine Learning Enthusiast • Generative AI Explorer

---

## 📬 Contact Me

Connect with me through any of the platforms below:

<p align="center">
  <a href="https://www.linkedin.com/in/muskan-tariq-095a50282/" target="_blank">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
  <a href="https://www.instagram.com/ai_enthusiast86?igsh=dnRyenAwdTBxdTZ6" target="_blank">
    <img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" />
  </a>
  <a href="mailto:muskantariq2003@gmail.com" target="_blank">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" />
  </a>
  <a href="https://www.youtube.com/@ai_enthusiast86?si=bYV1AgkBoCMVUBiK" target="_blank">
    <img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />
  </a>
</p>

----

# ⭐ Support

If you found this project interesting:

⭐ Star this repository  
🍴 Fork it  
💡 Share your feedback  

---

<div align="center">

### Built with ❤️, Python, and Generative AI

</div>
