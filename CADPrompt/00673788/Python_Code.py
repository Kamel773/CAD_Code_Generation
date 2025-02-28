import cadquery as cq
from typing import List,Tuple

length:float = 1.5 - 0.1875
width:float = 1.5 -0.375
extrude:float = 0.09375

pts:List[Tuple[float, float]] = [(0,0),(0,width),(length,0)]
angle_cut:cq.Workplane = cq.Workplane("ZY").polyline(pts).close().extrude(extrude)

box:cq.Workplane = cq.Workplane("ZY").box(1.5,1.5,extrude)

part:cq.Workplane = box.cut(angle_cut.translate((extrude/2,-1.5/2,-1.5/2)))
part = part.translate((extrude/2,0,0))

cq.exporters.export(part, 'Ground_Truth.stl')