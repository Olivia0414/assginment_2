from utils.currency import Currency
import sys
from argparse import ArgumentParser

def parse_arguments(cliargs):
    """
    CLI arg parser
    """
    parser = ArgumentParser(description="Currency argument parser")
    parser.add_argument(
        "--currency",
        type=str,
        help="Currency type, e.g. EUR",
    )
    parser.add_argument(
        "--period",
        type=str,
        help="Sample period in seconds, e.g. 5 means sample every 5 seconds"
    )
    parser.add_argument(
        "--time",
        type=str,
        help="Sample time in minutes, e.g, 1 means sample data for 1 minute"
    )
    return parser.parse_args(cliargs)

def main():
    """
    Main method
    """
    base_url = "https://api.freecurrencyapi.com/v1/latest"
    cli_args = sys.argv[1:]
    args = parse_arguments(cliargs=cli_args)
    currency = Currency(
        base_url, args.currency, args.period, args.time
    )
    currency.sample_currency_value()
    currency.currency_average()

if __name__ == "__main__":
    main()