import pgzrun

TITLE = "Accordion"
WIDTH = 450
HEIGHT = 450

# Constants
NUM_CIRCLES = 16
CIRCLE_SIZE = 12
CIRCLE_SIZE_BAS = 10
CIRCLE_COLORS = ['black'] * NUM_CIRCLES
CIRCLE_COLORS2 = ['black'] * 12

# Key-color-sound mappings
KEY_MAPPING = {
    keys.Z: (0, 'blue', sounds.gg4),
    keys.S: (1, 'blue', sounds.d4),
    keys.X: (2, 'blue', sounds.c4),
    keys.D: (3, 'blue', sounds.f4),
    keys.C: (4, 'blue', sounds.e4),
    keys.F: (5, 'blue', sounds.a4),
    keys.V: (6, 'blue', sounds.g4),
    keys.G: (7, 'blue', sounds.c5),
    keys.B: (8, 'blue', sounds.b4),
    keys.H: (9, 'blue', sounds.e5),
    keys.N: (10, 'blue', sounds.d5),
    keys.J: (11, 'blue', sounds.g5),
    keys.M: (12, 'blue', sounds.f5),
    keys.K: (13, 'blue', sounds.b5),
    keys.COMMA: (14, 'blue', sounds.a5),
    keys.L: (15, 'blue', sounds.d6),
    keys.R: (0, 'blue', sounds.e7),
    keys.K_4: (1, 'blue', sounds.gg),
    keys.T: (2, 'blue', sounds.e4),
    keys.K_5: (3, 'blue', sounds.g4),
    keys.Y: (4, 'blue', sounds.am),
    keys.K_6: (5, 'blue', sounds.cc),
    keys.U: (6, 'blue', sounds.a4),
    keys.K_7: (7, 'blue', sounds.c4),
    keys.I: (8, 'blue', sounds.dm),
    keys.K_8: (9, 'blue', sounds.ff),
    keys.O: (10, 'blue', sounds.d4),
    keys.K_9: (11, 'blue', sounds.f4),
}

def draw():
    screen.blit('main.png', (0, 0))
    draw_circles(CIRCLE_COLORS, CIRCLE_SIZE, 60, 35, 30, 100)
    draw_circles(CIRCLE_COLORS2, CIRCLE_SIZE_BAS, 60, 35, 335, 120)

def draw_circles(colors, size, x_spacing, y_spacing, x_start, y_start):
    for i, color in enumerate(colors):
        column = i % 2
        row = i // 2
        x = x_start + x_spacing * column
        y = y_start + y_spacing * row + (size if column else 0)
        screen.draw.filled_circle((x, y), size, color)

def change_circle_color(index, color):
    if 0 <= index < NUM_CIRCLES:
        CIRCLE_COLORS[index] = color

def play_sound(sound):
    if sound:
        sound.play()

def stop_sound(sound):
    if sound:
        sound.stop()

def on_key_down(key):
    if key in KEY_MAPPING:
        index, color, sound = KEY_MAPPING[key]
        change_circle_color(index, color)
        play_sound(sound)

def on_key_up(key):
    if key in KEY_MAPPING:
        index, _, sound = KEY_MAPPING[key]
        change_circle_color(index, 'black')
        stop_sound(sound)

pgzrun.go()
