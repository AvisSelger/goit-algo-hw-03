from datetime import datetime

def get_days_from_today(date_str):
    """
    Calculate the number of days between a given date and today.
    
    Parameters:
    - date_str (str): The date in 'YYYY-MM-DD' format.
    
    Returns:
    - int: The number of days between the given date and today. If the given date is in the future,
           the returned value will be negative.
    """
    date_format = "%Y-%m-%d"
    given_date = datetime.strptime(date_str, date_format)
    today_date = datetime.now()
 
    delta = (given_date - today_date).days
    return delta

example_date = "2020-10-09"
days_diff = get_days_from_today(example_date)
days_diff
