import cadquery as cq
from typing import List,Tuple

box_length:float = 0.525
box_width:float = 0.75
box_height:float = 0.1125

box:cq.Workplane = cq.Workplane("XY").box(box_length, box_width, box_height)

length:float = 0.3
width:float = 0.589754
height:float = box_height
top_length:float = 0.525

top_x:float = (length - top_length)/2

points:List[Tuple[float, float]] = [
    (0,0),
    (top_x,height),
    (top_x+top_length,height),
    (length,0)
]

trap:cq.Workplane = (
    cq.Workplane("XZ")
    .polyline(points).close()
    .extrude(box_width)
)

part:cq.Workplane = box.union(trap.translate((-length/2,box_width/2,height/2)))

part = part.translate((-0.022628,-box_width/2,-box_height/2-0.015833))


cq.exporters.export(part, 'Ground_Truth.stl')