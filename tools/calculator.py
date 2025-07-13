from langchain.tools import tool

@tool
def calculator(expression: str) -> str:
    """Evaluate a basic math expression like 2 + 3 or 10 * (5 - 1)."""
    try:
        allowed = "0123456789+-*/(). "
        if all(char in allowed for char in expression):
            return str(eval(expression))
        else:
            return "Invalid expression."
    except Exception as e:
        return f"Error: {e}"
