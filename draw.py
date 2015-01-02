#!/usr/bin/env python3

import math
import cairo

WIDTH, HEIGHT = 500, 500

surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context (surface)

#ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas
print(ctx.get_current_point())

ctx.move_to (250, 250)
print(ctx.get_current_point())
ctx.line_to (0, 0)


#ctx.arc (0.2, 0.1, 0.1, -math.pi/2, 0)
#ctx.line_to (0.5, 0.1)
#ctx.curve_to (0.5, 0.2, 0.5, 0.4, 0.2, 0.8)
#ctx.close_path ()

print(ctx.get_current_point())

#ctx.set_source_rgb (0.3, 0.2, 0.5) # Solid color
#ctx.set_line_width (0.02)
ctx.stroke ()

surface.write_to_png ("example.png") # Output to PNG
