import os
from dotenv import load_dotenv
from functools import wraps

def load_env_from_dir(directories):
    """
    Decorator to load environment variables from .env and .Renviron files
    located in the specified directory.

    :param directories: Comma-separated directories where .env and .Renviron files are located.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Split directories and check for .Renviron and .env files
            dirs = directories.split(',')
            for directory in dirs:
                renviron_file_path = os.path.join(directory, ".Renviron")
                if os.path.exists(renviron_file_path):
                    load_dotenv(renviron_file_path)
                    print(f"Loaded environment variables from: {renviron_file_path}")
                else:
                    print(f"Warning: {renviron_file_path} does not exist. Skipping load.")

                # Check for .env file
                env_file_path = os.path.join(directory, ".env")
                if os.path.exists(env_file_path):
                    load_dotenv(env_file_path)
                    print(f"Loaded environment variables from: {env_file_path}")
                else:
                    print(f"Warning: {env_file_path} does not exist. Skipping load.")
                
            return func(*args, **kwargs)

        return wrapper
    return decorator

#curr = str(os.getcwd())
#@load_env_from_dir(curr)
#def main():
#    # Access your environment variables
#    my_var = os.getenv('sms_database')
#    print(f'sms_database: {my_var}')

#if __name__ == "__main__":
#    main()