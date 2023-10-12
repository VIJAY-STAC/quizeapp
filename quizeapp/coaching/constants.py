import enum

class QuestionType(enum.Enum):
    """Question type enum."""
    MULTIPLE_CHOICE = 1
    SINGLE_CHOICE = 2
    TEXT = 3

class AnswerStatus(enum.Enum):
    """Answer status enum."""
    CORRECT = "correct"
    INCORRECT = "incorrect"
    NOT_ANSWERED =  "not_answered"


ANSWER_STATUS_CHOICES = (
    ("correct", "Correct"),
    ("incorrect", "Incorrect"),
    ("not_answered", "Not Answered"),
)