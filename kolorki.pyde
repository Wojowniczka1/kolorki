def setup():
    frameRate(60)
    size(400, 400)
    background(255, 255, 170)
    strokeWeight(2)
    global krotka0
    global krotka1
    global krotka2
    krotka0 = (149, 230, 163)
    krotka1 = (220, 135, 220)
    krotka2 = (255, 168, 149)
    global krotka3
    global krotka4
    global krotka5
    krotka3 = (159, 225, 176)
    krotka4 = (220, 180, 235)
    krotka5 = (255, 180, 170)
    global w
    global x
    global y
    global z
    w = 0
    x = 0
    y = 50
    z = 50
    
def draw():
    global w
    w = w + 1
    global x
    x = x + 1
    rect(w, x, y, z)
    if w < 100:
        fill(*krotka0)
        stroke(*krotka3)
    if w > 101:
        fill(*krotka1)
        stroke(*krotka4)
    if w > 250:
        fill(*krotka2)
        stroke(*krotka5)
    if w > width:
        exit()
