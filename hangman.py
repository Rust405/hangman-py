import os
import requests

base_url = 'https://random-word-api.herokuapp.com/'

def menu():
    os.system('cls')

    title = 'Hangman'

    print(title)
    print('-'*len(title))

    print()

    print('(s) Start')

    print('(x) Exit')

    choice = input('\nOption: ')

    match choice:
        case 's':
            start()
        case 'x':
            print()
            os.system('pause')
            os.system('cls')
            os.system('exit')
        case _:
            menu()


def start():
    os.system('cls')

    randomWord = getRandomWord()
    guessWord = '_' * len(randomWord)
    wrongAttemptCtr = 0
    wrongGuesses = []

    while guessWord != randomWord:
        os.system('cls')

        draw(wrongAttemptCtr, guessWord)

        guess = ''

        if len(wrongGuesses) > 0:
            print("\nWrong attempts: " + (', ').join(wrongGuesses) + ".")

        while (len(guess) == 0):
            guess = input('\nGuess letter or whole word (1 attempt only): ')

        if (len(guess) == 1):
            isCorrectGuess = guess in randomWord
            guessWord = insertLetters(randomWord, guessWord, guess)

            if not isCorrectGuess and guess not in wrongGuesses:
                wrongAttemptCtr += 1
                wrongGuesses.append(guess)
        else:
            isCorrectGuess = guess == randomWord
            guessWord = guess
            wrongAttemptCtr = 7  # immediate fail

        if wrongAttemptCtr == 7:
            break

    if wrongAttemptCtr < 7:
        os.system('cls')
        draw(wrongAttemptCtr, guessWord)
        print("\nCongratulations, the correct word is \"" + randomWord + "\".\n")
        os.system("pause")
        menu()
    else:
        os.system('cls')
        draw(wrongAttemptCtr, guessWord)
        print("\nYou lost, the correct word was \"" + randomWord + "\".\n")
        os.system("pause")
        menu()


def draw(wrongAttemptCtr, guessWord):
    drawMan(wrongAttemptCtr)
    drawLines(guessWord)


def insertLetters(randomWord, guessWord, guess):
    for index in range(len(randomWord)):
        if (randomWord[index] == guess):
            newWord = list(guessWord)
            newWord[index] = guess
            guessWord = "".join(newWord)

    return guessWord


def drawMan(wrongAttemptCtr):
    lines = 5

    print('-' * 5)

    if wrongAttemptCtr >= 1:
        print('  | ')
        lines -= 1

    if wrongAttemptCtr >= 2:
        print('  O ')
        lines -= 1

    if wrongAttemptCtr == 3:
        print(' /| ')
        lines -= 1

    if wrongAttemptCtr >= 4:
        print(' /|\\')
        lines -= 1

    if wrongAttemptCtr >= 5:
        print('  | ')
        lines -= 1

    if wrongAttemptCtr == 6:
        print(' / ')
        lines -= 1

    if wrongAttemptCtr >= 7:
        print(' / \\')
        lines -= 1

    print('\n' * lines)


def drawLines(guessWord):
    wordArr = list(guessWord)
    print(" ".join(str(word) for word in wordArr))


def getRandomWord():
    res = requests.get(base_url + 'word')
    return res.json()[0]


menu()
