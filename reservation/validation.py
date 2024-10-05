from datetime import datetime

# Modify validate_date function
def validate_date(date_str):
    try:
        # Parse the date string in 'dd-MMM-yyyy' format
        input_date = datetime.strptime(date_str, '%d-%b-%Y')  # Example: '05-Oct-2024'
        current_date = datetime.now()

        # Check if the entered date is in the past
        if input_date < current_date:
            print("Invalid date. The date entered is in the past. Please enter a valid future date.")
            return False, None

        # Return the date in MySQL-compatible format ('YYYY-MM-DD')
        formatted_date = input_date.strftime('%Y-%m-%d')
        return True, formatted_date
    except ValueError:
        print("Invalid date format. Please enter in the format 'dd-MMM-yyyy' (e.g., '16-Jan-2024').")
        return False, None
