import cadquery as cq
from typing import List, Tuple

length:float = 0.375
width:float = 0.11438
height:float = 0.75 

points:List[Tuple[float, float]] = [
    (length/2, 0),
    (length, width/2),
    (length/2, width),
    (0, width/2)
]

part:cq.Workplane = (
    cq.Workplane("XZ")
    .polyline(points)
    .close()
    .extrude(height)
)

part = part.translate((-length/2, 0, 0))
cq.exporters.export(part, 'Ground_Truth.stl')