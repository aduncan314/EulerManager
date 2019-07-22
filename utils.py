import re

YN_OPTION_MAP = {
    'yes': ['y', 'yes', 'yup', 'ya'],
    'no': ['n', 'no', 'nope', 'na']
}


def mangle_title(title: str) -> str:
    return re.sub('\W+', '', title.title())


def input_yes_no(msg):
    usr_resp = input(msg).lower()
    while not (usr_resp in YN_OPTION_MAP['yes'] or usr_resp in YN_OPTION_MAP['no']):
        print("Please respond y/n")
        usr_resp = input(msg)

    return usr_resp in YN_OPTION_MAP['yes']
