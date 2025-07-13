# Calculator Agent

A smart tool agent built with Streamlit that can automatically determine whether to perform mathematical calculations or Google searches based on user input.

## Features

- **Smart Input Detection**: Automatically detects if the input is a mathematical expression or a search query
- **Mathematical Calculator**: Evaluates basic math expressions (addition, subtraction, multiplication, division, parentheses)
- **Google Search Integration**: Performs web searches using SerpAPI
- **Web Interface**: Clean and intuitive Streamlit-based user interface

## How It Works

The application uses a regex pattern to detect mathematical expressions. If the input matches the pattern (contains only numbers, operators, parentheses, and spaces), it uses the calculator tool. Otherwise, it performs a Google search.

### Supported Math Operations
- Basic arithmetic: `+`, `-`, `*`, `/`
- Parentheses for grouping: `(2 + 3) * 4`
- Decimal numbers: `3.14 * 2`
- Complex expressions: `(10 + 5) * (3 - 1) / 2`

## Prerequisites

- Python 3.7 or higher
- Virtual environment (recommended)

## Installation

1. **Clone or download the project**
   ```bash
   cd calculator-agent
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root with the following variables:
   ```
   SERPAPI_API_KEY=your_serpapi_key_here
   DEEPSEEK_API_KEY=your_deepseek_api_key_here
   ```
   
   **Note**: 
   - Get your SerpAPI key from [SerpAPI](https://serpapi.com/)
   - Get your DeepSeek API key from [DeepSeek](https://platform.deepseek.com/)

## Usage

### Method 1: Using the batch file (Windows)
Simply double-click `run_app.bat` to start the application.

### Method 2: Manual startup
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Run the application
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Usage Examples

### Mathematical Expressions
- `2 + 3` → Returns: `5`
- `10 * (5 - 1)` → Returns: `40`
- `3.14 * 2` → Returns: `6.28`

### Search Queries
- `Python programming` → Returns Google search results
- `weather today` → Returns Google search results
- `latest news` → Returns Google search results

## Project Structure

```
calculator-agent/
├── app.py              # Main Streamlit application
├── config.py           # Configuration and API settings
├── requirements.txt    # Python dependencies
├── run_app.bat        # Windows batch file for easy startup
├── tools/
│   ├── __init__.py
│   ├── calculator.py   # Mathematical calculation tool
│   └── google_search.py # Google search tool
└── venv/              # Virtual environment
```

## Dependencies

- **streamlit**: Web application framework
- **langchain**: Tool integration framework
- **google-search-results**: SerpAPI client for Google searches
- **python-dotenv**: Environment variable management

## Security Notes

- The calculator tool uses `eval()` for mathematical expressions, which is safe in this context as it only allows mathematical characters
- API keys are stored in environment variables for security
- Input validation is performed to prevent malicious code execution

## Troubleshooting

1. **"Module not found" errors**: Make sure you've activated the virtual environment and installed all dependencies
2. **API errors**: Verify your API keys are correctly set in the `.env` file
3. **Port already in use**: The default port is 8501. If it's busy, Streamlit will automatically use the next available port

