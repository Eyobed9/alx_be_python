from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date
    
def calculate_future_date(current, days):
    future_date = (current + timedelta(days=days)).strftime('%Y-%m-%d')
    print(f"Future date: {future_date}")
    
def main():
    current = display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(current, days)
    
if __name__ == "__main__":
    main()