import sys
import calendar
from typing import List


class CalendarCLI:
    def __init__(self, args: List[str]) -> None:
        self.args = args

    def run(self) -> None:
        if len(self.args) == 1:
            self.print_calendar_year()
        elif len(self.args) == 2:
            self.print_calendar_month()
        else:
            self.print_usage()
            sys.exit(1)

    def print_calendar_year(self) -> None:
        try:
            year: int = int(self.args[0])
        except ValueError:
            print("The year must be a number. Please provide a valid year!")
            sys.exit(1)

        cal = calendar.TextCalendar()
        print(cal.formatyear(year))

    def print_calendar_month(self) -> None:
        try:
            month: int = int(self.args[0])
            year: int = int(self.args[1])
            if not (1 <= month <= 12):
                raise ValueError
        except ValueError:
            print("Please provide a valid month (1-12) and year.")
            sys.exit(1)

        cal = calendar.TextCalendar()
        print(cal.formatmonth(year, month))

    def print_usage(self) -> None:
        print("Usage:")
        print(" cli_cal <year>")
        print(" cli_cal <month> <year>")
