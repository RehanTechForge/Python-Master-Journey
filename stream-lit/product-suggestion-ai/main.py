import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
secret_key = os.getenv("MY_SECRET_KEY")

# ✅ Google Gemini API Config (Using Flash Model)
genai.configure(api_key=secret_key)

# ✅ Sample Product List
products = [
    {"name": "MacBook Pro 16-inch", "category": "Laptop", "description": "Best for professionals with M3 chip."},
    {"name": "Dell XPS 15", "category": "Laptop", "description": "Great for power users and creators."},
    {"name": "iPhone 15 Pro Max", "category": "Smartphone", "description": "Apple's latest flagship with A17 chip."},
    {"name": "Samsung Galaxy S24 Ultra", "category": "Smartphone", "description": "Flagship Android phone with S-Pen."},
    {"name": "Sony WH-1000XM5", "category": "Headphones", "description": "Industry-leading noise cancellation."},
    {"name": "Logitech MX Master 3S", "category": "Accessories", "description": "Best productivity mouse for professionals."},
]

# ✅ Initialize session state for user input & AI response
if "user_query" not in st.session_state:
    st.session_state.user_query = ""

if "ai_suggestion" not in st.session_state:
    st.session_state.ai_suggestion = "Click 'Best Product AI Suggestion' to get a recommendation!"

# ✅ Function to Get AI Suggestions Based on User Input
def get_ai_recommendation(user_query):
    product_text = "\n".join([f"{p['name']} ({p['category']}): {p['description']}" for p in products])

    prompt = f"""
    Here is a list of available products:
    {product_text}

    The user is looking for: "{user_query}"
    
    Based on the above product list, suggest the best matching products with a short reason.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Using "gemini-1.5-flash"
        response = model.generate_content(prompt)
        print(response)
        return response.text
    except Exception as e:
        return "⚠️ Error fetching AI recommendation."

# ✅ Function to Get Best Product Without User Input
def get_best_product():
    product_text = "\n".join([f"{p['name']} ({p['category']}): {p['description']}" for p in products])

    prompt = f"""
    Here is a list of available products:
    {product_text}

    Without any user input, suggest the absolute best product from this list for general users.
    Explain why it is the best choice.
    """

    try:
        model = genai.GenerativeModel("gemini-1.5-flash")  # ✅ Using "gemini-1.5-flash"
        response = model.generate_content(prompt)
        print(response)
        st.session_state.ai_suggestion = response.text
    except Exception as e:
        st.session_state.ai_suggestion = "⚠️ Error fetching AI best product."

# ✅ Streamlit UI
st.title("🛍️ AI-Powered Product Recommendation")

# ✅ Form for User Input
with st.form("query_form", clear_on_submit=True):
    st.session_state.user_query = st.text_input("What are you looking for?", value=st.session_state.user_query)
    submitted = st.form_submit_button("Search")

    if submitted:
        st.session_state.ai_suggestion = get_ai_recommendation(st.session_state.user_query)
        st.session_state.user_query = ""  # ✅ Input clear karna
        st.rerun()  # ✅ UI refresh

# ✅ AI Best Suggestion Button
if st.button("Best Product AI Suggestion"):
    get_best_product()
    st.rerun()  # ✅ UI refresh taake AI response show ho

# ✅ AI Response Section
st.subheader("🤖 AI Recommendations:")
st.write(st.session_state.ai_suggestion)

# ✅ Show Available Products
st.subheader("📦 Available Products:")
for product in products:
    st.markdown(f"**{product['name']}** ({product['category']}) - {product['description']}")
