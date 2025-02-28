import cadquery as cq
from typing import List,Tuple

height:float = 0.545455/2
length:float = 0.477273
top_length:float = 0.204545
width:float = 0.75

pts:List[Tuple[float, float]] = [
    (0,0),
    (0, height),
    (top_length, height),
    (length, 0)
]

angle:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(width)
)

part:cq.Workplane = angle.union(angle.rotate((1,0,0),(0,0,0),180).translate((0,0,width)))

part = part.rotate((0,1,0),(0,0,0),90).rotate((0,0,1),(0,0,0),180)
cq.exporters.export(part, 'Ground_Truth.stl')