import random
from words import words

def hangman():

    print("WELCOME TO HANGMAN GAME!")
    while True:
        try:
            players = int(input("How many players are going to play? (1-2)\n"))
            if players not in range(1, 3):
                print("Number must be 1 or 2!")
                continue
            break

        except:
            print("Incorrect input!")
            continue

    word = random.choice(words)

    while "-" in word or " " in word:
        word = random.choice(words)

    word_letter = [x for x in word]

    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                   "u", "v", "w", "x", "y", "z"]

    if players == 1:
        hang_m = ["_ " for i in range(len(word))]
        name = input("Provide name for Player:\t")
        score = 0

        while True:
            if len(word_letter) == 0:
                print(f"YOU WON {name}!")
                print(f"The word was {word}")
                print(f"Final Score {round(score, 2)}")
                break

            print("".join(hang_m))
            print("\n")
            print(letters)
            guess = input("\nGuess letter:\n")

            if guess not in letters:
                print("Guess is not in possible letters!")
                continue

            if guess in word:
                print("Correct guess!")
                if word.count(guess) == 1:
                    n = word.index(guess)
                    hang_m[n] = guess + " "
                    word_letter.remove(guess)
                    letters.remove(guess)
                    score += 1
                else:
                    indices = [i for i, letter in enumerate(word) if letter == guess]
                    for i in indices:
                        hang_m[i] = guess + " "
                        word_letter.remove(guess)
                        score += 1
                    letters.remove(guess)

            else:
                print("Try again!")
                letters.remove(guess)
                score -= 0.5

    elif players == 2:
        hang_m = ["_ " for i in range(len(word))]
        name1 = input("Provide name for Player #1:\t")
        name2 = input("Provide name for Player #2:\t")
        score1 = 0
        score2 = 0

        while True:
            if len(word_letter) == 0:
                if score1 > score2:
                    print(f"{name1} WON with {round(score1-score2, 2)} points!")
                    print(f"The word was {word}")
                    print(f"Final Scores:\n{name1} - {round(score1, 2)}\n{name2} - {round(score2, 2)}")
                    break
                elif score1 < score2:
                    print(f"{name2} WON with {round(score2-score1, 2)} points!")
                    print(f"The word was {word}")
                    print(f"Final Scores:\n{name1} - {round(score1, 2)}\n{name2} - {round(score2, 2)}")
                    break
                else:
                    print("It was a TIE!")
                    print(f"The word was {word}")
                    print(f"Final Scores:\n{name1} - {round (score1, 2)}\n{name2} - {round (score2, 2)}")
                    break

            while True:
                print("".join(hang_m))
                print("\n")
                print(letters)
                guess1 = input(f"\nGuess letter {name1}:\n")
                if guess1 not in letters:
                    print("Guess is not in possible letters!")
                    continue

                if guess1 in word:
                    print("Correct guess!")
                    if word.count(guess1) == 1:
                        n = word.index(guess1)
                        hang_m[n] = guess1 + " "
                        word_letter.remove(guess1)
                        letters.remove(guess1)
                        score1 += 1
                        break

                    else:
                        indices = [i for i, letter in enumerate(word) if letter == guess1]
                        for i in indices:
                            hang_m[i] = guess1 + " "
                            word_letter.remove(guess1)
                            score1 += 1
                        letters.remove(guess1)
                        break

                else:
                    print("Incorrect!")
                    print(f"{name2}'s Turn!")
                    letters.remove(guess1)
                    score1 -= 0.5
                    break

            if len(word_letter) == 0:
                print(f"{name1} guessed FINAL letter, +3 points for it!")
                score1 += 3
                continue

            while True:
                print("".join(hang_m))
                print("\n")
                print(letters)

                guess2 = input(f"\nGuess letter {name2}:\n")
                if guess2 not in letters:
                    print("Guess is not in possible letters!")
                    continue

                if guess2 in word:
                    print("Correct guess!")
                    if word.count(guess2) == 1:
                        n = word.index(guess2)
                        hang_m[n] = guess2 + " "
                        word_letter.remove(guess2)
                        letters.remove(guess2)
                        score2 += 1
                        break
                    else:
                        indices = [i for i, letter in enumerate(word) if letter == guess2]
                        for i in indices:
                            hang_m[i] = guess2 + " "
                            word_letter.remove(guess2)
                            score2 += 1
                        letters.remove(guess2)
                        break

                else:
                    print("Incorrect!")
                    print(f"{name1}'s Turn!")
                    letters.remove(guess2)
                    score2 -= 0.5
                    break

            if len(word_letter) == 0:
                print(f"{name2} guessed FINAL letter, +3 points for it!")
                score2 += 3
                continue

hangman()