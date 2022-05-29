# questions.json model used for program
# displaying 10 questions.json
# if says 'process finished with exit code 0' it means it works

class QuizQuestions:
    def __init__(self, q_num, question, O1_text, O2_text, O3_text,
                 O4_text, answer):
        self.q_num = q_num
        self.question = question
        self.btn1_text = O1_text
        self.btn2_text = O2_text
        self.btn3_text = O3_text
        self.btn4_text = O4_text
        self.answer = answer


# Questions
q1 = QuizQuestions(1, "How to say 'Christchurch'", "Ahuriri", "Otautahi", "Ngamotu",
                 "Waiharakeke")
q2 = QuizQuestions(2, "What colour is 'kākāriki' ?", "Yellow", "Blue", "Green",
                 "Orange", "Green")
q3 = QuizQuestions(3, "What is 'orange' in Maori ?", "Karaka", "Kahurangi",
                 "Kākāriki", "Ngako", "Karaka")
q4 = QuizQuestions(4, "What colour is 'papura' ?", "Red", "Violet", "Yellow",
                 "Purple", "Purple")
q5 = QuizQuestions(5, "What is 'yellow' in Maori ?", "Whero whero", "Kōwhai",
                 "Koura", "karekau", "Kōwhai")
q6 = QuizQuestions(6, "What colour is 'Karekau' ?", "Silver", "Black",
                 "Turquoise", "Crimson", "Turquoise")
q7 = QuizQuestions(7, "What is 'lime' in Maori ?", "Pokarekare", "Ma",
                 "Kotakota", "kākāriki", "Kotakota")
q8 = QuizQuestions(8, "What colour is 'pango' ?", "Black", "Red", "White",
                 "Yellow", "Black")
q9 = QuizQuestions(9, "What is 'White' in Maori ?", "Kōwhai", "Ma", "Rohi",
                 "Whero", "Ma")
q10 = QuizQuestions(10, "What colour is 'parauri' ?", "Gold", "Purple", "Pink",
                  "Brown", "Brown")
