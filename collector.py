import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://projecteuler.net/problem={}'


def call_by_id(q_id):
    response = requests.get(BASE_URL.format(q_id))
    if response.status_code == 200:
        payload = parse_question(response.content)
        return payload
    else:
        raise ConnectionError(f"Call returned http response: {response.status_code}")


def parse_question(response_content):
    """
    Return question text
    :param response_content:
    :return:
    """
    soupy = BeautifulSoup(response_content, features="html.parser")
    q = soupy.select('.problem_content > p')

    # Site does not return 404; redirects to home
    if len(q) == 0:
        raise ValueError("No HTML for class \"problem_content\"")

    # Join text in first level <p> as paragraphs; other tags get removed
    body = "\n\n".join((''.join(val.strings) if val.string is None else val.string for val in q))

    return body
