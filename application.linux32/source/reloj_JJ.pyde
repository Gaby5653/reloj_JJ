choclitos= 0
gomitas= 0
hamburguesa= 0
def setup():
    size(200, 200)
def draw():
    background(234, 195, 142)
    global choclitos
    global gomitas
    global hamburguesa
    circle(choclitos, 46, 25)
    if choclitos> height:
       choclitos= 0
    else:
     choclitos= map(second(), 0, 59, 0, height)
    circle(gomitas, 92, 45)
    if gomitas> height:
       gomitas= 0
    else:
     gomitas= map(minute(), 0, 59, 0, height)
    circle(hamburguesa, 138, 65)
    if hamburguesa> height:
       hamburguesa= 0
    else:
     hamburguesa= map(hour(), 0, 59, 0, height)
    
