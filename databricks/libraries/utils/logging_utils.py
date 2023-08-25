import logging

def setup_logging(level=logging.INFO, filename=None):
    """
    Configura o logging básico para a aplicação.
    
    Parameters:
    - level: Nível de log (e.g., logging.INFO, logging.DEBUG)
    - filename: Se fornecido, os logs serão escritos neste arquivo. Caso contrário, os logs serão impressos no console.
    """
    logging.basicConfig(level=level, filename=filename, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    """Registra uma mensagem de nível INFO."""
    logging.info(message)

def log_error(message):
    """Registra uma mensagem de nível ERROR."""
    logging.error(message)

def log_warning(message):
    """Registra uma mensagem de nível WARNING."""
    logging.warning(message)
