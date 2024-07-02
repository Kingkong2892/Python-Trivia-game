import random

# Trivia questions
questions = [
    {
        "question": "Who is the CEO of Apple?",
        "answers": ["Tim Cook", "Elon Musk", "Jeff Bezos", "Sundar Pichai"],
        "correct_answer": "Tim Cook"
    },
    {
        "question": "What is the capital of France?",
        "answers": ["London", "Paris", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "Which company developed the first personal computer?",
        "answers": ["Apple", "Microsoft", "IBM", "Intel"],
        "correct_answer": "IBM"
    },
    # Add more questions here
]

# Game loop
score = 0
for question in questions:
    print(question["question"])
    for i, answer in enumerate(question["answers"]):
        print(f"{i+1}. {answer}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.strip().lower() == question["correct_answer"].lower():
        score += 1
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The correct answer is: {question['correct_answer']}")

# Display final score
print(f"Final Score: {score}/{len(questions)}")