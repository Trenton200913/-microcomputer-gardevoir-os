def on_button_pressed_a():
    music.play_melody("C - - - - - - - ", 160)
    basic.clear_screen()
    smarthome.motor_fan(AnalogPin.P1, False)
    basic.show_string("motor fan off")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play_melody("C5 - - - - - - - ", 154)
    basic.clear_screen()
    smarthome.motor_fan(AnalogPin.P0, True)
    basic.show_string("motor fan on")
    smarthome.crash_sensor_setup(DigitalPin.P0)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    katakana.show_string("giggity")
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

music.play_melody("- - G A G A - B ", 143)
basic.clear_screen()
basic.show_leds("""
    . # # # .
        # . . . #
        # # . # #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # # . . #
        # . . . #
        . # # # .
""")
basic.show_leds("""
    . # # # .
        # . . . #
        # # . # #
        # . . . #
        . # # # .
""")
basic.clear_screen()
basic.clear_screen()
basic.show_string("")
basic.clear_screen()
basic.show_string("MICROCOMPUTER gardevoir OS")
basic.clear_screen()
basic.show_string("2022 (C)TMB LTD")
basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
