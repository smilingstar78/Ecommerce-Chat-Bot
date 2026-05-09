import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
from groq import Groq

# -----------------------------
# 🔐 Load API Key & Setup
# -----------------------------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# 📦 Load dataset
# -----------------------------
# Ensure the file exists or handle error
if os.path.exists("books_data.csv"):
    df = pd.read_csv("books_data.csv")
else:
    df = pd.DataFrame(columns=["name", "price", "rating", "about"])

# -----------------------------
# 🎨 Modern Styling & Config
# -----------------------------
st.set_page_config(page_title="Eco-Agent | Shopping", page_icon="🛍️", layout="centered")

st.markdown("""
    <style>
        /* Custom Chat Bubble Styling */
        .stChatMessage:has([data-testid="stChatMessageAvatarUser"]) {
            flex-direction: row-reverse;
            text-align: right;
            background-color: rgba(0, 122, 255, 0.1);
            border-radius: 15px;
            margin-left: auto;
            width: fit-content;
            max-width: 85%;
        }
        .stChatInput { border-radius: 20px; }
        .stButton button { border-radius: 10px; width: 100%; }
    </style>
""", unsafe_allow_html=True)

# -----------------------------
# 🧠 Session State Setup
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I help you find the perfect book today?"}]

if "step" not in st.session_state:
    st.session_state.step = 1

if "user_profile" not in st.session_state:
    st.session_state.user_profile = {}

# -----------------------------
# 🔍 Logic Functions
# -----------------------------
def search_products(df, query):
    query = query.lower()
    results = df[
        df["name"].str.lower().str.contains(query, na=False) | 
        df["about"].str.lower().str.contains(query, na=False)
    ]
    return results.head(5)

def ask_ai(user_query):
    results = search_products(df, user_query)
    product_text = ""
    if results.empty:
        product_text = "No matching products found."
    else:
        for _, row in results.iterrows():
            product_text += f"Name: {row['name']}\nPrice: {row['price']}\nRating: {row['rating']}\nAbout: {row['about']}\n---\n"

    system_prompt = f"You are Eco-Agent, a smart shopping assistant.\nUser Profile: {st.session_state.user_profile}\nAvailable Products:\n{product_text}\nBe helpful and recommend the best items."
    
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(st.session_state.messages[-5:]) # Send last 5 messages for context
    
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )
    return response.choices[0].message.content

# -----------------------------
# 🛠️ Sidebar Info
# -----------------------------
with st.sidebar:
    st.title("🛍️ Eco-Agent")
    st.markdown("---")
    if st.session_state.user_profile:
        st.success(f"📍 Delivering to: {st.session_state.user_profile.get('city')}")
        if st.button("Reset Location"):
            st.session_state.user_profile = {}
            st.rerun()
    else:
        st.warning("📍 Location not set")
    
    st.info("I help you search through our local book database using AI.")

# -----------------------------
# 🏠 UI: Multi-step Flow (Address)
# -----------------------------
if st.session_state.step == 2:
    with st.container(border=True):
        st.markdown("### 🤖 Location Request")
        st.write("I can calculate delivery and provide local availability if I know your location.")
        c1, c2 = st.columns(2)
        if c1.button("✅ Yes, add location"):
            st.session_state.step = 3
            st.rerun()
        if c2.button("❌ No thanks"):
            st.session_state.step = 1
            st.rerun()

elif st.session_state.step == 3:
    with st.form("location_form"):
        st.subheader("📍 Enter Delivery Details")
        addr = st.text_input("Address")
        city = st.text_input("City")
        post = st.text_input("Postcode")
        country = st.text_input("Country")
        if st.form_submit_button("Save & Continue"):
            st.session_state.user_profile = {"address": addr, "city": city, "postcode": post, "country": country}
            st.session_state.step = 1
            st.rerun()

# -----------------------------
# 💬 Chat Interface
# -----------------------------
# Main Title
st.title("Eco-Agent")
st.caption("Local AI Shopping Expert")

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input Logic
if prompt := st.chat_input("Ask me about books..."):
    # 1. Store and display user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # 2. Trigger Logic Check
    if any(word in prompt.lower() for word in ["delivery", "address", "shipping"]):
        if not st.session_state.user_profile:
            st.session_state.step = 2
            st.rerun()

    # 3. AI Response
    with st.chat_message("assistant"):
        with st.spinner("Analyzing inventory..."):
            response = ask_ai(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})