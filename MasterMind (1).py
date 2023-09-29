import random

def generate_secret_code():
    """Generate a random 4-digit secret code."""
    digits = [str(i) for i in range(10)]
    random.shuffle(digits)
    return ''.join(digits[:4])
def evaluate_guess(secret_code, guess):
    """Evaluate a guess and return feedback."""
    feedback = []
    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            feedback.append('X')
        elif guess[i] in secret_code:
            feedback.append('O')
    return ''.join(feedback)

def play_mastermind():
    secret_code = generate_secret_code()
    attempts = 10

    print("Welcome to Mastermind! Try to guess the 4-digit secret code.")
    print("You have 10 attempts. Use 'X' for correct digit and position, 'O' for correct digit but wrong position.")
    
    for _ in range(attempts):
        guess = input("Enter your guess: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a 4-digit number.")
            continue
        
        feedback = evaluate_guess(secret_code, guess)
        print("Feedback:", feedback)
        
        if feedback == 'XXXX':
            print("Congratulations! You've guessed the secret code:", secret_code)
            break
    else:
        print("You've run out of attempts. The secret code was:", secret_code)

if __name__ == "__main__":
    play_mastermind()