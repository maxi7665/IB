def sparta_encode(text: str, offset: int):
    """Шифр Спартанцев"""
    matrix = []
    row = 0
    column = 0
    for c in text:
        if row >= (offset + 1):
            row = 0
            column += 1
        if column == 0:
            matrix.append([])
        matrix[row].append(c)
        row += 1
    return matrix

def matrix_to_text(matrix: list, is_to_encoded=True):
    """Матрицу преобразовать в текст"""
    text=""
    if is_to_encoded:
        for row in matrix:
            for c in row:
                text+=c
    else:
        col = 0
        while True:
            for row in matrix:
                if len(row) < (col + 1):
                    break
                text+=row[col]    
            if len(row) < (col + 1):
                break
            col += 1       
    return text

def matrix_str(matrix: list):
    text=""
    for row in matrix:
        for c in row:
            text+=c + " "
        text += "\r\n"
    return text
        

def sparta_decode(enc_text: str, offset):
    """Раскодировать текст в матрицу"""
    # остаток от деления - сколько будет заполненных строк в последнем столбце
    mod = len(enc_text) % (offset + 1)
    # кол-во полностью заполненных колонок
    filled_cols = len(enc_text) // (offset + 1)
    # индекс последней колонки
    last_column = filled_cols if mod > 0 else filled_cols - 1
    # индекс последней заполненной строки в последней колонке
    last_filled_row = mod - 1
    row = 0
    column = 0
    matrix=[]
    for c in enc_text:
        if column > last_column:
            column = 0
            row += 1
        if column == last_column and row > last_filled_row:
            column = 0
            row += 1
        if column == 0:
            matrix.append([])
        matrix[row].append(c)
        column += 1
    return matrix


text = "КРИПТОГРАММЫ ДРЕВНИХ ВРЕМЕН".replace(" ", "")
text = "СИММЕТРИЧНЫЕ СИСТЕМЫ ДЕЛЯТСЯ НА БЛОЧНЫЕ И ПОТОЧНЫЕ".replace(" ", "")
offset = 6

print(len(text))

# encoded = sparta_encode(text, offset)
# print(matrix_str(encoded))
# text = matrix_to_text(encoded)
# print(text)

# decoded = sparta_decode(text, offset)
# print(matrix_str(decoded))
# decoded_text = matrix_to_text(decoded, False)
# print(decoded_text)

text = "Н_ЦТ_АОИОСЧПИГЕАЕ_ОМЛРП_ЬОАЯВ"
offset = 5

decoded = sparta_decode(text, offset)
print(matrix_str(decoded))
decoded_text = matrix_to_text(decoded, False)
print(decoded_text)


