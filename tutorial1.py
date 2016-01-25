from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
red = Color(0xff0000, .8)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
thinline = LineStyle(1, black)
rectangle = RectangleAsset(50, 20, thinline, blue)
rectangle2 = RectangleAsset(60, 60, thinline, red)
polygon = PolygonAsset(30, 40, thinline, green)
Sprite(rectangle)
Sprite(rectangle2)
Sprite(polygon)
myapp = App()
myapp.run()

