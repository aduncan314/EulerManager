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


def format_cli_display(lines: str, title=None) -> str:
    split_lines = lines.split('\n')
    max_line_len = max(map(len, split_lines))
    body = "\n|\n|  ".join(split_lines)

    line_break = '*' * (max_line_len + 1)

    if title is None:
        return f"|  {'*' * (max_line_len + 1)}\n|  {body}\n|  {'*' * (max_line_len + 1)}"
    else:
        title_line = f"{' ' * int(0.5 * (max_line_len - len(title)))}{title.capitalize()}\n|  {line_break}"
        return f"|  {line_break}\n|  {title_line}\n|  {body}\n|  {line_break}"
