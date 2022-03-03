board = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
def draw_board(board):
    print(board['7'] + ' ' + '|' + board['8'] + ' ' + '|' + board['9'])
    print('--+--+--')
    print(board['4'] +' ' + '|' + board['5'] + ' ' + '|' + board['6'])
    print('--+--+--')
    print(board['1'] +' ' +'|' + board['2'] +' ' + '|' + board['3'])
is_win= True
available_number = "123456789"
selected_num = []
while is_win == True:
    for i in range (9):
        user_input= input("Do you want to be X or O: ").upper()
        place=input(f'Choose the position of {user_input} from {available_number}: ')
        available_number = available_number.replace(place,"")
        if place not in selected_num:
            selected_num.append(place)
            board[place] = user_input
            #print(board) 
            draw_board(board)
            if board['7'] ==  board['8'] == board['9'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['4'] ==  board['5'] == board['6'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['1'] ==  board['2'] == board['3'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['7'] ==  board['5'] == board['3'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['1'] ==  board['5'] == board['9'] == 'X':
                print('Congratulation, X player win the game!')
                is_win = False
                break
            elif board['3'] ==  board['6'] == board['9'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['2'] ==  board['5'] == board['8'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['1'] ==  board['4'] == board['7'] == 'X':
                print('Congratulation, X player win the game!')
                is_win=False
                break
            elif board['7'] ==  board['8'] == board['9'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
            elif board['4'] ==  board['5'] == board['6'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
            elif board['1'] ==  board['2'] == board['3'] == 'O':
                print('Congratulation, you win the game!')
                is_win=False
                break
            elif board['7'] ==  board['5'] == board['3'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
            elif board['1'] ==  board['5'] == board['9'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
            elif board['3'] ==  board['6'] == board['9'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
            elif board['2'] ==  board['5'] == board['8'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
            elif board['1'] ==  board['4'] == board['7'] == 'O':
                print('Congratulation, O player win the game!')
                is_win=False
                break
        else:
            print("you must select another place")