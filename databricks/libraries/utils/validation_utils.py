import re

def is_valid_email(email):
    """
    Valida se uma string é um endereço de e-mail válido.
    
    Parameters:
    - email: String contendo o endereço de e-mail a ser validado.
    
    Returns:
    - True se for um e-mail válido, False caso contrário.
    """
    email_regex = r"[^@]+@[^@]+\.[^@]+"
    return bool(re.match(email_regex, email))

def is_positive_integer(value):
    """
    Valida se um valor é um número inteiro positivo.
    
    Parameters:
    - value: Valor a ser validado.
    
    Returns:
    - True se for um número inteiro positivo, False caso contrário.
    """
    return isinstance(value, int) and value > 0
