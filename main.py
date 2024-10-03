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
        print("\nPlease select one of the below option to proceed:")
        print("1. Make a Reservation")
        print("2. Query Reservations")
        print("3. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            bus_no = int(input("Enter Bus No (1-3): "))
            bus = BUS_INFO.get(bus_no)
            while bus_no not in BUS_INFO:
                print("Invalid Bus No. Please enter 1, 2, or 3.")
                bus_no = int(input("Enter Bus No (1-3): "))

            print("-" * 40)
            print(f"Route for bus no {bus_no} is : {bus['route']}")
            print(f"Fare from {bus['route']} is {bus['fare']} Rupees")
            print(f"Departure Time: {BUS_INFO[bus_no]['depart']}\tArrival Time: {BUS_INFO[bus_no]['arrive']}")
            print("-" * 40)

            date = input("Enter date of journey (e.g., 16-Jan-2007): ")
            while not validate_date(date):
                date = input("Enter date of journey (e.g., 16-Jan-2007): ")

            make_reservation(bus_no, date)

        elif choice == '2':
            bus_no = int(input("Enter Bus No (1-3): "))
            while bus_no not in BUS_INFO:
                print("Invalid Bus No. Please enter 1, 2, or 3.")
                bus_no = int(input("Enter Bus No (1-3): "))

            date = input("Enter date of journey (e.g., 16-Jan-2007): ")
            while not validate_date(date):
                date = input("Enter date of journey (e.g., 16-Jan-2007): ")

            query_reservations(bus_no, date)

        elif choice == '3':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
