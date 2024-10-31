import os
from dotenv import load_dotenv
from functools import wraps
import glob
import warnings
def load_env_from_dir(directories):
    """
    Decorator to load environment variables from .env and .Renviron files
    located in the specified directory.

    :param directories: Comma-separated directories where .env and .Renviron files are located.
    """
    # Split directories and check for .Renviron and .env files
    dirs = directories.split(',')
    filepath = os.path.dirname(os.path.abspath(__file__))
    dirs = filepath if not dirs else dirs
    if filepath != os.getcwd():
        warnings.warn('Script directory is differnt from working directory. Using script directory.')
    for directory in dirs:
        # Check for .Renviron
        renviron_file_path = os.path.join(directory, ".Renviron")
        if os.path.exists(renviron_file_path):
            load_dotenv(renviron_file_path)
            print(f"Loaded environment variables from: {renviron_file_path}")
        # Check for anything with env in filename
        env_file_path = env_files = glob.glob(os.path.join(directory, "*env*"))
        if os.path.exists(env_file_path):
            load_dotenv(env_file_path)
            print(f"Loaded environment variables from: {env_file_path}")
