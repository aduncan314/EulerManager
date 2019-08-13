import collector
import executor
from model import Question
from utils import input_yes_no, format_cli_display


def main():
    euler_q = _choose_question()

    print(format_cli_display(euler_q.question_text, euler_q.title))
    if euler_q.is_solved:
        print(format_cli_display(
            f"Solution: {euler_q.solved_value}\nMinimum Solution Time: {euler_q.min_solution_time}"
        ))
    elif input_yes_no("\nDo you want to attempt to run a solution? "):
        solution, t = executor.run(euler_q.question_id)

        if solution == euler_q.solved_value:
            if t < euler_q.min_solution_time:
                euler_q.add_vals(min_solution_time=t)
        else:
            print(format_cli_display(
                f"Saved solution does not match calculated solution."
                f"\nCurrent Value: {euler_q.solved_value}\nNew Value: {solution}",
                title='**WARNING**'
            ))
            if print(input_yes_no('Do you want to overwrite the old data?')):
                euler_q.add_vals(solved_value=solution, min_solution_time=t, is_solved=True)
                print(format_cli_display('Values updated'))


def _choose_question() -> (int, str, str):
    while True:
        cli_input = input("Choose Euler Project problem by id: ")

        try:
            q_id = int(cli_input)
            q = Question(q_id)
            if not q.record_exists:
                q_title, q_text = collector.call_by_id(q_id)
                q.add_vals(title=q_title, question_text=q_text)
            return q
        except IndexError:
            print(f"No Euler Project problem found with id {cli_input}")
        except ValueError:
            print(f"Problem id must be an integer. Cannot cast {cli_input}")


if __name__ == "__main__":
    main()
