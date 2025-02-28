import cadquery as cq
length:float = .75
width:float = 0.4
height:float = 0.2375
diameter:float = 0.11875

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .cylinder(height, diameter/2, combine="cut")
)

part = part.translate((-length/2, width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')