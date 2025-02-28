import cadquery as cq

height:float = 0.48649
radius:float = 0.75
hole_diameter:float = 0.121621621621622*2

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, radius)
    .faces(">Z")
    .hole(hole_diameter, height)
)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')

