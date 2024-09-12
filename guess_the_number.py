import random

correct = 'you guessed correctly!'
too_low = 'too low'
too_high = 'too high'


def configure_range():
    """ Set the high and low values for the random number """
    return 1, 10


def generate_secret(low, high):
    """ Generate a secret number for the user to guess """
    return random.randint(low, high)


def get_guess():
    """ get user's guess, as an integer number """
    return int(input('Guess the secret number? '))


def check_guess(guess, secret):
    """ compare guess and secret, return string describing result of comparison """
    if guess == secret:
        return correct
    if guess < secret:
        return too_low
    if guess > secret:
        return too_high


def main():
    guess_count = 0
    (low, high) = configure_range()
    secret = generate_secret(low, high)

    while True:
        guess = get_guess()
        guess_count += 1
        result = check_guess(guess, secret)
        print(result)

        if result == correct:
            break

    print(f'It took you {guess_count} guesses.')
    print('Thanks for playing the game!')


if __name__ == '__main__':
    main()
