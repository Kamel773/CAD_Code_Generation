import cadquery as cq

height:float = 1.5
radius:float = 0.02885/2

part:cq.Workplane = cq.Workplane("XY").cylinder(height, radius)

part = part.rotate((1, 0, 0),(0, 0, 0), 90)
cq.exporters.export(part,'Ground_Truth.stl')