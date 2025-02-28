import cadquery as cq

height:float = 0.75
diameter:float = 0.07812
hole_diameter:float = 0.046741

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces(">Z")
    .hole(hole_diameter, height)
)

part = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')