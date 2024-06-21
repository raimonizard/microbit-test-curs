input.onButtonPressed(Button.A, function () {
    for (let index = 0; index < 4; index++) {
        basic.showIcon(IconNames.No)
        control.waitMicros(10000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            `)
        control.waitMicros(10000)
        basic.showIcon(IconNames.Yes)
        control.waitMicros(10000)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Cow)
})
basic.forever(function () {
	
})
