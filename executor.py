import importlib
from time import perf_counter

FUNCTION_NAME_MAP = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


def run(question_id):
    soln_func = _get_soln_func(question_id)
    t_start = perf_counter()
    ans = soln_func()
    t_end = perf_counter()
    return ans, t_end - t_start


def _get_soln_func(q_id):
    filename, func_name = _parse_id(q_id)
    parent_module = importlib.import_module(f"solutions.{filename}")
    try:
        return getattr(parent_module, func_name)
    except AttributeError:
        raise RuntimeError(f"No solution for problem {q_id} found")


def _parse_id(q_id):
    q_id_str = str(q_id)
    mod_name = q_id_str[:-1]
    func_name = FUNCTION_NAME_MAP[q_id_str[-1]]
    return f'_{mod_name}' if mod_name != '' else '_0', func_name
