import turtle
import turtle as t

## 함수 선언 ##
def screenLeftClick(x,y) :
    global r, g, b
    global i
    t.pencolor(r,g,b)
    t.pendown()
    t.goto(x,y)

def screenRightClick(x,y) :
    global i
    t.penup()
    t.goto(x,y)

def screenMidClick(x,y) :
    global r,g,b
    global i

    if (i%3==1) :
        t.shape('arrow')
    if (i%3==2) :
        t.shape('circle')
    if (i%3==0) :
        t.shape('turtle')
    i+=1

    (p,q) = t.pos()

    t.penup()
    t.goto(x,y)
    t.pendown()

    for k in range(5): #별 그리기
        t.pensize(2)
        t.forward(100)
        t.left(144)
        t.speed(5)
    t.penup()
    t.goto(p,q)
    t.pensize(8)
    t.pendown()

## 변수 선언 부분 ##
r, g, b = 0.0,0.0,0.0
i = 1
p,q = 0.0,0.0

## 메인 코드 부분 ##
t.title('거북이로 그림을 그리자!')
t.shape('turtle')
t.speed(4)
t.pensize(8)

t.onscreenclick(screenLeftClick, 1)
t.onscreenclick(screenMidClick, 2)
t.onscreenclick(screenRightClick, 3)

t.done()


