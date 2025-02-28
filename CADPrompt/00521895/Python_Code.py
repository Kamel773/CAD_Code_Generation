import cadquery as cq
length:float = 1
width:float = 0.75
height:float = 0.75
diameter:float = 0.5

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .cylinder(height, diameter/2, combine="cut")
)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')