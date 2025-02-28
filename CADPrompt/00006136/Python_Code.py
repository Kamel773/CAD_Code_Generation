import cadquery as cq
from typing import List,Tuple

length:float = 1.04094
width:float = 0.465517
extrude:float = 0.75

pts:List[Tuple[float, float]] = [
    (0, 0),
    (length/2, width),
    (length, 0)
]
part:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(extrude)
)

part = part.translate((-length/2,0,0)).rotate((0,0,1),(0,0,0),-90).rotate((0,1,0),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')