import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://projecteuler.net/problem={}'


def call_by_id(q_id: int) -> tuple:
    response = requests.get(BASE_URL.format(q_id))
    if response.status_code == 200:
        return _parse_question(response.content)
    else:
        raise ConnectionError(f"Call returned http response: {response.status_code}")


def _parse_question(response_content) -> (str, str):
    """
    Return question text
    :param response_content:
    :return:
    """
    soupy = BeautifulSoup(response_content, features="html.parser")
    body = soupy.select('.problem_content > p')
    title = soupy.select('h2')

    # Site does not return 404; redirects to home
    if len(body) == 0:
        # TODO: would runtime error be better since the index isn't an internal one?
        raise IndexError("No HTML found for CSS class \"problem_content\"")

    # Join text in first level <p> as paragraphs; other tags got removed
    body = '\n'.join(''.join(val.strings) if val.string is None else val.string for val in body)
    title = str(title[0].string)
    return title, body
