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
