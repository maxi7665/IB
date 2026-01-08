def create_alphabet():
    # Создаем алфавит без 'й' и 'ё'
    full_alphabet = "абвгдежзиклмнопрстуфхцчшщьыъэюя"
    return full_alphabet.replace('й', '').replace('ё', '')

def vigenere_process(text, key, decrypt=False):
    alphabet = create_alphabet()
    n = len(alphabet)
    text = text.lower().replace('й', 'и').replace('ё', 'е')
    key = key.lower().replace('й', 'и').replace('ё', 'е')
    
    res_text = ""
    full_key = ""
    
    key_indices = [alphabet.index(k) for k in key if k in alphabet]
    k_len = len(key_indices)
    ki = 0
    
    for char in text:
        if char in alphabet:
            t_idx = alphabet.index(char)
            k_idx = key_indices[ki % k_len]
            
            # Сопоставление: строка (ключ), столбец (текст)
            if decrypt:
                new_idx = (t_idx + k_idx) % n
            else:
                new_idx = (t_idx - k_idx) % n
            
            res_text += alphabet[new_idx]
            full_key += alphabet[k_idx]
            ki += 1
        else:
            res_text += char
            full_key += " "

    return res_text, full_key

# Исходные данные
# source_text = "КРИПТОАНАЛИЗЧТЕНИЕБЕЗКЛЮЧА"
# keyword = "ЭВРИКА"

source_text = "ТИГРЗВЕРЬВЕСЬМАЧИСТОПЛОТНЫЙ"
keyword = "КОШКА"

# source_text = "эззаменациолнылбинет"
# #source_text = "экзаменационныйбилет"
# keyword = "ВОПРОС"

# Шифрование
encrypted_text, looped_key = vigenere_process(source_text, keyword)

# Вывод таблицы
print(f"{'Исходный текст:':<20} {source_text}")
print(f"{'Ключевое слово:':<20} {looped_key}")
print(f"{'Шифр:':<20} {encrypted_text}")

# Пример расшифровки для проверки
decrypted_text, _ = vigenere_process(encrypted_text, keyword, decrypt=True)
print(f"{'Расшифровка:':<20} {decrypted_text}")

# encrypted_text = "ЫЪЩСЮХЛУЗЩАЪЛОЬТЫЬГД"
# keyword = "ВОПРОС"

# decrypted_text, key = vigenere_process(encrypted_text, keyword, decrypt=True)
# print(f"{'Ключевое слово:':<20} {key}")
# print(f"{'Шифр:':<20} {encrypted_text}")

# print(f"{'Расшифровка:':<20} {decrypted_text}")
