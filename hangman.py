from custom_words import shuffled_answers

title = 'Family Hang(man) Time!'
prompt = "Guess a letter: "

def mask_word(word: str, guessed_letters: set[str]) -> str:
    # Reveal non-letters (digits, spaces, punctuation) immediately;
    # only hide letters until guessed.
    out = []
    for ch in word:
        if ch.isalpha():
            out.append(ch if ch in guessed_letters else "_")
        else:
            out.append(ch)
    return "".join(ch if ch in guessed_letters else "_" for ch in word)

def answerer():
    answer = shuffled_answers.popitem()
    word = answer[0].upper()
    player = answer[1]['player']
    theme = answer[1]['theme']
    hint = answer[1]['hint']
    return word, player, theme, hint

def play(word, player, theme, hint):
    guessed = False
    guessed_letters = set()
    guessed_words = set()
    tries = 6

    word_completion = mask_word(word, guessed_letters)

    print(f"\n{title}")
    print(display_hangman(tries))
    print(word_completion)
    print('\n')
    print(player)

    while not guessed and tries > 0:
        guess = input(prompt).upper().strip()

        if guess == "?":
            tries -= 1
            print(hint)
        elif len(guess) == 1:
            # Allow ANY single character (letters, digits, punctuation, space),
            # except we already handled '?' above.
            if guess in guessed_letters:
                print(f"You already guessed '{guess}', dummy.")
            else:
                guessed_letters.add(guess)
                if guess in word:
                    print(f"You got lucky...'{guess}' is in the word")
                else:
                    print(f"No! '{guess}' is NOT in the word. "
                          f"Type '?' if you need a hint, but it will cost a limb.")
                    tries -= 1
        elif len(guess) == len(word):
            if guess in guessed_words:
                print(f"You already guessed '{guess}', dummy.")
            else:
                guessed_words.add(guess)
                if guess == word:
                    guessed = True
                    word_completion = word
                else:
                    print(f"Ha! Nice try, '{guess}' is not the word. "
                          "Maybe stick with letters, it's easier.")
                    tries -= 1
        else:
            print("\nNot a valid guess. That is so obviously not a valid guess. "
                  "Please, this is serious.")

        # Recompute the masked display after each turn
        if not guessed:
            word_completion = mask_word(word, guessed_letters)

        print(display_hangman(tries))
        print(word_completion)
        print('\n')

        # If all letters are revealed (no underscores left), you win
        if "_" not in word_completion:
            guessed = True

    if guessed:
        print(f"{player}, you're a winner! The theme is {theme}.")
    else:
        print(f"No surprise {player} ran out of tries. The answer is {word}, and the theme is {theme}.")



def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |     \\O/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |     \\O
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |       \\
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |
                   |
                   |
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |
                   |
                   |
                   |
                   -
                """
    ]
    tries = max(0, min(tries, 6))
    return stages[tries]

def main():
    # try:
        answer, player, theme, hint = answerer()
        play(answer, player, theme, hint)
        while input("Play Again? (Y/N) ").upper() == "Y":
            answer, player, theme, hint = answerer()
            play(answer, player, theme, hint)
    # except:
    #     print("\n\nOh no, there are no more words!\n\n")

if __name__ == "__main__":
    main()
