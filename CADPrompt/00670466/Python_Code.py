import cadquery as cq
from typing import List,Tuple

length:float = 1.5
width:float = 0.150756
extrude:float = 0.188445

pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, width),
    (length, 0)
]
part:cq.Workplane = cq.Workplane("XY").polyline(pts).close().extrude(extrude)

part = part.translate((-length/2, -width/2, -extrude/2)).rotate((0,0,1),(0,0,0),90)
cq.exporters.export(part, 'Ground_Truth.stl')