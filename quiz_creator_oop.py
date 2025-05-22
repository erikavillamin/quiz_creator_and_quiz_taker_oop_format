import emoji

class QuizCreator:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename
    
    def quiz_question(self):
        question = input(emoji.emojize("Enter a question :thinking_face:: "))
        if not question.lower().startswith("question:"):
            question = "Question: " + question
        return question