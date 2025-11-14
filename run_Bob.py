from streamlit.web import cli

if __name__ == "__main__":
    #cli._main_run_clExplicit('Bob.py', 'streamlit run')
    #cli._main_run_clExplicit("streamlit", "run", "Bob.py", "--server.port", "8501")
    cli._main_run_clExplicit("Bob.py", "streamlit run", "--server.port", "3000")
