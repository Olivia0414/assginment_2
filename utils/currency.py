import requests
from requests.structures import CaseInsensitiveDict
import os
import logging
import time
import pandas

# url = "https://api.freecurrencyapi.com/v1/latest?currencies=EUR"


logging.basicConfig(
    filename='currency_avg.log',
    format="%(levelname)s -- %(message)s",
)
log = logging.getLogger(__name__)
log.setLevel(level=logging.DEBUG)


class CurrencyException(Exception):
    """
    Custom exception for class CurrencyRequest
    """

class Currency:
    """
        Currency class
    """
    def __init__(self, base_url, currency, sample_period, sample_time):
        self.base_url = base_url
        self.currency = currency
        self.sample_period = int(sample_period)
        self.sample_time = int(sample_time) * 60
        self.headers = CaseInsensitiveDict()
        self.headers["apikey"] = os.environ.get("API_TOKEN")   #"jCapRYOERxQ8W0AyfRwph8yEK8v1YkLq4m3yd4W5"
        self.currency_values=[] ## An empty list to stored sampled currency values 

    def get_json_data(self):
        """
            Send currenty data request via API and return JSON data
        """
        api_url = self.base_url + "?currencies=" + self.currency
        req = requests.get(api_url, headers=self.headers)

        if (req.status_code != 200):
            raise CurrencyException(f"Failed to get data: {req.reason}")
        return req.json()
        
    def sample_currency_value(self):
        """
            Sample currency data based on sample period and sample time given
        """
        cycles = self.sample_time // self.sample_period + 1
        for _ in range(cycles):
            data = self.get_json_data()
            currency_value = data["data"][self.currency]
            self.currency_values.append(currency_value)
            print(f"USD to {self.currency} exchange is: {currency_value}")
            log.info(f"USD to {self.currency} exchange is: {currency_value}")
            time.sleep(self.sample_period)

    def currency_average(self):
        """
            Calculate average of sampled currency values and write to a log file
        """
        currency_avg = sum(self.currency_values) / len(self.currency_values)
        log.info(f"USD to {self.currency} exchange average value over the last {self.sample_time}: {currency_avg}")

