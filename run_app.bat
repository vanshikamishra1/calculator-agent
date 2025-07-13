@echo off
cd /d C:\Users\vansh\OneDrive\Desktop\calculator-agent

call venv\Scripts\activate.bat

echo Running the Streamlit Calculator Agent...
call venv\Scripts\python.exe -m streamlit run app.py

pause
