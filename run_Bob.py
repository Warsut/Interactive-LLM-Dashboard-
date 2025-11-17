import os
os.environ["STREAMLIT_DEVELOPMENT_MODE"] = "false"
os.environ["STREAMLIT_DEV_MODE"] = "0"
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
os.environ["STREAMLIT_SERVER_PORT"] = "8501"
os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"

import streamlit.web.cli as stcli
import sys

#function to find the path
def find_path(x_path):
        #"""Works in dev and PyInstaller EXE"""
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, x_path)
        return os.path.join(os.path.abspath("."), x_path)

if __name__ == "__main__":
    sys.argv = ["streamlit", "run", find_path("Bob.py"), "--server.port=8501"]
    sys.exit(stcli.main())