import logging
import os

# Define the log directory and file
log_dir = "logs"
log_file = os.path.join(log_dir, "app.log")

# Create the directory if it does not exist
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),  # Log to file
        logging.StreamHandler()  # Optional: Also log to console
    ]
)

# Example log messages
logging.info("This is an info log.")
logging.error("This is an error log.")
