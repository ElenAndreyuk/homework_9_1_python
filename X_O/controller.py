import view
import model
import emoji
from playsound import playsound
def button_click():
    val = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_over = False
    player1 = True

    while game_over == False:
        view.output_board(val)
        if player1 == True:
            symbol, step = "X", int(input(emoji.emojize(":fire:игрок 1, ваш ход: ", language= 'en')))
        else:
            symbol, step = "O", int(input(emoji.emojize("	:droplet: игрок 2, ваш ход: ", language= 'en')))
        val = model.take_input(step, symbol, val) 
        win = model.get_result(val) 
        if win == "":
            game_over = False
        else:
            game_over = True
        player1 = not(player1)   

    view.output_board(val)
    print(emoji.emojize(f":1st_place_medal: Победил {win}", language='en' ))
    playsound('verdi_pobednyy_marsh.mp3')
