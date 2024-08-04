def play_kbc_game():
  """Implements the KBC game logic."""

  question_bank = {
      "1. Which country is Delhi located in?": {
          "a": "India",
          "b": "America",
          "c": "Pakistan",
          "d": "Nepal",
          "correct_answer": "a"
      },
      "2. What is the capital of India?": {
          "a": "Bihar",
          "b": "Delhi",
          "c": "Himachal Pradesh",
          "d": "Uttar Pradesh",
          "correct_answer": "b"
      },
      # Add more questions and answers here ...
  }

  prize_money = [1000, 2000, 3000, 5000, 10000, 200000, 40000, 80000, 160000, 320000]
  current_level = 0
  correct_answers = 0
  completed_stages = 1

  while current_level < len(question_bank):
    question, options = next(iter(question_bank.items()))  # Get a random question

    print(question)
    for option_key, option_text in options.items():
      print(f"{option_key}. {option_text}")

    user_answer = input("Enter your answer (a-d): ").upper()
    if user_answer == question_bank[question]["correct_answer"]:  # Access correct answer using dictionary key
      correct_answers += 1
      print(f"Congratulations! Your answer is correct. You win Rs.{prize_money[current_level]}")
      current_level += 1
      if current_level % 5 == 0:
        print(f"Congratulations! You have completed stage {completed_stages}.")
        completed_stages += 1
    else:
      print(f"Sorry, your answer is incorrect. The correct answer is {question_bank[question]['correct_answer']}.")
      print(f"You won Rs.{prize_money[current_level - 1]}.")
      break

  print(f"Thank you for playing! You answered {correct_answers} questions correctly and won Rs.{prize_money[current_level - 1]}.")

if __name__ == "__main__":
  play_kbc_game()
