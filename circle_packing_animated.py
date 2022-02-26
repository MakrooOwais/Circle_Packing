import random
from PIL import Image
from p5 import *
from circle import Circle

global circles
circles = []


def setup():
    global img
    img = load_image("Circle Packing\data.png")
    global width, height
    width, height = img.width, img.height
    global img_pix
    img_pix = Image.open("Circle Packing\data.png").load()
    global spots
    spots = []
    for x in range(img.width):
        for y in range(img.height):
            b = img_pix[x, y]
            if b != (0, 0, 0):
                spots.append((x, y))

    size(width, height)
    c = Circle(0, 0)
    c.set_w_h(width, height)


def draw():
    background(0)

    total = 1
    count = 0
    attempts = 0
    while count < total:
        new_c = new_circle()
        if new_c:
            circles.append(new_c)
            count = count + 1
        attempts = attempts + 1
        if attempts > 1000:
            no_loop()
            print("FINISHED")
            break

    for circle in circles:
        if circle.growing:
            if circle.edges():
                circle.growing = False
            else:
                for other in circles:
                    if other != circle:
                        d = dist((circle.x, circle.y), (other.x, other.y))
                        if d - 2 < circle.r + other.r:
                            circle.growing = False
                            break

        circle.grow()
        circle.show()

    save_frame("circles.png")


def new_circle():
    p = spots[random.randrange(len(spots))]

    valid = True
    for circle in circles:
        d = dist(p, (circle.x, circle.y))
        if d < circle.r:
            valid = False
            break
    if valid:
        return Circle(*p)
    else:
        return None


if __name__ == "__main__":
    run()
