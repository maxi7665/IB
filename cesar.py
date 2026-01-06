
alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def encode(text: str, offset):
    """Шифр Цезаря"""
    text = text.upper()
    encoded=""
    for c in text:
        position = alphabet.find(c)

        if position >= 0:
            new_pos = (position + offset) % len(alphabet)
            new_c = alphabet[new_pos]
            encoded += new_c
        else:
            encoded += c
    return encoded

offset = 3

print(f"Алфавит: {alphabet}")

encoded_alphabet = encode(alphabet, offset)
print(f"Закодированный алфавит: {" ".join(encoded_alphabet)}")

# source = "ВСТРЕЧАЕМСЯ В ПАРКЕ ПАРОЛЬ И ОТЗЫВ ТЕ ЖЕ"
# encoded = encode(source, offset)
# print(" ".join(encoded.replace(" ", "")))
# decoded = encode(encoded, -offset)
# print(" ".join(decoded.replace(" ", "")))

source = "ТУМЫИОЦЕМЗИОТСДИЗМО"
offset = 3

decoded = encode(source, -offset)
print(" ".join(source))
print(" ".join(decoded))