import collector
import executor as ex
from question import Question
from utils import input_yes_no

if __name__ == "__main__":
    try:
        question_id = None
        while question_id is None:
            try:
                cli_input = input("Choose Euler Project problem by id: ")
                question_id = int(cli_input)
                q_text = collector.call_by_id(question_id)
            except ValueError:
                print(f"{cli_input} is not a valid question id. "
                      f"Please choose a positive integer that corresponds to a real problem")
                question_id = None

            q = Question(question_id)
            print(q_text)

        run_solution = input_yes_no("Do you want to attempt to run a solution? ")

        if run_solution:
            q = Question(question_id)
            sol, t = ex.run(question_id)
            q._add_vals(solved_value=sol, min_solution_time=t)
            print(sol)
            print(t)
            q.save()

    except RuntimeError as r:
        print(f"FATAL ERROR. Exiting program\n\n\n***{r}***")
        exit(1)
