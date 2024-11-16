#section 26
#Member's Name                    Id no.
#1.Mekhluqat Abdulwehab           ugr/30876/15
#2.Khulud Mohammed                ugr/30809/15
#3.Hidaya Nurmeka                 ugr/30681/15
#4.Hikma Mohamedin                ugr/30682/15
from cs1graphics import*
paper=Canvas(1400,800,"skyblue","my world")
suna22=Layer()
sun=Circle(40,Point(0,250))
paper.add(sun)
sun.setFillColor("yellow")
grass=Rectangle(1400,200)
grass.moveTo(600,700)
grass.setDepth(80)
grass.setFillColor("green")
paper.add(grass)
facade=Square(280,Point(600,600))
facade.setFillColor("white")
paper.add(facade)
door=Rectangle(80,140,Point(600,650))
door.setFillColor("brown")
paper.add(door)
roof=Polygon(Point(120,400),Point(230,200),Point(410,200),Point(510,400))
roof.setFillColor("brown")
roof.moveTo(400,500)
paper.add(roof)
chimney=Rectangle(25,50,Point(500,600))
chimney.setFillColor("darkblue")
chimney.setDepth(140)
chimney.moveTo(650,280)
paper.add(chimney)
smoke=Path(Point(310,140),Point(300,130),Point(320,110),Point(310,100))
smoke.moveTo(650,255)
paper.add(smoke)
tree=Polygon(Point(100,160),Point(60,280),Point(140,280))
tree.setFillColor("darkgreen")
tree.moveTo(800,500)
paper.add(tree)
tree5=Layer()
t51=Polygon(Point(200,300),Point(210,80),Point(220,300))
t51.setFillColor("brown")
tree5.add(t51)
lv=Polygon(Point(210,80),Point(225,120),Point(220,120),Point(240,150),Point(230,150),Point(250,180),Point(240,180),Point(260,210),Point(250,210),Point(270,240),Point(150,240),Point(170,210),Point(160,210),Point(180,180),Point(170,180),Point(190,150),Point(180,150),Point(200,120),Point(195,120),Point(210,80))
lv.setFillColor("darkgreen")                                                                                                                                                                                  
tree5.add(lv)
tree5.setDepth(1)
tree5.moveTo(60,300)
paper.add(tree5)

T1=tree5.clone()
T1.scale(0.7)
T1.moveTo(800,400)
paper.add(T1)

pole=Rectangle(10,250)
pole.setFillColor("gray")
pole.moveTo(350,680)
paper.add(pole)

bird1=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird1.setBorderWidth(10)
bird1.setBorderColor("gray")
bird1.setDepth(10)
bird1.moveTo(900, 50)
paper.add(bird1)

bird2=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird2.setBorderWidth(10)
bird2.setBorderColor("black")
bird2.setDepth(10)
bird2.moveTo(950, 100)
paper.add(bird2)

bird3=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird3.setBorderWidth(10)
bird3.setBorderColor("black")
bird3.setDepth(10)
bird3.moveTo(800, 50)
paper.add(bird3)

bird4=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird4.setBorderWidth(10)
bird4.setBorderColor("white")
bird4.setDepth(10)
bird4.moveTo(850, 100)
paper.add(bird4)

bird5=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird5.setBorderWidth(10)
bird5.setBorderColor("white")
bird5.setDepth(10)
bird5.moveTo(820, 90)
paper.add(bird5)

bird6=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird6.setBorderWidth(10)
bird6.setBorderColor("gray")
bird6.setDepth(10)
bird6.moveTo(800, 95)
paper.add(bird6)

for i in range (150):
    bird1.flip(80)
    bird2.flip(80)
    bird3.flip(80)
    bird4.flip(80)
    bird5.flip(80)
    bird6.flip(80)
    
    bird1.move(-40,0)
    bird2.move(-20,0)
    bird3.move(-40,0)
    bird4.move(-20,0)
    bird5.move(-20,0)
    bird6.move(-40,0)
    
    bird1.scale(0.99)
    bird2.scale(0.99)
    bird3.scale(0.99)
    bird4.scale(0.99)
    bird5.scale(0.99)
    bird6.scale(0.99)
    
