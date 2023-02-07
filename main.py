import pgzrun

TITLE = "AccordioN"
WIDTH = 450
HEIGHT = 450

# Set the initial colors for the circles
circle_colors = ['black'] * 16
circle_colors2 = ['black'] * 12
circle_size = 12
circle_size_bas = 10
def draw():
    screen.blit('main.png', (0, 0))
    # Draw the circles
    for i in range(16):
        if i % 2 == 0:
            # First column
            screen.draw.filled_circle((80 * (i % 2) + 50, 35 * (i // 2) + 100), circle_size, circle_colors[i])
        else:
            # Second column
            screen.draw.filled_circle((60 * (i % 2) + 30, 35 * (i // 2) + 100 + circle_size), circle_size, circle_colors[i])

    for j in range(12):
        if j % 2 == 0:
            # First column
            screen.draw.filled_circle((80 * (j % 2) + 370, 35 * (j // 2) + 150), circle_size_bas, circle_colors2[j])
        else:
            # Second column
            screen.draw.filled_circle((60 * (j % 2) + 335, 35 * (j // 2) + 120 + circle_size_bas), circle_size_bas, circle_colors2[j])

def on_key_down(key):
    # Change the color of the circle corresponding to the key pressed
    if key == keys.Z:
        circle_colors[0] = 'blue'
        sounds.gg4.play()
    elif key == keys.S:
        circle_colors[1] = 'blue'
        sounds.d4.play()
    elif key == keys.X:
        circle_colors[2] = 'blue'
        sounds.c4.play()
    elif key == keys.D:
        circle_colors[3] = 'blue'
        sounds.f4.play()
    elif key == keys.C:
        circle_colors[4] = 'blue'
        sounds.e4.play()
    elif key == keys.F:
        circle_colors[5] = 'blue'
        sounds.a4.play()
    elif key == keys.V:
        circle_colors[6] = 'blue'
        sounds.g4.play()
    elif key == keys.G:
        circle_colors[7] = 'blue'
        sounds.c5.play()
    elif key == keys.B:
        circle_colors[8] = 'blue'
        sounds.b4.play()
    elif key == keys.H:
        circle_colors[9] = 'blue'
        sounds.e5.play()
    elif key == keys.N:
        circle_colors[10] = 'blue'
        sounds.d5.play()
    elif key == keys.J:
        circle_colors[11] = 'blue'
        sounds.g5.play()
    elif key == keys.M:
        circle_colors[12] = 'blue'
        sounds.f5.play()
    elif key == keys.K:
        circle_colors[13] = 'blue'
        sounds.b5.play()
    elif key == keys.COMMA:
        circle_colors[14] = 'blue'
        sounds.a5.play()
    elif key == keys.L:
        circle_colors[15] = 'blue'
        sounds.d6.play()

    elif key == keys.R:
        circle_colors2[0] = 'blue'
        sounds.e7.play()
    elif key == keys.K_4:
        circle_colors2[1] = 'blue'
        sounds.gg.play()
    elif key == keys.T:
        circle_colors2[2] = 'blue'
        sounds.e4.play()
    elif key == keys.K_5:
        circle_colors2[3] = 'blue'
        sounds.g4.play()
    elif key == keys.Y:
        circle_colors2[4] = 'blue'
        sounds.am.play()
    elif key == keys.K_6:
        circle_colors2[5] = 'blue'
        sounds.cc.play()
    elif key == keys.U:
        circle_colors2[6] = 'blue'
        sounds.a4.play()
    elif key == keys.K_7:
        circle_colors2[7] = 'blue'
        sounds.c4.play()
    elif key == keys.I:
        circle_colors2[8] = 'blue'
        sounds.dm.play()
    elif key == keys.K_8:
        circle_colors2[9] = 'blue'
        sounds.ff.play()
    elif key == keys.O:
        circle_colors2[10] = 'blue'
        sounds.d4.play()
    elif key == keys.K_9:
        circle_colors2[11] = 'blue'
        sounds.f4.play()


def on_key_up(key):
    # Reset the color of the circle when the key is released
    if key == keys.Z:
        circle_colors[0] = 'black'
        sounds.gg4.stop()
    elif key == keys.S:
        circle_colors[1] = 'black'
        sounds.d4.stop()
    elif key == keys.X:
        circle_colors[2] = 'black'
        sounds.c4.stop()
    elif key == keys.D:
        circle_colors[3] = 'black'
        sounds.f4.stop()
    elif key == keys.C:
        circle_colors[4] = 'black'
        sounds.e4.stop()
    elif key == keys.F:
        circle_colors[5] = 'black'
        sounds.a4.stop()
    elif key == keys.V:
        circle_colors[6] = 'black'
        sounds.g4.stop()
    elif key == keys.G:
        circle_colors[7] = 'black'
        sounds.c5.stop()
    elif key == keys.B:
        circle_colors[8] = 'black'
        sounds.b4.stop()
    elif key == keys.H:
        circle_colors[9] = 'black'
        sounds.e5.stop()
    elif key == keys.N:
        circle_colors[10] = 'black'
        sounds.d5.stop()
    elif key == keys.J:
        circle_colors[11] = 'black'
        sounds.g5.stop()
    elif key == keys.M:
        circle_colors[12] = 'black'
        sounds.f5.stop()
    elif key == keys.K:
        circle_colors[13] = 'black'
        sounds.b5.stop()
    elif key == keys.COMMA:
        circle_colors[14] = 'black'
        sounds.a5.stop()
    elif key == keys.L:
        circle_colors[15] = 'black'
        sounds.d6.stop()

    elif key == keys.R:
        circle_colors2[0] = 'black'
        sounds.e7.stop()
    elif key == keys.K_4:
        circle_colors2[1] = 'black'
        sounds.gg.stop()
    elif key == keys.T:
        circle_colors2[2] = 'black'
        sounds.e4.stop()
    elif key == keys.K_5:
        circle_colors2[3] = 'black'
        sounds.g4.stop()
    elif key == keys.Y:
        circle_colors2[4] = 'black'
        sounds.am.stop()
    elif key == keys.K_6:
        circle_colors2[5] = 'black'
        sounds.cc.stop()
    elif key == keys.U:
        circle_colors2[6] = 'black'
        sounds.a4.stop()
    elif key == keys.K_7:
        circle_colors2[7] = 'black'
        sounds.c4.stop()
    elif key == keys.I:
        circle_colors2[8] = 'black'
        sounds.dm.stop()
    elif key == keys.K_8:
        circle_colors2[9] = 'black'
        sounds.ff.stop()
    elif key == keys.O:
        circle_colors2[10] = 'black'
        sounds.d4.stop()
    elif key == keys.K_9:
        circle_colors2[11] = 'black'
        sounds.f4.stop()


pgzrun.go()
