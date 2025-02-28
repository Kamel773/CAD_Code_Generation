import cadquery as cq
from typing import List,Tuple

length:float = 0.628103
width:float = 0.011084
height:float = 0.722001
top_length:float = 0.240157

top_x:float = (length - top_length)/2
shift:float = 0.009237

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

#-0.0018474
part:cq.Workplane = work.extrude(width).translate((-0.018474,height/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')