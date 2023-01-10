import os

def decrypt_file(file_path):
    # pobieranie wartości przesunięcia szyfrującego z nazwy pliku
    shift = int(file_path.split("_")[-1].split(".")[0])
    # otwarcie pliku zaszyfrowanego
    with open(file_path, "r") as f:
        encrypted_text = f.read()
    # deszyfrowanie tekstu
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            char_code = ord(char)
            char_code -= shift
            if char.isupper():
                if char_code < ord('A'):
                    char_code += 26
                decrypted_text += chr(char_code)
            elif char.islower():
                if char_code < ord('a'):
                    char_code += 26
                decrypted_text += chr(char_code)
        else:
            decrypted_text += char
    # zapisanie deszyfrowanego tekstu do pliku
    new_file_path = file_path.replace("zaszyfrowany", "deszyfrowany")
    with open(new_file_path, "w") as f:
        f.write(decrypted_text)

def decrypt_directory(dir_path):
    for file_name in os.listdir(dir_path):
        # sprawdzenie, czy plik jest zaszyfrowany
        if file_name.startswith("plik_zaszyfrowany") and file_name.endswith(".txt"):
            file_path = os.path.join(dir_path, file_name)
            decrypt_file(file_path)

def main():
    # pobranie ścieżki katalogu od użytkownika
    dir_path = input("Podaj ścieżkę katalogu: ")
    # deszyfrowanie plików w katalogu
    try:
        decrypt_directory(dir_path)
    except Exception as e:
        print("Wystąpił błąd podczas deszyfrowania plików:", e)

if __name__ == "__main__":
    main()