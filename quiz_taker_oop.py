import tkinter as tk
import random

background_color = "#FFFFFF"  # white
text_color = "#000000"    # black
accent_color = "#FF8C00"    # orange

class QuizTakerApp:
    def __init__(self, app_window, quiz_questions):
        self.app_window = app_window
        self.app_window.title("Quiz Taker App")
        self.app_window.configure(bg=background_color)
        self.quiz_questions = quiz_questions
        self.current_question_index = 0
        self.total_score = 0
        self.selected_option = tk.StringVar()
        self.timer_secs = 15
        self.timer_id = None

        self.question_text_label = tk.Label(
            app_window, text="", wraplength=400,
            font=("Arial", 14, "bold"), bg=background_color, fg=accent_color
        )
        self.question_text_label.pack(pady=20)

        self.answer_option_buttons = []
        for _ in range(4):
            option_button = tk.Radiobutton(
                app_window, text="", variable=self.selected_option, value="",
                font=("Arial", 12), anchor='w', justify='left',
                bg=background_color, fg=text_color, selectcolor=background_color,
                activeforeground=accent_color
            )
            option_button.pack(fill='x', padx=20, pady=2)
            self.answer_option_buttons.append(option_button)

        self.timer_label = tk.Label(
            app_window, text="", font=("Arial", 12),
            bg=background_color, fg="#FF0000"
        )
        self.timer_label.pack()

        self.answer_feedback_label = tk.Label(
            app_window, text="", font=("Arial", 12),
            bg=background_color, fg=text_color
        )
        self.answer_feedback_label.pack(pady=5)

        self.submit_button = tk.Button(
            app_window, text="Submit", command=self.submit_answer,
            font=('Arial', 12), bg=accent_color, fg=background_color, activebackground="#ffa733"
        )
        self.submit_button.pack(pady=20)

        self.final_result_label = tk.Label(
            app_window, text="", font=("Arial", 16, "bold"),
            bg=background_color, fg=accent_color
        )
        self.final_result_label.pack(pady=10)

        self.display_next_question()
        
    def display_next_question(self):
        self.answer_feedback_label.config(text="")
        if self.current_question_index >= len(self.quiz_questions):
            self.display_final_score()
            return

        self.selected_option.set(None)
        current_question = self.quiz_questions[self.current_question_index]
        self.question_text_label.config(
            text=(f"Q{self.current_question_index + 1}: {current_question['question']}")
        )
        for i, choice in enumerate(current_question['choices']):
            choice_value = choice[0].upper()
            self.answer_option_buttons[i].config(
                text=choice, value=choice_value, state=tk.NORMAL
            )
        self.timer_secs = 15
        self.update_timer()
    
    def update_timer(self):
        self.timer_label.config(text=(f"Time left: {self.timer_secs} seconds"))
        if self.timer_secs > 0:
            self.timer_secs -= 1
            self.timer_id = self.app_window.after(1000, self.update_timer)
        else:
            self.answer_feedback_label.config(text="Time's up!")
            self.submit_answer(skip_check=True)

    def submit_answer(self, skip_check=False):
        if self.timer_id:
            self.app_window.after_cancel(self.timer_id)
            self.timer_id = None

        user_answer = self.selected_option.get()
        correct_answer = self.quiz_questions[self.current_question_index]['answer']
        if not skip_check and user_answer == correct_answer:
            self.total_score += 1
        self.current_question_index += 1
        self.display_next_question()

    def display_final_score(self):
        self.question_text_label.config(text="Quiz Finished!")
        for button in self.answer_option_buttons:
            button.pack_forget()
        self.submit_button.pack_forget()
        self.answer_feedback_label.pack_forget()
        self.timer_label.pack_forget()

        total_questions = len(self.quiz_questions)
        percentage = (self.total_score / total_questions) * 100

        if percentage >= 80:
            feedback_text = "Excellent work!"
            score_color = "#28a745"  # green
        elif percentage >= 50:
            feedback_text = "Good job!"
            score_color = "#FFA500"  # orange
        else:
            feedback_text = "Better luck next time!"
            score_color = "#FF4C4C"  # red

        result_frame = tk.Frame(self.app_window, bg=background_color, bd=2, relief="ridge")
        result_frame.pack(pady=20, padx=30)

        result_label = tk.Label(
            result_frame,
            text=f"Your Score: {self.total_score}/{total_questions} ({int(percentage)}%)\n{feedback_text}",
            font=("Arial", 16, "bold"),
            fg=score_color,
            bg=background_color,
            justify="center"
        )
        result_label.pack(padx=20, pady=20)

        restart_button = tk.Button(
            self.app_window,
            text="Retake Quiz",
            font=('Arial', 12),
            bg=accent_color,
            fg=background_color,
            activebackground="#ffa733",
            command=self.restart_quiz
        )
        restart_button.pack(pady=10)