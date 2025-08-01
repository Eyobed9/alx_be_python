from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date
    
def calculate_future_date(current, days):
    future_date = (current + timedelta(days=days))
    return future_date.strftime('%Y-%m-%d')
    
def main():
    current = display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(current, days)
    print(f"Future date: {future_date}")
    
if __name__ == "__main__":
    main()