import cadquery as cq

height:float = 0.00656
diameter:float = 1.5
hole_diameter:float = diameter - 0.203459*2

part:cq.Workplane = cq.Workplane("XZ").cylinder(height, diameter/2).faces(">Z").hole(hole_diameter, height)

part = part.translate((0, 0, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')