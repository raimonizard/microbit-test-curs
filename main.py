def on_button_pressed_a():
    for index in range(4):
        basic.show_icon(IconNames.NO)
        control.wait_micros(10000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            """)
        control.wait_micros(10000)
        basic.show_icon(IconNames.YES)
        control.wait_micros(10000)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_icon(IconNames.COW)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
