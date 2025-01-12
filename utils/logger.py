import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str, log_file: str = "app.log", level: logging.Level = logging.INFO):
    """
    Set up a logger with a RotatingFileHandler.
    
    :param name: Name of the logger.
    :param log_file: File to save the logs.
    :param level: Logging level.
    :return: Configured logger instance.
    """
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Create directory for logs if it doesn't exist
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    # Create handlers
    file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=3)  # 5 MB per log file
    console_handler = logging.StreamHandler()
    
    # Set log levels for handlers
    file_handler.setLevel(level)
    console_handler.setLevel(level)
    
    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add handlers to the logger
    if not logger.handlers:  # Avoid adding duplicate handlers
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
    
    return logger

# Example usage of the logger
if __name__ == "__main__":
    logger = setup_logger("test_logger", "logs/test.log")
    logger.info("This is an info message")
    logger.error("This is an error message")
