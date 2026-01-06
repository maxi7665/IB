import numpy as np

def matrix_str(matrix: list, is_formatted=True):
    text=""
    row=0
    col=0
    while True:
        
        if col >= len(matrix):
            col=0
            row+=1
            if is_formatted:
                text += "\r\n"

        column = matrix[col]

        if row >= len(column):
            if col == 0:
                break
            #c = "-"
        else:
            c = column[row]
    
        text+=c
        if is_formatted:
            text += " "      
        col+=1
    return text

def keyword_encode(text: str, keyword: str, rows_num: int):
    """Закодировать текст перестановкой по ключевому слову"""
    columns = []

    text=text.replace(" ", "-")
    print(len(text))

    row = 0

    max_row = -1

    # заполнение столбцов таблицы
    for c in text:
        if row >= rows_num:
            row = 0
        if row == 0:
            col = []
            columns.append(col)
        col.append(c)
        row+=1
        max_row = max(max_row, row)

    while (len(col) < max_row + 1):
        col.append("-")

    letters = list(keyword)
    full_keyword = ""

    for i in range(len(columns)):
        if len(letters) == 0:
            letters = list(keyword)
        full_keyword += letters.pop(0)

    sorted_full_keyword = sorted(full_keyword)
    letters_counts = dict()

    for order, c in enumerate(sorted_full_keyword, 1):
        if c not in letters_counts:
            letters_counts[c] = []
        letters_counts[c].append(order)
    
    column_orders = []

    for c in reversed(full_keyword):
        letter_count = letters_counts[c].pop()
        column_orders.insert(0, letter_count)      

    # выводим таблицу до перестановки
    print(" ".join(full_keyword))
    print(" ".join([str(c) for c in column_orders]))
    print(matrix_str(columns))

    sorted_column_orders = sorted(column_orders)

    sorted_columns = []

    for i in sorted_column_orders:
        old_index = column_orders.index(i)
        column = columns[old_index]
        sorted_columns.append(column)

    # выводим таблицу после перестановки
    print(" ".join(sorted_full_keyword))
    print(" ".join([str(c) for c in sorted_column_orders]))
    print(matrix_str(sorted_columns))

    encoded = matrix_str(sorted_columns, False)

    return encoded

def keyword_decode(text: str, keyword: str, rows_num: int):
    """Закодировать текст перестановкой по ключевому слову"""
    sorted_rows = []
    col = 0
    max_row = -1

    chars_in_row = len(text) // rows_num

    # заполнение столбцов таблицы
    for c in text:
        if col >= chars_in_row:
            col = 0
        if col == 0:
            row_ = []
            sorted_rows.append(row_)
        row_.append(c)
        col+=1

    sorted_columns = []

    # из построчного представления делаем поколоночное
    for r, row in enumerate(sorted_rows):
        for c, char in enumerate(row):
            if len(sorted_columns) < (c + 1):
                sorted_columns.append([])
            sorted_columns[c].append(char)

    letters = list(keyword)
    full_keyword = ""

    for i in range(len(sorted_columns)):
        if len(letters) == 0:
            letters = list(keyword)
        full_keyword += letters.pop(0)

    sorted_full_keyword = sorted(full_keyword)
    letters_counts = dict()

    for order, c in enumerate(sorted_full_keyword, 1):
        if c not in letters_counts:
            letters_counts[c] = []
        letters_counts[c].append(order)
    
    column_orders = []

    for c in reversed(full_keyword):
        letter_count = letters_counts[c].pop()
        column_orders.insert(0, letter_count)      

    sorted_column_orders = sorted(column_orders)

    columns = []

    for i in column_orders:
        old_index = sorted_column_orders.index(i)
        column = sorted_columns[old_index]
        columns.append(column)

    # выводим таблицу после перестановки
    print(" ".join(sorted_full_keyword))
    print(" ".join([str(c) for c in sorted_column_orders]))
    print(matrix_str(sorted_columns))

    # выводим таблицу после перестановки
    print(" ".join(full_keyword))
    print(" ".join([str(c) for c in column_orders]))
    print(matrix_str(columns))

    text = ""
    for c in columns:
        col_str = "".join(c)
        text+=col_str

    encoded = text

    return encoded






# key = "АРБУЗ"
# rows_num = 7
# text = "КРИПТОАНАЛИЗ ЧТЕНИЕ БЕЗ КЛЮЧА"

# key = "КРИСТАЛЛ"
# rows_num = 6
# text = "СИММЕТРИЧНЫЕ СИСТЕМЫ ДЕЛЯТСЯ НА БЛОЧНЫЕ И ПОТОЧНЫЕ"

# key = "ЕВРОПА"
# rows_num = 5
# text = "СИММЕТРИЧНЫЕ СИСТЕМЫ ДЕЛЯТСЯ НА БЛОЧНЫЕ И ПОТОЧНЫЕ"

# encoded = keyword_encode(text, key, rows_num)
# print(encoded)
# decoded = keyword_decode(encoded, key, rows_num)
# print(decoded)

key = "АЛМАЗ"
rows_num = 6
encoded = "ЯБЖБОВЫЕИВАТТЛЬСЬ.ЛЕЛМ.ЮЩЮО.БЕ"

decoded = keyword_decode(encoded, key, rows_num)
print(decoded)

