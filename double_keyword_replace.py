import math

def get_cyclic_key(key, length):
    """Циклически повторяет или обрезает ключ до нужной длины."""
    return (key * (math.ceil(length / len(key))))[:length]

def get_permutation_order(current_key):
    """Возвращает индексы для перестановки на основе алфавитного порядка символов ключа."""
    # Сортируем индексы ключа по алфавиту символов
    indexed_key = sorted(list(enumerate(current_key)), key=lambda x: x[1])
    return [item[0] for item in indexed_key]

def print_table(matrix, title, key_str):
    """Выводит таблицу в консоль."""
    print(f"\n[ {title} ]")
    print(f"Ключевая последовательность: {'  '.join(key_str)}")
    print("-" * (len(key_str) * 5))
    for row in matrix:
        print("   ".join(row))

def encrypt(text: str, rows, cols, key):
    text = text.replace(" ", "").upper()
    total_cells = rows * cols
    text = text.ljust(total_cells, '-')[:total_cells]
    
    # 1. Заполнение матрицы ПО СТОЛБЦАМ
    matrix = [['' for _ in range(cols)] for _ in range(rows)]
    idx = 0
    for c in range(cols):
        for r in range(rows):
            matrix[r][c] = text[idx]
            idx += 1
    
    col_key = get_cyclic_key(key, cols)
    row_key = get_cyclic_key(key, rows)
    
    print_table(matrix, "ИСХОДНАЯ ТАБЛИЦА (ЗАПОЛНЕНА ПО СТОЛБЦАМ)", col_key)
    print(f"Ключ строки: {row_key}")

    # 2. Перестановка столбцов
    col_order = get_permutation_order(col_key)
    matrix_col_permuted = []
    for r in range(rows):
        new_row = [matrix[r][i] for i in col_order]
        matrix_col_permuted.append(new_row)
    
    sorted_col_key = [col_key[i] for i in col_order]
    print_table(matrix_col_permuted, "ПОСЛЕ ПЕРЕСТАНОВКИ СТОЛБЦОВ", sorted_col_key)

    # 3. Перестановка строк
    row_order = get_permutation_order(row_key)
    final_matrix = [matrix_col_permuted[i] for i in row_order]
    
    sorted_row_key = [row_key[i] for i in row_order]
    print_table(final_matrix, "ФИНАЛЬНАЯ ТАБЛИЦА (ПОСЛЕ ПЕРЕСТАНОВКИ СТРОК)", sorted_row_key)
    
    # Чтение результата ПОСТРОЧНО
    ciphertext = "".join(["".join(row) for row in final_matrix])
    return ciphertext

def decrypt(ciphertext, rows, cols, key):
    col_key = get_cyclic_key(key, cols)
    row_key = get_cyclic_key(key, rows)
    col_order = get_permutation_order(col_key)
    row_order = get_permutation_order(row_key)

    # 1. Заполняем матрицу из шифротекста ПОСТРОЧНО
    matrix = [list(ciphertext[i*cols : (i+1)*cols]) for i in range(rows)]
    
    # 2. Обратная перестановка строк
    rows_restored = [None] * rows
    for i, pos in enumerate(row_order):
        rows_restored[pos] = matrix[i]
        
    # 3. Обратная перестановка столбцов
    final_matrix = [['' for _ in range(cols)] for _ in range(rows)]
    for r in range(rows):
        for i, pos in enumerate(col_order):
            final_matrix[r][pos] = rows_restored[r][i]

    print_table(final_matrix, "ТАБЛИЦА ПОСЛЕ ОБРАТНЫХ ПЕРЕСТАНОВОК", col_key)
    print(f"Ключ строки: {row_key}")
    
    # 4. Чтение результата ПО СТОЛБЦАМ (как в оригинале)
    result = []
    for c in range(cols):
        for r in range(rows):
            result.append(final_matrix[r][c])
            
    return "".join(result)

def get_n_cols(text, n_rows):
    """Рассчитать кол-во колонок для размещения текста при заданном кол-ве строк"""
    size = len(text)
    n_cols = size // n_rows
    if (size % n_rows > 0):
        n_cols +=1
    return n_cols

# --- Настройки ---
# msg = "СЕКРЕТНЫЙ_КЛЮЧ–ЗАКРЫТЫЙ_КАНАЛ_СВЯЗИ"
# key_word = "ГАРАЖ"
# n_rows = 6
# n_cols = get_n_cols(msg, n_rows)

#msg = "РАСШИФРОВКА_ПРОЦЕСС_ОБРАТНОГО_ПРИМЕНЕНИЯ_ШИФРА"
msg = "пятигорскиигосударствен.лингвистическ.университет"
#key_word = "БРИГАНТИНА"
key_word = "ТРОТУАР"
n_rows = 7
n_cols = get_n_cols(msg, n_rows)

print(f"ИСХОДНОЕ СООБЩЕНИЕ: {msg}")
print(f"ПАРАМЕТРЫ: {n_rows} строк, {n_cols} столбцов, Ключ: {key_word}")

# Запуск
enc = encrypt(msg, n_rows, n_cols, key_word)
print(f"\nЗАШИФРОВАННЫЙ ТЕКСТ (построчно): {enc}")

# dec = decrypt(enc, n_rows, n_cols, key_word)
# print(f"\nРАСШИФРОВАННЫЙ ТЕКСТ (по столбцам): {dec}")


enc = "итоеонч.аист.скдкряниввстргесусепевурииилтнсгтгии"
key_word = "ТРОТУАР"
n_rows = 7
n_cols = 7

dec = decrypt(enc, n_rows, n_cols, key_word)
print(f"\nРАСШИФРОВАННЫЙ ТЕКСТ (по столбцам): {dec}")