bulb=Circle(20,Point(350,550))
bulb.setFillColor("white")
paper.add(bulb)
from time import sleep
timeDelay=.70
a=0
b=0
for i in range(12):
    sun.move(a,b)
    sleep(timeDelay)
    a=a+50
    b=b-2
paper.setBackgroundColor("gray")
bird1=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird1.setBorderWidth(10)
bird1.setBorderColor("gray")
bird1.setDepth(10)
bird1.moveTo(900, 50)
paper.add(bird1)

bird2=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird2.setBorderWidth(10)
bird2.setBorderColor("black")
bird2.setDepth(10)
bird2.moveTo(950, 100)
paper.add(bird2)

bird3=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird3.setBorderWidth(10)
bird3.setBorderColor("black")
bird3.setDepth(10)
bird3.moveTo(800, 50)
paper.add(bird3)

bird4=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird4.setBorderWidth(10)
bird4.setBorderColor("white")
bird4.setDepth(10)
bird4.moveTo(850, 100)
paper.add(bird4)

bird5=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird5.setBorderWidth(10)
bird5.setBorderColor("white")
bird5.setDepth(10)
bird5.moveTo(820, 90)
paper.add(bird5)

bird6=Path(Point(250, 85), Point(270, 70), Point(280, 80), Point(290, 70), Point(310, 85))
bird6.setBorderWidth(10)
bird6.setBorderColor("gray")
bird6.setDepth(10)
bird6.moveTo(800, 95)
paper.add(bird6)

for i in range (150):
    bird1.flip(40)
    bird2.flip(40)
    bird3.flip(40)
    bird4.flip(40)
    bird5.flip(40)
    bird6.flip(40)
    
    bird1.move(-40,0)
    bird2.move(-20,0)
    bird3.move(-40,0)
    bird4.move(-20,0)
    bird5.move(-20,0)
    bird6.move(-40,0)
    
    bird1.scale(1.0)
    bird2.scale(1.0)
    bird3.scale(1.0)
    bird4.scale(1.0)
    bird5.scale(1.0)
    bird6.scale(1.0)
    

c=200
d=-10
for i in range(10):
    sun.move(c,d)
    sleep(timeDelay)
    c=c+40
    d=d+20
paper.setBackgroundColor("black")
from time import sleep
timeDelay=.20   

moon=Circle(60,Point(0,400))
moon.setDepth(140)
moon.setFillColor("white")
paper.add(moon)
star=Circle(6,Point(700,100))
star.setFillColor("white")
paper.add(star)
bulb.setFillColor("yellow")
star1=Circle(6,Point(100,100))
star1.setFillColor("white")
paper.add(star1)
star2=Circle(6,Point(360,180))
star2.setFillColor("white")
paper.add(star2)
star3=Circle(6,Point(300,400))
star3.setFillColor("white")
paper.add(star3)
star4=Circle(6,Point(740,120))
star4.setFillColor("white")
paper.add(star4)
star5=Circle(6,Point(380,500))
star5.setFillColor("white")
paper.add(star5)
star6=Circle(6,Point(500,100))
star6.setFillColor("white")
paper.add(star6)
star7=Circle(6,Point(850,400))
star7.setFillColor("white")
paper.add(star7)
star8=Circle(6,Point(900,400))
star8.setFillColor("white")
paper.add(star8)
star9=Circle(6,Point(1000,130))
star9.setFillColor("white")
paper.add(star9)
star10=Circle(6,Point(1200,300))
star10.setFillColor("white")
paper.add(star10)
star11=Circle(6,Point(1100,80))
star11.setFillColor("white")
paper.add(star11)
a=0
b=0
for i in range(7):
    moon.move(a,b)
    sleep(timeDelay)
    a=a+30
    b=b-15
c=220
d=-10
