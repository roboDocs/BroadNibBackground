import os
import drawBot

# get path to extension lib
baseFolder = os.getcwd()
extensionFolder = os.path.join(baseFolder, 'BroadNibBackground.roboFontExt')
libFolder = os.path.join(extensionFolder, 'lib')
modulePath = os.path.join(libFolder, 'BroadNibBackground.py')

# import pen from module
import importlib.util
spec = importlib.util.spec_from_file_location("broadNibBackground", modulePath)
broadNibBackground = importlib.util.module_from_spec(spec)
spec.loader.exec_module(broadNibBackground)

glyph = CurrentGlyph()

steps = 12
width = 200
height = 50
angle = 27
shape = oval

size(512, 512)
translate(22, 67)
scale(0.75)
fill(0, 1, 0.6, 0.6)

pen = broadNibBackground.BroadNibPen(None, steps, width, height, angle, shape, ctx=drawBot)
glyph.draw(pen)

fill(None)
stroke(0, 0.3)
strokeWidth(20)
drawGlyph(glyph)

imgPath = os.path.join(baseFolder, 'broadNibBackgroundMechanicIcon.png')
saveImage(imgPath)

