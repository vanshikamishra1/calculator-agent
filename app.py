import streamlit as st
import re
from tools.calculator import calculator
from tools.google_search import google_search

def is_math_expression(text: str) -> bool:
    pattern = r"^\s*[\d\s\+\-\*/\(\)\.]+\s*$"
    return bool(re.match(pattern, text))

st.set_page_config(page_title="Tool Agent")
st.title("Tool Agent")

user_input = st.text_input("Enter input:")

if user_input:
    if is_math_expression(user_input):
        result = calculator(user_input)
        tool_used = "Calculator"
    else:
        result = google_search(user_input)
        tool_used = "Google Search"

    st.write(f"Tool: {tool_used}")
    st.write(f"Result: {result}")
