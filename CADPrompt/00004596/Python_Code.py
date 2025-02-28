import cadquery as cq

height:float = 1.5
diameter:float = 0.75
hole_diameter:float = 0.3125

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces(">Z")
    .hole(hole_diameter, height)
)

part = part.rotate((0, 0, 0),(0, 1, 0), -90)
cq.exporters.export(part, 'Ground_Truth.stl')