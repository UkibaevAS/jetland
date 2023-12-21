import requests
import os
import dotenv

dotenv.load_dotenv()
cookies = {
    "cookies": os.getenv('COOKIES')
}
s = requests.Session()


async def loan_parsing() -> dict:
    url = "https://jetlend.ru/invest/api/exchange/loans?filter=%5B%7B%22values%22%3A%5B%22AAA%2B%22%2C%22AAA%22%2C%22AA%2B%22%2C%22AA%22%2C%22A%2B%22%2C%22A%22%2C%22BBB%2B%22%2C%22BBB%22%5D%2C%22field%22%3A%22rating%22%7D%5D&limit=800&offset=0&sort_dir=desc&sort_field=ytm"
    response = s.request("GET", url, cookies=cookies)

    return response.json()
