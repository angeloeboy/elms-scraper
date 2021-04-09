import requests
from bs4 import BeautifulSoup
import sys


def get_auth():

    cookies = s.get("https://elms.sti.edu")
    soup = BeautifulSoup(cookies.content, 'html.parser')
    token = soup.select(
        'meta[name="csrf-token"]')

    authToken = token[0].get("content")
    return authToken


def login():

    data = {
        'authenticity_token': get_auth(),
        'userid': str(sys.argv[0]),
        'password': str(sys.argv[1])
    }

    s.post('https://elms.sti.edu/log_in/submit_from_portal', data=data)

    dashboard = s.get("https://elms.sti.edu/enrolled_dashboard")

    return dashboard


def main():

    soup = BeautifulSoup(login().content, 'html.parser')
    title = soup.select(
        '#centreColumn > aside > div > div:nth-child(2) > ul > div > ol')

    assignments = title[0].findAll("a")

    for assignment in assignments:
        subject = assignment.find("span").text

        if subject != "Collapse list":
            number = assignment.find(
                "span", {"class": "small_number_block"}).text
            print(subject)
            print(number)


s = requests.Session()

main()

s.close()
