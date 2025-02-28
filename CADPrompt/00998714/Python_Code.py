import cadquery as cq
from typing import List,Tuple

length:float = 0.929516
width:float = 0.54 
height:float = 0.3
top_length:float = 1.5

top_x:float = (length - top_length)/2

points:List[Tuple[float, float]] = [
    (0, 0),
    (length, 0),
    (top_x + top_length, width),
    (top_x, width),
]

work:cq.Workplane = (
    cq.Workplane("XZ")
    .center(-length/2,-width/2)
    .polyline(points).close()
)

part:cq.Workplane = work.extrude(height).translate((0,height/2,width/2+0.12))

radius = (length/2)+0.014

ellipse = cq.Workplane("XZ").circle(radius).extrude(height).translate((0,height/2,))
part = part.cut(ellipse.translate((0,0,width+0.12-radius-0.18)))

cq.exporters.export(part, 'Ground_Truth.stl')