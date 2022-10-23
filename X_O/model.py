def take_input(step,symbol, val):
    val[step - 1] = symbol
    return val

def get_result(val):
    victories = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    win = ""
    for i in victories:
        if val[i[0]] == "X" and val[i[1]] == "X" and val[i[2]] == "X":
            win = "X"
        if val[i[0]] == "O" and val[i[1]] == "O" and val[i[2]] == "O":
            win = "O"            
    return win
