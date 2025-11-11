import logging
from datetime import datetime
import os

def get_logger(name="QA_LOGGER"):
    # create logs directory if it doesn't exist 
    os.makedirs("logs", exist_ok=True)

    log_file = f"logs/test_run_{datetime.now().strftime('%y%m%d_%H%M%S')}.log"

    # configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger(name)