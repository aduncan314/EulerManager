from os import path

from sqlalchemy import Column, INTEGER, VARCHAR, BOOLEAN, TEXT
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_PATH_DATA = path.dirname(path.abspath(__file__))  # __name__ is data module
DATABASE_NAME = 'Euler.db'

DeclarativeBase = declarative_base()
eng = create_engine(f'sqlite:///{path.join(BASE_PATH_DATA, DATABASE_NAME)}')
Session = sessionmaker(bind=eng)
euler_sesh = Session()


class QuestionDeclarative(DeclarativeBase):
    __tablename__ = "Question"

    id = Column(INTEGER, primary_key=True, autoincrement=True)
    question_id = Column(INTEGER, unique=True)
    title = Column(VARCHAR(128))
    is_solved = Column(BOOLEAN)
    solved_value = Column(VARCHAR(64))
    min_solution_time = Column(INTEGER)
    question_text = Column(TEXT)

    def __init__(self, question_id: int):
        self.question_id = question_id
        self.stored_att = dict()
        self._get_info()

    def _get_info(self):
        self._row = euler_sesh.query(self.__class__).filter_by(question_id=self.question_id).first()
        euler_sesh.commit()
        return self._row

    @property
    def record_exists(self):
        return self._row is not None

    def _add_vals(self, **kw_values):
        """
        Add value to uninitialized instance variables

        :param kw_values: kwargs corresponding to member attributes
        :return:
        """
        for k in kw_values.keys():
            if getattr(self, k, False) is None:
                self.stored_att[k] = kw_values[k]
            else:
                raise RuntimeError(f'Value {k} is {getattr(self, k, "not found")}')

    def _update_records(self):
        euler_sesh.query(self.__class__).update(self.stored_att)
        euler_sesh.commit()

    def _add_record(self):
        euler_sesh.add(self)
        euler_sesh.commit()

    def __str__(self):
        return self.title


DeclarativeBase.metadata.create_all(eng)
