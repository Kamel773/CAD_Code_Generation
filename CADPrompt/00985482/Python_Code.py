import cadquery as cq
from typing import List,Tuple

length:float = 0.75
width:float = 0.340821
extrude:float = 0.031444
frame_size:float = 0.047166
right_margin:float = 0.16366
left_margin:float = 0.17824 - 0.060417

pts:List[Tuple[float, float]] = [
    (0,0),
    (length,0),
    (length-right_margin,width),
    (0+left_margin,width)
    
]

part:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(extrude)
    .faces("-Z")
    .edges()
    .toPending()
    .offset2D(-frame_size)
    .extrude(extrude, combine="cut")
)

cq.exporters.export(part, 'Ground_Truth.stl')