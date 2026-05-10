import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# -----------------------------
# 🔐 Setup & Page Config
# -----------------------------
load_dotenv()
st.set_page_config(page_title="AI Book Finder", page_icon="📚")
st.title("📚 AI Shopping Assistant")

# Initialize Groq Client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# 📦 Load dataset (Cached for speed)
# -----------------------------
@st.cache_data
def load_data():
    # Ensure this file exists in your directory
    return pd.read_csv("books_data.csv")

df = load_data()

# -----------------------------
# 🧠 Session State (Memory)
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 🔍 Search function
# -----------------------------
def search_products(df, query):
    query = query.lower()
    results = df[
        df["name"].str.lower().str.contains(query, na=False)
        | df["about"].str.lower().str.contains(query, na=False)
    ]
    return results.head(5)

# -----------------------------
# 🤖 AI Logic
# -----------------------------
def get_ai_response(user_query):
    # 1. Search products
    results = search_products(df, user_query)
    
    product_text = "No matching products found." if results.empty else ""
    if not results.empty:
        for _, row in results.iterrows():
            product_text += f"Name: {row['name']} | Price: {row['price']} | Rating: {row['rating']}\nAbout: {row['about']}\n---\n"

    # 2. System Prompt
    system_prompt = f"""
    You are a smart e-commerce shopping assistant. 
    Help users find books and recommend the best options.
    
    Available products from database:
    {product_text}

    Rules:

1. Be friendly, concise, and helpful.

2. Recommend the most suitable product based on the user's needs, preferences, and budget.

3. If no matching products are found, politely ask the user to try different keywords or refine their request.

4. Don't add to cart unless User says.

5. Answer only the question the user has asked.

6. Do NOT place or confirm an order automatically.

7. Only confirm an order when the user explicitly says:
   "Confirm my order"

8. After the order is confirmed, ask for the shipping address.

9. If the shipping address is incomplete or missing, politely ask again until all required details are provided:
   - Address
   - City
   - Postcode
   - Country

10. Once the shipping details are complete, acknowledge the order and confirm that it has been placed successfully.
    """

    # 3. Build message context
    messages = [{"role": "system", "content": system_prompt}]
    # Add history from session state
    for msg in st.session_state.messages:
        messages.append({"role": msg["role"], "content": msg["content"]})
    
    messages.append({"role": "user", "content": user_query})

    # 4. API Call
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content

# -----------------------------
# 🎨 UI Display
# -----------------------------
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Search for a book... (e.g., 'fantasy novels under $20')"):
    # User message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Assistant message
    with st.chat_message("assistant"):
        response = get_ai_response(prompt)
        st.markdown(response)
    
    st.session_state.messages.append({"role": "assistant", "content": response})