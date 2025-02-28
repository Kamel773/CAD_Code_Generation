import cadquery as cq
from typing import List,Tuple

box_length:float = 0.747683
box_width:float = 0.747683
box_height:float = 0.747683
box:cq.Workplane = cq.Workplane("XY").box(box_length, box_width, box_height)

triangle_length:float = 0.498375
triangle_width:float = 0.498375
triangle_extrude:float = box_length

pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, triangle_width),
    (triangle_length ,0)
]
triangle:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(triangle_extrude)
)

part:cq.Workplane = (
    box
    .union(triangle.rotate((0,1,0),(0,0,0),90).translate((-box_length/2, -box_width/2, -box_height/2)))
)

part = part.translate((box_length/2, -box_width/2, box_height/2)).rotate((0, 0, 1),(0, 0, 0),180)
cq.exporters.export(part, 'Ground_Truth.stl')