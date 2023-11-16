import random

# Напишите функцию draw_board(board), которая рисует доску размером 3х3. Функция принимает на вход двумерный список и выдает игровое поле.
def draw_board(board):
	# запустить цикл, который проходит по всем 3 строкам доски
	for i in board:
		print(*i, sep=' | ')
		print('---------')


# Функция принимает на вход двумерный список `**board`** и игрока (Х или 0)
# и просит игрока ввести координаты того места, где он хочет разместить свой символ на доске.
# Если место уже занято, функция предлагает игроку повторить попытку.

def ask_move(player, board):
	value = list(map(int, input(f'\t{player}, Куда будем ходить? Введите координаты (x, y) ').split()))
	# не делала обработку подачи строки на вход, по умолчанию подаются цифры / не доделана обработка ошибок

	if len(value) != 2 or (value[0] and value[1]) not in [0, 1, 2]:
		print(f'{player}! Таких координат нет!')
		ask_move(player, board)
	if board[value[0]][value[1]] == 'X' or board[value[0]][value[1]] == 'O':
		print(f'{player}! Сюда уже походили!')
		ask_move(player, board)
	else:
		print(f'вы ввели координаты хода: x = {value[0]}, y = {value[1]}\n')

	return value

def check_win(board):
	win = [['X', 'X', 'X'], ['O', 'O', 'O']]
	win_X = 'X'
	win_O = 'O'
	for i in range(len(board)):
		# проверка строк
		if board[i] in win:
			return True
		# проверка столбцов
		if (board[0][i] == win_X and board[1][i] == win_X and board[2][i] == win_X) or (board[0][i] == win_O and board[1][i] == win_O and board[2][i] == win_O):
			return True
	# проверка диагонали
	if board[0][0] == board[1][1] == board[2][2] == win_X or board[0][0] == board[1][1] == board[2][2] == win_O:
		return True
	if board[0][2] == board[1][1] == board[2][0] == win_X or board[0][2] == board[1][1] == board[2][0] == win_O:
		return True

	return False


def ask_and_make_move(player, board):
	value = ask_move(player, board)

	if player == 'player_1':
		board[value[0]][value[1]] = 'X'
		if check_win(board):
			return True

		player = 'player_2'

	elif player == 'player_2':
		board[value[0]][value[1]] = 'O'
		if check_win(board):
			return True

		player = 'player_1'

	draw_board(board)
	a = ask_and_make_move(player, board)
	if a:
		print(f'{player} выиграл, поздравляем!')
		draw_board(board)




def tic_tac_toe():
	board = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
	player = ['player_1', 'player_2']

	rand = random.choice(player)
	ask_and_make_move(rand, board)



tic_tac_toe()
