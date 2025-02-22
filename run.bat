@echo off
:: Set the title of the command prompt window
title Streamlit App Runner

:: Clear the screen for better readability
cls

:: Run the Streamlit app
echo Running Streamlit App...
echo Press Ctrl+C to stop the app.

:: Run the app without requiring 'y' to terminate
python -m streamlit run app/main.py

:: Check if the app exited with an error
if %ERRORLEVEL% neq 0 (
    echo The Streamlit app encountered an error.
    pause
    exit /b 1
)

:: Success message
echo Streamlit app stopped successfully.
pause