import requests
import json
import re


class Checker:

    headers = {"User-Agent": "Mozilla/5.0"}
    lols_gg = "https://lols.gg/en/name/checker"
    lol_names = "https://lolnames.gg/en"

    def __init__(self, username: str, region: str):
        self.username = self.valid_username(username)
        self.region = region.upper()

    def start(self) -> dict:
        return (
            {
                "statusCode": 200,
                "username": self.username,
                "region": self.region,
                "lolsGG": self.check(self.lols_gg),
                "lolNames": self.check(self.lol_names)
            }

            if self.is_request_valid()

            else {
                "statusCode": 400,
                "username": self.username,
                "region": self.region,
                "lolsGG": None,
                "lolNames": None
            }
        )

    def check(self, url: str) -> str:
        url = f"{url}/{self.region}/{self.username}"
        response = requests.get(url, headers=self.headers)
        return self.get_left_time(response.text)

    def valid_username(self, username: str) -> str:
        return re.sub("[^0-9a-zA-Z ]", "", username)

    def is_request_valid(self) -> bool:
        return len(self.username) > 2 and self.region in self.get_valid_regions()

    def get_left_time(self, text: str) -> int:
        response = re.search("available in ([^.]*) days.", text)
        return int(response[1]) if response is not None else 0

    def get_valid_regions(self) -> list:
        return ["BR", "NA", "OCE", "LAS", "LAN", "EUNE", "EUW", "KR", "JP", "RU", "TR"]


if __name__ == "__main__":
    checker = Checker("Balaclava", "BR")
    availability = checker.start()

    with open("response.json", "w") as f:
        json.dump(availability, f, indent=4)
