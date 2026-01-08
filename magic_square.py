import math
import random
from string import ascii_uppercase

def process_text(text, square_size):
    """Дополняет текст пробелами (до 3-х) под размер квадрата."""
    capacity = square_size ** 2
    if len(text) < capacity:
        diff = capacity - len(text)
        text += " " * min(diff, 3)
        if diff > 3:
            text += "".join(random.choices(ascii_uppercase)[:3])
    return text

def print_matrix(matrix, title):
    print(f"\n--- {title} ---")
    for row in matrix:
        print(" | ".join(f"{str(cell):^3}" for cell in row))

def encrypt(text, magic_square):
    n = len(magic_square)
    capacity = n * n
    chunks = [text[i:i + capacity] for i in range(0, len(text), capacity)]
    full_result = ""

    for chunk in chunks:
        # Создаем пустую сетку
        grid = [['' for _ in range(n)] for _ in range(n)]
        
        # 1. Расставляем символы согласно числам в магическом квадрате
        for char_idx, char in enumerate(chunk):
            target_num = char_idx + 1
            for r in range(n):
                for c in range(n):
                    if magic_square[r][c] == target_num:
                        grid[r][c] = char

        print_matrix(grid, "Матрица с вставленными символами (Шифрование)")
        
        # 2. Читаем построчно
        for row in grid:
            full_result += "".join(row)
            
    return full_result

def decrypt(cipher_text, magic_square):
    n = len(magic_square)
    capacity = n * n
    chunks = [cipher_text[i:i + capacity] for i in range(0, len(cipher_text), capacity)]
    full_result = ""

    for chunk in chunks:
        # 1. Заполняем сетку построчно зашифрованным текстом
        grid = []
        for i in range(0, len(chunk), n):
            grid.append(list(chunk[i:i+n]))
        
        print_matrix(grid, "Матрица дешифровки (заполнена построчно)")
        
        # 2. Извлекаем символы в порядке магических чисел
        temp_dict = {}
        for r in range(n):
            for c in range(n):
                val = magic_square[r][c]
                temp_dict[val] = grid[r][c]
        
        for i in range(1, len(chunk) + 1):
            if i in temp_dict:
                full_result += temp_dict[i]
                
    return full_result

# --- Пример использования ---
# Магический квадрат 3х3 (сумма 15)
# magic_sq = [
#     [8, 1, 6],
#     [3, 5, 7],
#     [4, 9, 2]
# ]
# source_text = "ПРИВЕ"

source_text = "ЛОГИЧЕСКИЙ*ТИП*ДАНЫХ*В*OBJECT*PASCAL"

# magic_sq = [
#     [32,30,18,4,16,11],
#     [15,28,14,12,8,34],
#     [13,7,19,29,17,26],
#     [23,1,5,20,	27,35],
#     [6,36,31,25,10,3],
#     [22,9,24,21,33,2]
# ]

magic_sq = [
    [16,	33,	5,	23,	8,	26],
[15,	34,	24,	6,	25,	7],
[20,	1,	27,	9,	36,	18],
[19,	2,	28,	10,	35,	17],
[30,	12,	13,	31,	3,	22],
[11,	29,	14,	32,	4,	21]

]




# print_matrix(magic_sq, "Магический квадрат")
# processed_source = process_text(source_text, 3)

# print(f"Исходный текст: '{source_text}'")
# print(f"Текст после обработки: '{processed_source}'")
# print(f"Длина текста: {len(processed_source)}")

# # Шифрование
# encrypted = encrypt(processed_source, magic_sq)
# print(f"\nЗашифрованный текст: '{encrypted}'")

# # Дешифрование
# decrypted = decrypt(encrypted, magic_sq)
# print(f"\nРасшифрованный текст: '{decrypted.strip()}'")

matrix_3 = [
    [7,	33,	3,	20,	31,	17],
[21,	14,	8,	1,	35,	32],
[30,	25,	34,	5,	2,	15],
[16,	23,	29,	27,	6,	10],
[24,	12,	9,	36,	11,	19],
[13,	4,	28,	22,	26,	18],

]

print_matrix(magic_sq, "Магический квадрат")

encrypted = "еиобтедвя-нзтпсомаелчтылсчттоеоаолхт"

# Дешифрование
decrypted = decrypt(encrypted, magic_sq)
print(f"\nРасшифрованный текст: '{decrypted.strip()}'")
