import random

def get_valid_guess(low, high):
    """
    Validates and retrieves a user's guess within the specified range.

    Args:
        low (int): The lower bound of the valid range.
        high (int): The upper bound of the valid range.

    Returns:
        int or None: The user's valid guess within the range, or None if the user wants to quit.

    """
    while True:
        user_guess = input(f'Escolha um número entre {low} e {high}) (ou digite "q" para sair): ')

        if user_guess.lower() == 'q':
            print("Encerrando ...")
            return None
        try:
            user_guess = int(user_guess)
            if low <= user_guess <= high:
                return user_guess
            print(f'Você deve digitar um número entre {low} e {high}.')

        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def guess_number(low=1, high=100, random_numbers=[], max_attempts=10):
    """
    Plays a number guessing game where the user tries to guess a randomly generated number.

    Args:
        low (int, optional): The lower bound of the random number range. Defaults to 1.
        high (int, optional): The upper bound of the random number range. Defaults to 10.
        random_numbers (list, optional): A list to track the generated random numbers. Defaults to an empty list.

    Returns:
        int or None: The randomly generated number that the user successfully guessed, or None if the game was interrupted.

    """
    random_number = random.randint(low, high)
    attempts = 0

    print("Nível de Dificuldade:")
    print("(1) - Fácil")
    print("(2) - Médio")
    print("(3) - Difícil")

    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        max_attempts = 20
    elif nivel == 2:
        max_attempts = 10
    else:
        max_attempts = 5

    while attempts < max_attempts:
        user_guess = get_valid_guess(low, high)
        
        if user_guess is None:
            return None

        attempts += 1

        if user_guess < random_number:
            print("Você chutou um número baixo. Tente de novo.")
        elif user_guess > random_number:
            print("Você chutou um número alto. Tente de novo.")
        else:
            print("Parabéns, você acertou o número.")
            break

    if attempts == max_attempts:
        print(f'Limite de tentativas atingido. O número secreto era {random_number}. ')

    random_numbers.append(random_number)
    return random_number

def main():
    """
    Entry point of the program. Plays the number guessing game.

    """
    random_numbers = []

    while True:
        result = guess_number(random_numbers=random_numbers)

        if result is None:
            print(f'Lista de números gerados: {random_numbers}')
            break
    
if __name__ == '__main__':
    main()

