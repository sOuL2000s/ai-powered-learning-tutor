import random
import pandas as pd

# Sample questions with difficulty levels
questions = [
    {"question": "What is 5 + 7?", "answer": 12, "difficulty": "easy"},
    {"question": "What is the square root of 16?", "answer": 4, "difficulty": "easy"},
    {"question": "What is 15 * 15?", "answer": 225, "difficulty": "medium"},
    {"question": "Solve for x: 2x + 5 = 17", "answer": 6, "difficulty": "medium"},
    {"question": "What is the derivative of x^2?", "answer": "2x", "difficulty": "hard"},
    {"question": "Integrate 1/x dx", "answer": "ln(x)", "difficulty": "hard"}
]

# Track performance
performance = pd.DataFrame(columns=["Question", "Difficulty", "Correct"])

def get_question(difficulty_level):
    # Filter questions by difficulty
    level_questions = [q for q in questions if q["difficulty"] == difficulty_level]
    return random.choice(level_questions)

def ask_question(question):
    print("\nQuestion:", question["question"])
    user_answer = input("Your answer: ")
    return user_answer == str(question["answer"])

def adjust_difficulty(correct_answers):
    if correct_answers >= 3:
        return "medium"
    elif correct_answers >= 5:
        return "hard"
    return "easy"

# Quiz loop
difficulty_level = "easy"
correct_answers = 0

for i in range(5):  # Ask 5 questions
    question = get_question(difficulty_level)
    is_correct = ask_question(question)
    performance = performance.append({"Question": question["question"], "Difficulty": difficulty_level, "Correct": is_correct}, ignore_index=True)
    
    if is_correct:
        correct_answers += 1
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question["answer"])

    difficulty_level = adjust_difficulty(correct_answers)

# Display performance summary
print("\nQuiz Summary:")
print(performance.to_string(index=False))
