from typing import List

import requests
from bs4 import BeautifulSoup


def get_departure_time(from_station: str, to_station: str) -> List[str] | None:

    url = f'https://www.tutu.ru/rasp.php?st1={from_station}&st2={to_station}'

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the specific element containing the departure time
        departure_time = soup.find_all('a', class_='g-link desktop__depTimeLink__1NA_N')

        times = [departure.text for departure in departure_time]

        return times

    return None
