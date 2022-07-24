from json import dump
import requests
import re


class Checker:

    headers = {"User-Agent": "Mozilla/5.0"}
    lols_gg = "https://lols.gg/en/name/checker"
    lol_names = "https://lolnames.gg/en"

    def __init__(self, nickname: str, region: str):
        self.nickname = self.valid_nickname(nickname)
        self.region = region.upper()

    def start(self) -> dict:
        return (
            {
                "statusCode": 200,
                "nickname": self.nickname,
                "region": self.region,
                "lolsGG": self.check_nickname(self.lols_gg),
                "lolNames": self.check_nickname(self.lol_names)
            }

            if self.is_request_valid()

            else {
                "statusCode": 400,
                "nickname": self.nickname,
                "region": self.region,
                "lolsGG": None,
                "lolNames": None
            }
        )

    def check_nickname(self, url: str) -> int:
        url = f"{url}/{self.region}/{self.nickname}"
        response = requests.get(url, headers=self.headers)
        return self.get_left_time(response.text)

    def is_request_valid(self) -> bool:
        return (
            2 < len(self.nickname) < 17
            and "RIOT" not in self.nickname.upper()
            and self.region in self.get_valid_regions()
        )

    def get_left_time(self, response_text: str) -> int:
        response = re.search("available in ([^.]*) days.", response_text)
        return int(response[1]) if response is not None else 0

    @staticmethod
    def get_valid_regions() -> list:
        return ["BR", "NA", "OCE", "LAS", "LAN", "EUNE", "EUW", "KR", "JP", "RU", "TR"]

    @staticmethod
    def valid_nickname(nickname: str) -> str:
        return re.sub("[^0-9a-zA-Zç ]", "", nickname)


if __name__ == "__main__":
    checker = Checker("Balaclava", "BR")
    availability = checker.start()

    with open("response.json", "w") as f:
        dump(availability, f, indent=4)
