import os
os.environ["STREAMLIT_DEVELOPMENT_MODE"] = "false"
os.environ["STREAMLIT_DEV_MODE"] = "0"
os.environ["STREAMLIT_WATCHER_TYPE"] = "none"
os.environ["STREAMLIT_SERVER_PORT"] = "8501"
os.environ["STREAMLIT_GLOBAL_DEVELOPMENT_MODE"] = "false"

import streamlit.web.cli as stcli
import sys

#function to find the path of the file that it is given (note: MEIPASS is the temporary folder pyinstaller makes, which is why we need this)
def find_path(file_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, file_path) #return the pyinstaller path
        return os.path.join(os.path.abspath("."), file_path) #return the current directory path plus the given file path


# run Bob, streamlit run Bob.py (typical command we put in console), and then make the port 8501, very important the port is 8501 
if __name__ == "__main__":
    sys.argv = ["streamlit", "run", find_path("Bob.py"), "--server.port=8501"]
    sys.exit(stcli.main())