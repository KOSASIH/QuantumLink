# Import necessary modules
import os
import logging
import datetime

# Define utility functions

def create_directory(directory):
    """
    Create a directory if it does not exist.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)

def setup_logging(log_file="quantumlink.log", log_level=logging.INFO):
    """
    Setup logging configuration.
    """
    logging.basicConfig(filename=log_file,
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        level=log_level)

def get_current_timestamp():
    """
    Get the current timestamp.
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
