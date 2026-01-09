# import json
# import os
# import json
# import traceback
# import pandas as pd
# from dotenv import load_dotenv
# from mcqgenrator.utils import read_file,get_table_data
# import streamlit as st
# from langchain.callbacks import get_openai_callback
# from mcqgenrator.MCQGenrator import generate_evaluate_chain

# #loading json file
# with open('C:\Complete_Content\All_Project\TEST_FOR_EVERYTHING\langchain\Response.json', 'r') as file:
#     RESPONSE_JSON = json.load(file)

# #print(RESPONSE_JSON)

# test.py (in root folder)
import os
from src.mcqgenerator import logger   # this runs your logger.py setup
import logging

def test_logging_action():
    # Trigger a log entry
    logging.info("Action successful from test.py")

    # Verify log file creation
    log_dir = os.path.join(os.getcwd(), "logs")
    files = os.listdir(log_dir)

    if files:
        print(f"✅ Log file created: {files[-1]}")
    else:
        print("❌ No log file found in logs/")

if __name__ == "__main__":
    test_logging_action()
