import cadquery as cq

height:float = 0.09494
diameter:float = 1.5
hole_diameter:float = .93038

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces(">Z")
    .hole(hole_diameter, height)
)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')