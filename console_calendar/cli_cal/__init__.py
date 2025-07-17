from .cli import CalendarCLI
import sys


def main() -> None:
    cli_calendar: CalendarCLI = CalendarCLI(sys.argv[1:])
    cli_calendar.run()
