import cadquery as cq
from typing import List,Tuple

length:float = 0.95149
width:float = 0.15482
extrude:float = 0.11183

pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, width),
    (length, 0)
]
part:cq.Workplane = cq.Workplane("XY").polyline(pts).close().extrude(extrude)

part = part.rotate((1, 0, 0),(0, 0, 0), -90).translate((-0.75,0,-width/2+0.00752))
cq.exporters.export(part, 'Ground_Truth.stl')