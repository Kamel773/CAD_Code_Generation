import cadquery as cq
from typing import List,Tuple

length:float = 1.5
width:float = 0.73113
extrude:float = 0.00472

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

part = part.translate((-length/2, -width/2, -extrude/2)).rotate((1, 0, 0),(0, 0, 0), 90)
cq.exporters.export(part, 'Ground_Truth.stl')