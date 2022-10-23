import view
import model
def button_click():
    val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_over = False
    player1 = True

    while game_over == False:
        view.output_board(val)
        if player1 == True:
            symbol, step = "X", int(input("игрок 1, ваш ход: "))
        else:
            symbol, step = "O", int(input("игрок 2, ваш ход: "))
        val = model.take_input(step, symbol, val) 
        win = model.get_result(val) 
        if win == "":
            game_over = False
        else:
            game_over = True
        player1 = not(player1)   

    view.output_board(val)
    print("Победил", win)