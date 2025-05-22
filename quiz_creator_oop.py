import emoji

class QuizCreator:
    def __init__(self, filename="quiz_questions.txt"):
        self.filename = filename

    def quiz_question(self):
        question = input(emoji.emojize("Enter a question :thinking_face:: "))
        if not question.lower().startswith("question:"):
            question = "Question: " + question
        return question
    
    def quiz_choices(self):
        letter_a = input(emoji.emojize("Enter letter a :red_apple:: ")).strip()
        letter_b = input(emoji.emojize("Enter letter b :boy:: ")).strip()
        letter_c = input(emoji.emojize("Enter letter c :cow:: ")).strip()
        letter_d = input(emoji.emojize("Enter letter d :dog:: ")).strip()
        return letter_a, letter_b, letter_c, letter_d