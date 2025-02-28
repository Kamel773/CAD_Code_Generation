import cadquery as cq
from typing import List,Tuple

length:float = 1.49593
width:float = 0.589754
height:float = 0.382114
top_length:float = 0.910569

top_x:float = (length - top_length)/2
shift:float = 0.026423

points:List[Tuple[float, float]] = [
    (0,0),
    (top_x+shift,height),
    (top_x+top_length+shift,height),
    (length,0)
]

work:cq.Workplane = (
    cq.Workplane("XY").center(-(length/2),-(height/2))
    .polyline(points).close()
)

part:cq.Workplane = work.extrude(width).translate((0,0,0)).rotate((1,0,0),(0,0,0),-90).translate((0,0,-height/2))

cq.exporters.export(part, 'Ground_Truth.stl')