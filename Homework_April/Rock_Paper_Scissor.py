print("*****Rock Paper Scissor*****")
print('\n1. Rock\n2. Paper\n3. Scissor')
c=1
while c==1:
    player1 = int(input('\nPlayer 1 please input your choice: '))
    if player1>3 or player1<1:
        print('Player1 wrong input')
    player2 = int(input('\nPlayer 2 please input your choice: '))
    if player2>3 or player2<1:
        print('Player2 wrong input')

    if player1==1 and player2==3:
        print('\nPLayer1 selected Rock and Player2 selected Scissor')
        print('Player1 wins!!')
    elif player1==1 and player2==2:
        print('\nPLayer1 selected Rock and Player2 selected Paper')
        print('Player2 wins!!')
    elif player1==2 and player2==1:
        print('\nPLayer1 selected Paper and Player2 selected Rock')
        print('Player1 wins!!')
    elif player1==2 and player2==3:
        print('\nPLayer1 selected Paper and Player2 selected Scissor')
        print('Player2 wins!!')
    elif player1==3 and player2==2:
        print('\nPLayer1 selected Scissor and Player2 selected Paper')
        print('Player1 wins!!')
    elif player1==3 and player2==1:
        print('\nPLayer1 selected Scissor and Player2 selected Rock')
        print('Player2 wins!!')
    else:
        print('System error!!')
    c = int(input("\nPress 1 if you wish to continue"))
