import turtle as t
y=[[(10,90),(20,90),(10,90),(20,90),(10,0)],
   [(0,90),(0,0),(10,225),(1,0),(-1,0),(14,135),(20,180),(20,90)],
   [(10,90),(10,90),(10,270),(10,270),(10,180),(10,90),(10,90),(10,270),(10,90)],
   [(10,135),(14,225),(10,135),(14,225),(0,0),(10,270),(20,90)],
   [(0,90),(10,270),(10,90),(10,180),(20,90)],
   [(10,180),(10,270),(10,270),(10,90),(10,90),(10,180),(10,270),(0,0),(20,90)],
   [(0,0),(10,135),(1,0),(-1,0),(14,315),(10,270),(10,270),(10,270),(10,135),(14,45)],
   [(10,135),(14,315),(10,180),(10,45),(14,45)],
   [(10,90),(20,90),(10,90),(20,180),(10,270),(10,270),(10,90)],
   [(10,90),(10,45),(14,180),(14,225),(10,90),(10,90),(10,0)]]
u=[1,4,1,7,0,0]
for i in u:
    h=y[i]
    for a,b in h:
        if b == 0 and a == 0: t.penup()
        if b == 0 and a == 1: t.pendown()
        t.forward (a)
        t.right(b)
    t.penup()
    t.forward (10)
    t.pendown()
