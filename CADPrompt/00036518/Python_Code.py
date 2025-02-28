import cadquery as cq
from typing import List,Tuple

diameter:float = 0.375
length:float = 0.691189
top_length:float = 0.208765

cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(length, diameter/2)
    .rotate((0,1,0),(0,0,0),90)
)

pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, diameter),
    (top_length, diameter),
    (length, 0)
]

intersect_angle:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(diameter)
    .translate((-length/2,-diameter/2,-diameter/2))
)

part:cq.Workplane = (
    cylinder
    .intersect(intersect_angle)
    .rotate((1,0,0),(0,0,0),-90)
)

part = part.rotate((0,0,1),(0,0,0),180).translate((0.40445,0,0))
cq.exporters.export(part, 'Ground_Truth.stl')