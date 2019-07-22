import logging

from model import QuestionDeclarative
from utils import input_yes_no

logger = logging.getLogger(__name__)


class Question(QuestionDeclarative):
    def __init__(self, question_id: int):
        super().__init__(question_id)

    def save(self):
        if len(self.stored_att) < 1:
            logger.warn("No values to save")
        else:
            if not self.record_exists:
                logger.warn(f'No record exists for id {self.question_id}\n\tAdding record')
                self._add_record()
            else:
                self._update_records()

    @property
    def title(self):
        return self.title

    @title.setter
    def title(self, new_title, is_interactive=False):
        self.title = new_title if self.title is None else self.title
        if is_interactive:
            self.title = new_title if input_yes_no("Do you want to overwrite the old title with the new (y/n):"
                                                   f"\n\tOld title: {self.title}\n\tNew title:{new_title}"
                                                   ) else self.title

    @property
    def is_solved(self):
        return self.is_solved

    @property
    def solved_value(self):
        return self.solved_value

    @property
    def min_solution_time(self):
        return self.min_solution_time

    @property
    def question_text(self):
        return self.question_text
