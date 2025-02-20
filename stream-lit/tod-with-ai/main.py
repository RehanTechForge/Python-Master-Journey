import streamlit as st
from google import genai

# Initialize Google Gemini AI
client = genai.Client(api_key="API_KEY")  # ⚠️ Apni API key yahan add karo

# Initialize session state for todos
if "todos" not in st.session_state:
    st.session_state.todos = []

if "my_text" not in st.session_state:
    st.session_state.my_text = ""

if "ai_suggestion" not in st.session_state:
    st.session_state.ai_suggestion = "AI will suggest tasks based on your to-do list."

# Function to add todo
def add_todo(task):
    if task:
        st.session_state.todos.append(task)

# Function to remove todo
def remove_todo(index):
    if 0 <= index < len(st.session_state.todos):
        del st.session_state.todos[index]

# Function to get AI suggestion
def get_ai_suggestion():
    if not st.session_state.todos:
        st.session_state.ai_suggestion = "No tasks yet. Add some tasks and get AI suggestions!"
        return

    todo_text = ", ".join(st.session_state.todos)  # Convert list to a single string
    prompt = f"My current to-do list: {todo_text}. Suggest some improvements or related tasks."

    try:
        response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
        )
        st.session_state.ai_suggestion = response.text  # AI ka response session state me store karna
    except Exception as e:
        st.session_state.ai_suggestion = "⚠️ Error getting AI suggestions."

# Streamlit UI
st.title("📝 AI-Powered To-Do App")

# ✅ Form ka use taake Enter press par hi task add ho
with st.form("todo_form", clear_on_submit=True):
    my_text = st.text_input("Enter a task:", key="my_text")
    submitted = st.form_submit_button("Add Task")
    
    if submitted:
        add_todo(my_text)
        get_ai_suggestion()  # ✅ Jab bhi naye tasks add hon, AI ka suggestion update ho
        st.rerun()

st.subheader("Your Tasks:")
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([0.8, 0.2])
    col1.write(f"{i+1}. {todo}")
    if col2.button("❌", key=f"del_{i}"):
        remove_todo(i)
        get_ai_suggestion()  # ✅ Delete hone par bhi AI ka response update ho
        st.rerun()

if not st.session_state.todos:
    st.info("No tasks added yet!")

# AI Suggestion Box
st.subheader("💡 AI Suggestions:")
st.write(st.session_state.ai_suggestion)
