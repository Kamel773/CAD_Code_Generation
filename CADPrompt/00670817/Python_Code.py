import cadquery as cq

height:float = 0.113636
diameter:float = 1.5
hole_diameter:float = diameter - 0.380682*2

part:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2).faces(">Z").hole(hole_diameter, height)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')