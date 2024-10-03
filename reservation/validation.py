from datetime import datetime

def validate_date(date_str):
    try:
        input_date = datetime.strptime(date_str, '%d-%b-%Y')
        current_date = datetime.now()

        if input_date < current_date:
            print("Invalid date. The date is in the past.")
            return False
        return True
    except ValueError:
        print("Invalid date format. Please enter in the format 'dd-MMM-yyyy'.")
        return False
