import cadquery as cq
from typing import List,Tuple

length:float = 0.75
width:float = 0.75
extrude:float = 0.03

pts:List[Tuple[float, float]] = [(0,0),(0,width),(length,0)]
triangle:cq.Workplane = cq.Workplane("ZX").polyline(pts).close().extrude(extrude)

part:cq.Workplane = triangle

part = part.translate((0,-extrude/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')