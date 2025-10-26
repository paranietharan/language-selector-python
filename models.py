from experta import Fact, Field

class Answer(Fact):
    """User's answer to a question"""
    question_id = Field(str, mandatory=True)
    value = Field(str, mandatory=True)

class Recommendation(Fact):
    """Language recommendation"""
    language = Field(str, mandatory=True)
    score = Field(int, mandatory=True)
    reason = Field(str, mandatory=True)