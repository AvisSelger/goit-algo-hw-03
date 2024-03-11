import re

def nolmlize_phone_number(phone_number):
    """
    normalize the phone number format.
    
    Parameters:
    - phone_number (str): The phone number in various formats.
    
    Returns:
    - str: The sanitized phone number in the format "+380XXXXXXXX".
    """
    digits = re.sub(r'\D', '', phone_number)
    if len(digits) == 10:
        digits = '38' + digits
    elif len(digits) == 9:
        digits = '380' + digits

    sanitized = '+' + digits
    return sanitized

phone_numbers = [
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [nolmlize_phone_number(number) for number in phone_numbers]
sanitized_numbers
