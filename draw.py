import turtle as t
import time




# 画山的函数
def drawMountain(x, y):
    # 设置画笔信息
    t.colormode(255)
    t.color((0, 100, 0))#用较深的绿色画轮廓
    t.speed(1000)
    t.pensize(5)

    t.penup()
    t.goto(x, y)
    t.pendown()
    t.seth(70)

    # 画山
    t.begin_fill()
     #山的左侧轮廓  向右上画
    for i in range(30):
        t.right(1)
        t.forward(5)
    #山顶
    t.circle(-20, 80)
    #山的右侧轮廓  向左下画
    for i in range(30):
        t.right(1)
        t.forward(5)
    #形成封闭图形，从而使山为纯绿色
    t.color((0, 255, 0))
    t.seth(180)
    t.forward(120)
    t.end_fill()

# 画裂开的函数
def drawSplit(x,y):
    # 设置画笔信息
    t.speed(1000)
    t.pensize(5)
    t.colormode(255)
    t.color((0,0,0))

    t.penup()
    t.goto(x, y)
    t.pendown()

    # 画曲线
    t.seth(-135)
    for i in range(3):
        t.circle(11, 80)
        t.circle(-11, 80)



#写成语
def drawWords(words, posx, posy):
    t.hideturtle() #使 turtle 不可见
    t.tracer(False) #关闭轨迹
    t.penup()
    t.goto(posx, posy)
    t.pencolor("black")
    t.pendown()
    i = 0
    while i < len(words):
        t.write(words[i], align="center", font=("微软雅黑", 14, "normal"))
        i += 1
        t.penup()
        t.goto(posx, posy - 20 * i)
        t.pendown()
#写名字
def drawName(code):
    t.hideturtle() #使 turtle 不可见
    t.tracer(False) #关闭轨迹
    W = 3
    H = 100
    x = 300
    y = -200
    t.pencolor('black')
    t.penup()
    for f in code:
        t.fillcolor("black" if f == "1" else "white")
        t.begin_fill()
        t.goto(x, y)
        t.goto(x + W, y)
        t.goto(x + W, y + H)
        t.goto(x, y + H)
        t.goto(x, y)
        t.end_fill()
        x += W
   
def drawAll(words):
    # 图名山崩地裂
    t.title('Python')


    t.hideturtle() #使 turtle 不可见
    t.setup(1000,600) #设置图形大小
    t.tracer(False) #关闭轨迹
    t.screensize(bg="#643200")#设置背景色为棕色，大地的颜色
   
    for i in range(0,10):
        # 清空画面
        t.clear()
        drawName("10100000010011110011010111") #本人学号42024151
        drawWords(["计203", "许文杰", "42024151"], 350, -225)
        drawWords(words, 350, 200)
    # 画很多山
        drawMountain(50, 70)
        drawMountain(-100, 70)
        drawMountain(-225, 70)
        drawMountain(-150, 30)
        drawMountain(-300, 30)
        drawMountain(-50, 30)
        drawMountain(80, 30)
        # 更新画面
        t.update()
        time.sleep(0.1)

    # 画山的裂开

        drawSplit(0, 190)
        drawSplit(-125,190)
        drawSplit(-50, 150)
        drawSplit(-200, 150)
        drawSplit(50, 150)
        drawSplit(180, 150)
    #画地面的裂开
        drawSplit(-200, -150)
        drawSplit(50, -150)
        drawSplit(180, -150)
        drawSplit(-150, -100)
        drawSplit(100, -100)
        drawSplit(250, -100)
        
        

    # 画图完毕后保留画面
    t.done()

    drawAll("山崩地摧")