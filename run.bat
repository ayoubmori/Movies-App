@echo off
echo Running Streamlit App...
:: Redirect output to a log file, overwriting it on each run
python -m streamlit run app/main.py > logs.txt 2>&1
