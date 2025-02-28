import cadquery as cq
from typing import List,Tuple

length:float = 0.20312
width:float = 0.20312
extrude:float = 0.75

pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, width),
    (length, 0)
]

part:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(extrude)
)

part = part.rotate((0, 1, 0),(0, 0, 0), -90)
cq.exporters.export(part, 'Ground_Truth.stl')