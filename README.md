# `🐍` `League Nickname Checker`

### About me:
- ![info](https://img.shields.io/static/v1?logo=discord&label=&message=Balaclava%231912&color=00d26a&logoColor=white&style=flat)
- ![languages](https://img.shields.io/static/v1?logo=Python&label=&message=Python%203.10.5&color=00d26a&logoColor=white&style=flat)
![languages3](https://img.shields.io/static/v1?label=&message=Requests&color=00d26a&logoColor=white&style=flat)
- ![ide](https://img.shields.io/static/v1?logo=Visual%20Studio%20Code&label=&message=Visual%20Studio%20Code&color=00d26a&logoColor=white&style=flat)
![ide1](https://img.shields.io/static/v1?logo=Github&label=&message=MIT&color=00d26a&logoColor=white&style=flat)

#

### Variables:

<details>
  <summary>🍵 (class) </summary>

  ```python
    headers = {"User-Agent": "Mozilla/5.0"}
    lols_gg = "https://lols.gg/en/name/checker"
    lol_names = "https://lolnames.gg/en"
  ```

</details>

<details>
  <summary>🍵 (instance) </summary>

  ```python
    nickname = self.valid_nickname(nickname)
    region = region.upper()
  ```

</details>

#

### Instance methods:

<details>
  <summary>✅ (start) -> dict: checker response </summary>

  ```python
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
  ```

</details>

<details>
  <summary>✅ (check_nickname) -> int: get_left_time(response.text) </summary>

  ```python
    def check_nickname(self, url: str) -> int:
        url = f"{url}/{self.region}/{self.nickname}"
        response = requests.get(url, headers=self.headers)
        return self.get_left_time(response.text)
  ```

</details>

<details>
  <summary>✅ (is_request_valid) -> bool: true if the nickname follows the riot rules and is a valid region  </summary>

  ```python
    def is_request_valid(self) -> bool:
        return (
            2 < len(self.nickname) < 17
            and "Riot" not in self.nickname
            and self.region in self.get_valid_regions()
        )
  ```

</details>
<details>
  <summary>✅ (get_left_time) -> int: days left until the nick becomes available </summary>

  ```python
    def get_left_time(self, response_text: str) -> int:
        response = re.search("available in ([^.]*) days.", response_text)
        return int(response[1]) if response is not None else 0
  ```

</details>

#

### Static (class) methods:

<details>
  <summary>🌱 (get_valid_regions) -> list: with all valid regions </summary>

  ```python
    def get_valid_regions() -> list:
        return ["BR", "NA", "OCE", "LAS", "LAN", "EUNE", "EUW", "KR", "JP", "RU", "TR"]
  ```

</details>

<details>
  <summary>🌱 (valid_nickname) -> str: containing only numbers, letters and space </summary>

  ```python
    def valid_nickname(nickname: str) -> str:
        return re.sub("[^0-9a-zA-Zç ]", "", nickname)
  ```

</details>

#

### `⚠️` License:
- [MIT License](https://choosealicense.com/licenses/mit/)
