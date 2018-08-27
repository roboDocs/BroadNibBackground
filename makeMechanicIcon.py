import os
import drawBot

'''
generates a Mechanic2 icon for BroadNibBackground using BroadNibBackground

run this script in the DrawBot RF extension
requires a skeleton glyph on which to apply the 'broadnib'

'''

# get path to BroadNibBackground module inside the extension
baseFolder = os.getcwd()
extensionFolder = os.path.join(baseFolder, 'BroadNibBackground.roboFontExt')
libFolder = os.path.join(extensionFolder, 'lib')
modulePath = os.path.join(libFolder, 'BroadNibBackground.py')

# import the BroadNibBackground module
import importlib.util
spec = importlib.util.spec_from_file_location("broadNibBackground", modulePath)
broadNibBackground = importlib.util.module_from_spec(spec)
spec.loader.exec_module(broadNibBackground)

# get a glyph
glyph = CurrentGlyph()

# define broadnib parameters
steps = 12
width = 200
height = 50
angle = 27
shape = oval

# draw icon...
size(512, 512)
translate(22, 67)
scale(0.75)
fill(0, 1, 0.6, 0.6)

# draw broadnib pen
pen = broadNibBackground.BroadNibPen(None, steps, width, height, angle, shape, ctx=drawBot)
glyph.draw(pen)

# draw original contours
fill(None)
stroke(0, 0.3)
strokeWidth(20)
drawGlyph(glyph)

# save result to to .png image
imgPath = os.path.join(baseFolder, 'broadNibBackgroundMechanicIcon.png')
saveImage(imgPath)
