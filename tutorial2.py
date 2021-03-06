from ggame import App, Color, LineStyle, Sprite
from ggame import CircleAsset

red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)

thinline = LineStyle(1, black)
mycircle = CircleAsset(5, thinline, blue)
circleto = CircleAsset(5, thinline, red)
xcoordinates = range(50, 500, 20)

# Generate a list of sprites that form a line!
sprites = [Sprite(mycircle, (x, .5*x)) for x in xcoordinates]
sprites = [Sprite(circleto, (x, .5*x + 10)) for x in xcoordinates]

myapp = App()
myapp.run()
