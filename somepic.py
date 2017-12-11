import turtle
import colorsys

def get_color(h, l, s):
    return [int(i * 255) for i in colorsys.hls_to_rgb(
        h / 255.0, l / 255.0, s / 255.0)]

def draw_triangle(t, s, c):  # turtle instance, length of side, color
    t.color(c)
    t.fillcolor(c)
    t.begin_fill()
    for _ in range(3):
        t.forward(s)
        t.right(120)
    t.end_fill()

def render():
    t = turtle.Turtle()
    t.speed(100)
    side_of_length = 700

    hue = 0
    saturation = 155
    lightness = 155

    while side_of_length > 0:
        color = get_color(hue, saturation, lightness)
        rgb_color = '#{:2x}{:2x}{:2x}'.format(*color)
        draw_triangle(t, side_of_length, rgb_color)
        t.right(10)
        side_of_length -= 10
        hue += 10

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    render()

    window.exitonclick()