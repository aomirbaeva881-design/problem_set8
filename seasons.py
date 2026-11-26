from datetime import date
import inflect
import sys
def calculate_minutes(birth,today):
    return (today-birth).days*1440
def main():
    try:
        birth=date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    minutes=calculate_minutes(birth, date.today())
    p=inflect.engine()
    print(p.number_to_words(minutes, andword="").capitalize() + " minutes")
if __name__ == "__main__":
    main()