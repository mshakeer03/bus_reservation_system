from reservation.reservation import make_reservation, query_reservations
from reservation.validation import validate_date
from config import BUS_INFO

def main():
    while True:
        print("\n--- Travel Agency Reservation System ---")
        print("-" * 40)
        print("Bus No\t\tRoute")
        print("-" * 40)
        print("  1\tDelhi (DEL) to Jaipur (JAI)")
        print("  2\tDelhi (DEL) to Nainital (NAI)")
        print("  3\tDelhi (DEL) to Chandigarh (CHA)")
        print("-" * 40)
        print("\nPlease select one of the below options to proceed:")
        print("1. Make a Reservation")
        print("2. Query Reservations")
        print("3. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            bus_no = int(input("Enter Bus No (1-3): "))
            while bus_no not in BUS_INFO:
                print("Invalid Bus No. Please enter 1, 2, or 3.")
                bus_no = int(input("Enter Bus No (1-3): "))

            date = input("Enter date of journey (e.g., 16-Jan-2024): ")
            is_valid, formatted_date = validate_date(date)
            while not is_valid:
                date = input("Enter date of journey (e.g., 16-Jan-2024): ")
                is_valid, formatted_date = validate_date(date)

            route = BUS_INFO[bus_no]['route']
            fare = BUS_INFO[bus_no]['fare']
            depart_time = BUS_INFO[bus_no]['depart']
            arrival_time = BUS_INFO[bus_no]['arrive']

            # Now, pass the formatted_date (in 'YYYY-MM-DD' format) instead of the original date
            make_reservation(bus_no, formatted_date, route, fare, depart_time, arrival_time)

        elif choice == '2':
            bus_no = int(input("Enter Bus No (1-3): "))
            while bus_no not in BUS_INFO:
                print("Invalid Bus No. Please enter 1, 2, or 3.")
                bus_no = int(input("Enter Bus No (1-3): "))

            date = input("Enter date of journey (e.g., 16-Jan-2024): ")
            is_valid, formatted_date = validate_date(date)
            while not is_valid:
                date = input("Enter date of journey (e.g., 16-Jan-2024): ")
                is_valid, formatted_date = validate_date(date)

            # Use formatted_date (in 'YYYY-MM-DD' format)
            query_reservations(bus_no, formatted_date)

        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
