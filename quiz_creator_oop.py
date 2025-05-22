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
    
    def quiz_correct_answer(self):
        while True:
            correct_ans = input(emoji.emojize("What letter is the correct answer? :thinking_face: ")).strip().lower()
            if correct_ans in ['a', 'b', 'c', 'd']:
                return correct_ans
            else:
                print(emoji.emojize("Invalid. Please enter a, b, c, or d only. :police_car_light:"))

    def save_question(self, question, choices, correct_ans):
        file_save = input("Do you want to save this question? (yes/no): ").strip().lower()
        if file_save in ["yes", "y"]:
            with open(self.filename, "a") as file:
                file.write(question + "\n")
                file.write("a) " + choices[0] + "\n")
                file.write("b) " + choices[1] + "\n")
                file.write("c) " + choices[2] + "\n")
                file.write("d) " + choices[3] + "\n")
                file.write("Answer: " + correct_ans + "\n\n")
            print(emoji.emojize("Question saved! :grinning_face_with_smiling_eyes:\n"))
        else:
            print(emoji.emojize("Question not saved. :frowning_face:\n"))