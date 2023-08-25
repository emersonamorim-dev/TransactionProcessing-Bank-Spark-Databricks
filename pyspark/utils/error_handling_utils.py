import logging
import time
from typing import Callable, Any

# Configuração básica de registro de logs
logging.basicConfig(filename="errors.log", level=logging.ERROR)

def handle_error(error: Exception):
    """Handle an error (e.g., log it, raise it)."""
    logging.error(f"Error occurred: {error}")
    print(f"Error occurred: {error}")

def retry_on_failure(func: Callable, retries: int = 3, delay: int = 5) -> Any:
    """Try to execute a function again after a failure."""
    for attempt in range(retries):
        try:
            return func()
        except Exception as e:
            if attempt < retries - 1:  
                time.sleep(delay)  
                continue
            else:
                handle_error(e)
                raise

def capture_and_return(func: Callable, default: Any = None) -> Any:
    """Capture an error and return a default value."""
    try:
        return func()
    except Exception as e:
        handle_error(e)
        return default

def capture_and_notify(func: Callable, notify_func: Callable) -> Any:
    """Capture an error and send a notification."""
    try:
        return func()
    except Exception as e:
        handle_error(e)
        notify_func(e)
        raise

# Função de notificação
def send_email_notification(error: Exception):
    # Aqui, você implementaria a lógica para enviar um e-mail.
    print(f"Sent email about error: {error}")

