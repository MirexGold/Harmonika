import pgzrun

TITLE = "Accordion"
WIDTH = 450
HEIGHT = 450

# Set the initial colors for the circles
circle_colors = ['black'] * 16
circle_colors2 = ['black'] * 12
circle_size = 12
circle_size_bas = 10

# Define circle positions
circle_positions = [
    (50, 100), (30, 100), (50, 100), (30, 100),
    (50, 100), (30, 100), (50, 100), (30, 100),
    (50, 100), (30, 100), (50, 100), (30, 100),
    (50, 100), (30, 100), (50, 100), (30, 100)
]

circle_positions2 = [
    (370, 150), (335, 165), (370, 165), (335, 180),
    (370, 180), (335, 195), (370, 195), (335, 210),
    (370, 210), (335, 225), (370, 225), (335, 240)
]

# Load sounds
note_sounds = {
    0: sounds.gg4, 1: sounds.d4, 2: sounds.c4,
    3: sounds.f4, 4: sounds.e4, 5: sounds.a4,
    6: sounds.g4, 7: sounds.c5, 8: sounds.b4,
    9: sounds.e5, 10: sounds.d5, 11: sounds.g5,
    12: sounds.f5, 13: sounds.b5, 14: sounds.a5,
    15: sounds.d6, 16: sounds.e7, 17: sounds.gg,
    18: sounds.e4, 19: sounds.g4, 20: sounds.am,
    21: sounds.cc, 22: sounds.a4, 23: sounds.c4,
    24: sounds.dm, 25: sounds.ff, 26: sounds.d4,
    27: sounds.f4
}


def draw():
    screen.blit('main.png', (0, 0))

    # Draw the circles in the original layout
    for i, (x, y) in enumerate(circle_positions):
        if i % 2 == 0:
            screen.draw.filled_circle((x + 80 * (i % 2), y + 35 * (i // 2)), circle_size, circle_colors[i])
        else:
            screen.draw.filled_circle((x + 60 * (i % 2), y + 35 * (i // 2) + circle_size), circle_size,
                                      circle_colors[i])

    for j, (x, y) in enumerate(circle_positions2):
        if j % 2 == 0:
            screen.draw.filled_circle((x + 80 * (j % 2), y + 35 * (j // 2)), circle_size_bas, circle_colors2[j])
        else:
            screen.draw.filled_circle((x + 60 * (j % 2), y + 35 * (j // 2) + circle_size_bas), circle_size_bas,
                                      circle_colors2[j])


def on_key_down(key):
    # Change the color of the circle corresponding to the key pressed
    key_color_map = {
        keys.Z: 0, keys.S: 1, keys.X: 2, keys.D: 3,
        keys.C: 4, keys.F: 5, keys.V: 6, keys.G: 7,
        keys.B: 8, keys.H: 9, keys.N: 10, keys.J: 11,
        keys.M: 12, keys.K: 13, keys.COMMA: 14, keys.L: 15,
        keys.R: 16, keys.K_4: 17, keys.T: 18, keys.K_5: 19,
        keys.Y: 20, keys.K_6: 21, keys.U: 22, keys.K_7: 23,
        keys.I: 24, keys.K_8: 25, keys.O: 26, keys.K_9: 27
    }

    if key in key_color_map:
        index = key_color_map[key]
        if index < 16:
            circle_colors[index] = 'blue'
        else:
            circle_colors2[index - 16] = 'blue'

        if index in note_sounds:
            note_sounds[index].play()


def on_key_up(key):
    # Reset the color of the circle when the key is released
    key_color_map = {
        keys.Z: 0, keys.S: 1, keys.X: 2, keys.D: 3,
        keys.C: 4, keys.F: 5, keys.V: 6, keys.G: 7,
        keys.B: 8, keys.H: 9, keys.N: 10, keys.J: 11,
        keys.M: 12, keys.K: 13, keys.COMMA: 14, keys.L: 15,
        keys.R: 16, keys.K_4: 17, keys.T: 18, keys.K_5: 19,
        keys.Y: 20, keys.K_6: 21, keys.U: 22, keys.K_7: 23,
        keys.I: 24, keys.K_8: 25, keys.O: 26, keys.K_9: 27
    }

    if key in key_color_map:
        index = key_color_map[key]
        if index < 16:
            circle_colors[index] = 'black'
        else:
            circle_colors2[index - 16] = 'black'

        if index in note_sounds:
            note_sounds[index].stop()


pgzrun.go()
