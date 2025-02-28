import cadquery as cq

from typing import List,Tuple

length:float = 0.3
width:float = 0.1875 
height:float = 0.75
top_length:float = 0.225

top_x:float = (length - top_length)/2

points:List[Tuple[float, float]] = [
    (0, 0),
    (length, 0),
    (top_x + top_length, width),
    (top_x, width),
]

work:cq.Workplane = (
    cq.Workplane("XY")
    .center(-length/2,-width/2)
    .polyline(points).close()
)

part:cq.Workplane = work.extrude(height).translate((0.011705, 0.148443, 0))

cq.exporters.export(part, 'Ground_Truth.stl')