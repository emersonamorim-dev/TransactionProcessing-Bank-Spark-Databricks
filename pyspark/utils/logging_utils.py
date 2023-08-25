import logging

def setup_logging(level=logging.INFO, log_format=None, log_file=None):
    """Setup logging configuration."""
    if log_format is None:
        log_format = "%(asctime)s - %(levelname)s - %(message)s"
    
    logging.basicConfig(level=level, format=log_format, filename=log_file)

def log_info(message: str):
    """Log an info message."""
    logging.info(message)

def log_warning(message: str):
    """Log a warning message."""
    logging.warning(message)

def log_error(message: str):
    """Log an error message."""
    logging.error(message)

def log_critical(message: str):
    """Log a critical message."""
    logging.critical(message)

def log_debug(message: str):
    """Log a debug message."""
    logging.debug(message)

def add_log_handler(handler: logging.Handler):
    """Add a new handler to the logger."""
    logging.getLogger().addHandler(handler)

# Example usage:
setup_logging()
log_info("This is an info message.")
log_error("This is an error message.")

# To log to a file:
setup_logging(log_file="application.log")
log_info("This log will be saved to 'application.log'.")



