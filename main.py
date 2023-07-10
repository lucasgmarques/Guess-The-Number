import random

def guessNumber(low=1, high=10, random_numbers=[]):
    random_number = random.randint(low, high)
    user_guess = None

    while user_guess != random_number:
        user_guess = input(f'Escolha um número entre {low} e {high} (ou \'q\' para sair): ')

        if user_guess.lower() == 'q':
            print("Encerrando ...")
            return None

        user_guess = int(user_guess)


        if user_guess < low or user_guess > high:
            print(f'Você deve digitar um número entre {low} e {high}')
            continue

        if user_guess < random_number:
            print("Você chutou um número baixo. Tente de novo.")
        elif user_guess > random_number:
            print("Você chutou um número alto. Tente de novo.")
        else:
            print("Parabéns, você acertou o número.")

    random_numbers.append(random_number)
    return random_number

def main():
    random_numbers = []
    
    while True:
        result = guessNumber(random_numbers=random_numbers)

        if result is None:
            print(f'Lista de números gerados: {random_numbers}')
            break
    

if __name__ == '__main__':
    main()

