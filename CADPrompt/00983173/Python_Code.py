import cadquery as cq

length = 1.3125
width = 1.3125
height = 0.0625
diameter = 1
hole_diameter = diameter - 0.03125*2
extrude = 0.6875
z_offset = 0.025308

part = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("Z")
    .tag("top_plate")
    .workplane(offset=0)
    .center(0,0)
    .circle(diameter/2)
    .extrude(extrude)
    .faces(">Z")
    .hole(hole_diameter)
    .faces(tag="top_plate")
    .edges()
    .toPending()
    .offset2D(-.05)
    .vertices()
    .hole(0.05)
).translate((0,0,z_offset+0.005942))

cq.exporters.export(part, 'Ground_Truth.stl')