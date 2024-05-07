
with open("/run/media/HD/Documentos/Github/KojunSolver/puzzles/n-11.txt", "r") as file:
    f = [x.replace("\n", "") for x in file.readlines()]
    board = [int(x) for x in f[0]]
    ordem = int(f[1])
    regioes = [[int(x) for x in r.split(',')] for r in f[2:]]

Board = list[int]
Regiao = list[int]
Regioes = list[Regiao]



def find_empty(regiao: Regiao) -> int:
    global board
    for i in regiao:
        if board[i] == 0:
            return i

def regra_2(num: int, posicao_celula: int) -> bool:
    global board, ordem
    top = posicao_celula - ordem
    bottom = posicao_celula + ordem

    if (posicao_celula - 1) % ordem == ordem - 1:
        left = -1
    else:
        left = posicao_celula - 1
    if (posicao_celula + 1) % ordem == 0:
        right = - 1
    else:
        right = posicao_celula + 1
    for pos in (left, right, top, bottom):
        if 0 <= pos < ordem*ordem and board[pos] == num:
            return False
    return True

def regra_3(num: int, posicao_celula: int, regiao: Regiao) -> bool:
    global board, ordem
    top = posicao_celula - ordem
    bottom = posicao_celula + ordem
    c_top = c_bottom = True
    if top in regiao:
        c_top = board[top] > num
    if bottom in regiao:
        c_bottom = num > board[bottom]
    return c_top and c_bottom


def is_valid(num: int, posicao_celula: int, regiao: Regiao) -> bool:
    return (
        regra_2(num, posicao_celula) and 
        regra_3(num, posicao_celula, regiao)
    )


def solve_regiao(regiao: Regiao, length_regiao: int) -> None:
    global board

    posicao_celula = find_empty(regiao)
    if posicao_celula is None:
        return True
    
    regiao_nums = [board[i] for i in regiao]

    for num in range(1, length_regiao + 1):
        
        if num not in regiao_nums and is_valid(num, posicao_celula, regiao):
            board[posicao_celula] = num        

            if solve_regiao(regiao, length_regiao):
                return True
        
        board[posicao_celula] = 0


def solve_kojun() -> None:
    global regioes
    for i in range(len(regioes)):
        r = regioes[i]
        solve_regiao(r, len(r))


def print_board() -> None:
    global board
    for index, n in enumerate(board):
        if index % 10 == 0:
            print()
        print(n, end=", ")
        

solve_kojun()
print_board()
