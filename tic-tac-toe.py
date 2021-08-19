import turtle
import math
import time


def screen_setup() :
    
    scrn.bgcolor("#050609")
    scrn.title("Tic-tac-Toe")
    scrn.setup(height=700,width=800)


def won(letter) :
    for i in range(0,3) :
        if board[i][0]==board[i][1] and board[i][0] == board[i][2] and board[i][0]==letter :
            draw_vertical_line(i)
            return 
        elif board[0][i]==board[1][i] and board[0][i] == board[2][i] and board[0][i]==letter :
            draw_horizontal_line(i)
            return
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0] == letter) :
        draw_left_diagonal()
        return 
    else :
        draw_right_diagonal()
        return 
    
def draw_left_diagonal() :
        t = turtle.Turtle()
        t.color("#FF0000")
        t.speed(0)
        t.pensize(5)
        t.hideturtle()
        t.penup()
        t.goto(-300,300-200*0)
        t.right(45)
        t.pendown()
        t.forward(800)
    
def draw_right_diagonal() :
        t = turtle.Turtle()
        t.color("#FF0000")
        t.speed(0)
        t.pensize(5)
        t.hideturtle()
        t.penup()
        t.goto(300,300-200*0)
        t.left(225)
        t.pendown()
        t.forward(800)
    
def draw_vertical_line(i) :
    t = turtle.Turtle()
    t.color("#FF0000")
    t.speed(0)
    t.pensize(5)
    t.hideturtle()
    t.penup()
    t.goto(-300,190-200*i)
    t.pendown()
    t.forward(600)

def draw_horizontal_line(x) :
    t = turtle.Turtle()
    t.right(90)
    t.color("#FF0000")
    t.speed(0)
    t.pensize(5)
    t.hideturtle()
    t.penup()
    t.goto(-200+200*x,300)
    t.pendown()
    t.forward(600)

def create_board() :
    penb.color("#FFFFFF")
    penb.speed(0)
    penb.pensize(4)
    penb.hideturtle()
    for x in range(0,2) :
        penb.up()
        penb.goto(-300,100-200*x)
        penb.down()
        penb.forward(600)

    penb.right(90)
    for x in range(0,2) :
         penb.up()
         penb.goto(-100+200*x,300)
         penb.down()
         penb.forward(600)
    
def numbering_board() :
    penb.color("#FFFB00")
    num = 1
    for x in range(0,3) :
        for y in range(0,3) :
            penb.penup()
            penb.goto(-290+y*200 ,280 - x * 200)
            penb.pendown()
            penb.write(num,font = ("Comic Sans MS",10))
            num+=1


def draw_x(x,y) :
    penb.color("green")
    penb.penup()
    penb.goto(x,y)
    penb.pendown()
    penb.setheading(60)
    
    for i in range(0,2) :
        penb.forward(75)
        penb.backward(150)
        penb.forward(75)
        penb.left(60)

def draw_o(x,y) :
    penb.color("green")
    penb.penup()
    penb.goto(x,y+75)
    penb.pendown()
    penb.setheading(180)

    penb.circle(75)

def activate(func) :
    for i in range(0,9) :
        scrn.onkey(func[i],str(i+1))
        
def winner(letter) :
    for i in range(0,3) :
        #row 
        if board[i][0]==board[i][1] and board[i][0] == board[i][2] and board[i][0]==letter :          
            return True
        #column
        elif board[0][i]==board[1][i] and board[0][i] == board[2][i] and board[0][i]==letter :
            return True
            #left diagonal
    if(board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[0][0] == letter) :
        return True
    #right diagonal
    elif (board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[0][2]==letter) :
        return True
    return False


def deactivate() :
        for i in range(0,9) :
            scrn.onkey(None,str(i+1))
        time.sleep(2)
        scrn.bye()

            
def add(row,column) :
    global count
    alert.clear()
    if board[row][column]=="x" or board[row][column]=="o" :

        alert.write("that spot is taken ", font = ("Comic Sans MS", 36))
    else :
        if count%2 == 0 :
            draw_x(-200+200*column,200-200 * row)
            board[row][column] = "x"
            count+=1
            if(winner("x")) :
                won("x")
                time.sleep(2)
                scrn.clear()
                screen_setup()
                alert.goto(-97,0)
                alert.write("You won!!",font = ("Comic Sans MS",36))
                
                deactivate()
        else :
            draw_o(-200+200*column,200-200*row)
            board[row][column] = "o"
            count+=1
            if(winner("o")) :
                won("o")
                time.sleep(2)
                scrn.clear()
                screen_setup()
                alert.goto(-97,0)
                alert.write("Opponent won!!",font = ("Comic Sans MS",36))
                deactivate()
        if check_draw() :
            time.sleep(2)
            scrn.clear()
            screen_setup()
            alert.goto(-97,0)
            alert.write("Draw",font = ("Comic Sans MS",36))
            deactivate()
def check_draw() :
    for i in range(0,3) :
        for j in range(0,3) :
            if(board[i][j]==" ") : return False 
    return True      
def square_one() :
    add(0,0)
def square_two() :
    add(0,1)
def square_three() :
    add(0,2)
def square_four() :
    add(1,0)
def square_five() :
    add(1,1)
def square_six() :
    add(1,2)
def square_seven() :
    add(2,0)
def square_eight() :
    add(2,1)
def square_nine() :
    add(2,2)
func = [square_one,square_two,square_three, square_four,square_five,square_six,square_seven,square_eight,square_nine]
board = []

for i in range(0,3) :
    row = []
    for j in range(0,3) :
        row.append(" ")
    board.append(row)

def setup_alert() :
    alert.penup()
    alert.hideturtle()
    alert.goto(-130,0)
    alert.pensize(3)
    alert.color("red")



count = 0
scrn = turtle.Screen()
penb = turtle.Turtle()
alert = turtle.Turtle()
screen_setup()
create_board()
numbering_board()
activate(func)
scrn.listen()
setup_alert()


# if you can't play the game remove the following line 
input("Press any key..")
