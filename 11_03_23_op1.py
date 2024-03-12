from datetime import datetime

def get_days_from_today_with_date_error_handling(date_str):
    try:
        given_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        current_date = datetime.now().date()
        delta = current_date - given_date
        return delta.days
    except ValueError as e:
        return f"Error: {str(e)}"

test_dates = ['2020-10-09', 'not-a-date', '2024-02-30']
for date in test_dates:
    print(f"Days from {date} to today: {get_days_from_today_with_date_error_handling(date)}")
