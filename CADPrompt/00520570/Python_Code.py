import cadquery as cq
from typing import List,Tuple

length:float = 0.012814
width:float = 0.767871 
height:float = 0.576632
top_width:float = 1.04978

top_x:float = (width - top_width)/2

points:List[Tuple[float, float]] = [
    (0, 0),
    (top_x, height),
    (top_x + top_width, height),
    (width, 0)
]

work:cq.Workplane = (
    cq.Workplane("XY").center(-(width/2), -(height/2))
    .polyline(points).close()
)

part:cq.Workplane = work.extrude(length).translate((0,0,0)).rotate((1,0,0),(0,0,0),-90)

part = part.translate((-0.212662,0,0.024279))
cq.exporters.export(part, 'Ground_Truth.stl')