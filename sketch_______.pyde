z=10
x=10
c=10
d=500
e=100
b=100
def setup():
    size(600,600)
def draw():
    global z,x,c,d,e,b
    line(1,500,600,500)
    background(random(0,255),random(0,255),random(0,255))
    fill(random(0,255),random(0,255),random(0,255))
    rect(z,500,x,c)
    rect(z,150,x,c)
    rect(d,300,x,c)
    z +=3
    x -=1
    c -=1
    d -=3
    e +=1
    b +=1
