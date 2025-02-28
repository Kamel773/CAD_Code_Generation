import cadquery as cq

height:float = 0.75
diameter:float = 0.85714
hole_diameter:float = 0.535714

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces(">Z")
    .hole(hole_diameter, height)
)

part = part.translate((0, 0, height/2)).rotate((1, 0, 0),(0, 0, 0), -90)
cq.exporters.export(part, 'Ground_Truth.stl')