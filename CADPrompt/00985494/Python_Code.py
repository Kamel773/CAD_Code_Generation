import cadquery as cq
from typing import List,Tuple

length:float = 0.495408
width:float = 0.744939
height:float = 0.233091
top_length:float = 0.148743

top_x:float = (length - top_length)/2
shift:float = 0

points:List[Tuple[float,float]] = [
    (0,0),
    (top_x+shift,height),
    (top_x+top_length+shift,height),
    (length,0)
]

work:cq.Workplane = (
    cq.Workplane("XZ").center(-(length/2),-(height/2))
    .polyline(points).close()
)

part:cq.Workplane = work.extrude(width)
part = part.rotate((0,1,0),(0,0,0), -90).translate((-height/2,0,0))


cq.exporters.export(part, 'Ground_Truth.stl')