def welcome_message():
    print("SELAMAT DATANG DI GAME TEBAK KATA!")
    print("Pemain 1 akan memasukkan kata tersembunyi \nPemain 2 harus menebak kata dengan menebak huruf - hurufnya terlebih dahulu")
    print("Pemain 2 juga bisa langsung menebak kata jika sudah tahu kata tersebut.")

def hide_word(word):
    return ['_' for _ in word]

def display_word(hidden_word):
    print(' '.join(hidden_word))

def play_game():
    welcome_message()

    word = input("Pemain 1, silakan masukkan sebuah kata: ").lower()
    hidden_word = hide_word(word)

    print('\n' * 50)
    print(f"Kata tersembunyi memiliki {len(word)} huruf.")
    display_word(hidden_word)

    attempts = 3
    guessed_letters = []

    while attempts > 0:
        print(f"\nKamu punya {attempts} kesempatan tersisa.")
        guess = input("Pemain 2, silakan masukkan huruf atau tebak kata lengkap: ").lower()

        if len(guess) > 1:
            if guess == word:
                print(f"Selamat! Pemain 2 berhasil menebak kata yang benar: '{word}'")
                break
            else:
                print(f"Tebakan kata '{guess}' salah.")
                attempts -= 1
        else:
            if len(guess) != 1 or not guess.isalpha():
                print("Tebakan harus satu huruf. Silakan coba lagi.")
                continue

            if guess in guessed_letters:
                print(f"Anda sudah menebak huruf '{guess}'. Silakan tebak huruf lain.")
                continue

            guessed_letters.append(guess)

            if guess in word:
                print(f"Huruf '{guess}' ada di dalam kata tersembunyi! Silakan lanjut menebak.")
                for i, letter in enumerate(word):
                    if letter == guess:
                        hidden_word[i] = guess
            else:
                print(f"Huruf '{guess}' tidak ada di dalam kata tersembunyi.")
                attempts -= 1

        display_word(hidden_word)

        if '_' not in hidden_word:
            print(f"Selamat! Pemain 2 berhasil menebak kata tersembunyi: '{word}'")
            break

    if attempts == 0:
        print(f"Kesempatan habis! Kata tersembunyi adalah '{word}'.")

play_game()
