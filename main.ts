input.onButtonPressed(Button.A, function () {
    music.playMelody("C - - - - - - - ", 160)
    basic.clearScreen()
    smarthome.motorFan(AnalogPin.P1, false)
    basic.showString("motor fan off")
})
input.onButtonPressed(Button.B, function () {
    music.playMelody("C5 - - - - - - - ", 154)
    basic.clearScreen()
    smarthome.motorFan(AnalogPin.P0, true)
    basic.showString("motor fan on")
    smarthome.crashSensorSetup(DigitalPin.P0)
    basic.showNumber(smarthome.ReadSoilHumidity(AnalogPin.P1))
})
input.onGesture(Gesture.Shake, function () {
    katakana.showString("giggity")
})
music.playMelody("G G G A G A - C5 ", 143)
basic.clearScreen()
basic.showLeds(`
    . # # # .
    # . . . #
    # # . # #
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . # # # .
    # . . . #
    # # . . #
    # . . . #
    . # # # .
    `)
basic.showLeds(`
    . # # # .
    # . . . #
    # # . # #
    # . . . #
    . # # # .
    `)
basic.clearScreen()
basic.clearScreen()
basic.showString("")
basic.clearScreen()
basic.showString("MICROCOMPUTER gardevoir OS")
basic.clearScreen()
basic.showString("2022 (C)TMB LTD")
basic.clearScreen()
basic.forever(function () {
	
})
