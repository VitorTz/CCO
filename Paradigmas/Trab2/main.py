
with open("/run/media/HD/Documentos/Github/Faculdade/Fase5/Paradigmas/Trabalho2/Solucao/input.txt", "r") as file:
    f = [x.replace("\n", "") for x in file.readlines()]
    board = [int(x) for x in f[0]]
    ordem = int(f[1])
    regioes = [[int(x) for x in r.split(',')] for r in f[2:]]

Board = list[int]
Regiao = list[int]
Regioes = list[Regiao]


def get_regiao(posicao: int) -> Regiao | None:
    global regioes
    for r in regioes:
        if posicao in r:
            return r


def regra_1(num: int, regiao: Regiao) -> bool:
    global board
    return num not in [board[i] for i in regiao]


def regra_2(num: int, posicao: int) -> bool:
    """Numbers in ortogonal adjacents must be different"""
    global ordem, board
    top = posicao - ordem
    bottom = posicao + ordem
    if (posicao - 1) % ordem == 0:
        left = -1
    else:
        left = posicao - 1
    if (posicao + 1) % ordem == 0:
        right = -1
    else:
        right = posicao + 1

    for pos in (left, right, top, bottom):
        if 0 <= pos < ordem*ordem and board[pos] == num:
            return False

    return True


def regra_3(num: int, posicao: int, regiao: Regiao) -> bool:
    global board, ordem

    top = posicao - ordem
    bottom = posicao + ordem
    c_top = c_bottom = True
    if top in regiao:
        c_top = board[top] > num
    if bottom in regiao:
        c_bottom = num > board[bottom]

    return c_top and c_bottom


def is_valid(num: int, posicao: int, regiao: Regiao) -> bool:
    return (
            regra_1(num, regiao) and
            regra_2(num, posicao) and
            regra_3(num, posicao, regiao)
    )


def find_next_empty() -> int:
    global board
    for i, n in enumerate(board):
        if n == 0:
            return i


def solve_sudoku():
    global board

    posicao = find_next_empty()

    if posicao is None:
        return True

    regiao = get_regiao(posicao)

    for num in range(1, len(regiao) + 1):

        if is_valid(num, posicao, regiao):

            board[posicao] = num

            if solve_sudoku():
                return True
        board[posicao] = 0
    return False


def print_board():
    global board

    for i, n in enumerate(board):
        if i % 10 == 0:
            print()
        print(n, end="")


solve_sudoku()
print_board()

