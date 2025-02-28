import cadquery as cq
from typing import List,Tuple

box_length:float = 0.051687
box_width:float = 0.120604
box_height:float = 0.75
box:cq.Workplane = cq.Workplane("XY").box(box_length,box_width,box_height)

corner_length:float = 0.052223
corner_width:float = 0.030151

pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, corner_width),
    (corner_length, 0)
]

corner:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(box_length)
    .rotate((0,1,0),(0,0,0),-90)
    .translate((-box_length/2,-corner_width/2,corner_length/2))
)

part:cq.Workplane = (
    box
    .cut(corner.translate((0,-box_width/2+corner_width/2,box_height/2-corner_length/2)))
    .cut(corner.translate((0,-box_width/2+corner_width/2,box_height/2-corner_length/2)).rotate((0,0,1),(0,0,0),180))
)

part = part.translate((box_length/2,box_width/2,box_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')