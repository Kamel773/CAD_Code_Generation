import cadquery as cq

length:float = 1.5
width:float = 1.5
height:float = 0.1125
diameter:float = 0.15

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .cylinder(height, diameter/2, combine="cut")
)

part:cq.Workplane = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')