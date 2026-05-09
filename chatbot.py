import os
import pandas as pd
from dotenv import load_dotenv
from groq import Groq

# -----------------------------
# 🔐 Load API Key
# -----------------------------
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# -----------------------------
# 📦 Load dataset (NO scraping here)
# -----------------------------
df = pd.read_csv("books_data.csv")

# -----------------------------
# 🧠 Memory storage
# -----------------------------
chat_history = []

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
# 🤖 Main chatbot function
# -----------------------------
def ask_ai(user_query):

    global chat_history

    # 🔍 Step 1: search products
    results = search_products(df, user_query)

    # 📦 Step 2: format products
    product_text = ""

    if results.empty:
        product_text = "No matching products found."
    else:
        for _, row in results.iterrows():
            product_text += f"""
Name: {row['name']}
Price: {row['price']}
Rating: {row['rating']}
About: {row['about']}
---
"""

    # 🧠 Step 3: system instruction
    system_prompt = f"""
You are a smart e-commerce shopping assistant.

You help users find books and recommend best options.

Use conversation history for context.

Available products:
{product_text}

Rules:
- Be friendly and short
- Recommend best product clearly
- If user asks follow-up question, use previous context
"""

    # 💬 Step 4: build messages with memory
    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(chat_history)
    messages.append({"role": "user", "content": user_query})

    # 🤖 Step 5: call Groq API
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply = response.choices[0].message.content

    # 💾 Step 6: save memory
    chat_history.append({"role": "user", "content": user_query})
    chat_history.append({"role": "assistant", "content": reply})

    return reply

# -----------------------------
# 💬 Chat loop (run in terminal)
# -----------------------------
if __name__ == "__main__":
    print("🛍️ AI Shopping Assistant Started (type 'exit' to stop)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bye 👋")
            break

        response = ask_ai(user_input)
        print("\nBot:", response)