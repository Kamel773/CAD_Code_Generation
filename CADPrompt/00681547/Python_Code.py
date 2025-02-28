import cadquery as cq
from typing import List,Tuple

box_length:float = 0.043025
box_width:float = 0.985934
box_height:float = 1.39258
box:cq.Workplane = cq.Workplane("XY").box(box_length,box_width,box_height)

corner_length:float = box_height - 1.19693
corner_width:float = (box_width - 0.563939)/2

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

part = part.rotate((0,1,0),(0,0,0),90).rotate((0,0,1),(0,0,0),-90).translate((0.157289,0.05371,box_length/2))

cq.exporters.export(part, 'Ground_Truth.stl')