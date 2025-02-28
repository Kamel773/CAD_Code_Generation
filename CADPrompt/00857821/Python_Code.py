import cadquery as cq
from typing import List, Tuple

diameter:float = 0.374906
height:float = 0.1875

pts:List[Tuple[float,float]] = [
    (0,0),
    (0,diameter),
    ((diameter*.7) + 0.01883 - 0.0001 ,diameter)
]

cylinder:cq.Sketch = (
    cq.Sketch()
    .push([(diameter/2,diameter*2 - 0.187124)])
    .circle((diameter/2))
    .push([(0,0)])
    .polygon(pts)
    .wires()
    .hull()
)

half:cq.Workplane = cq.Workplane("XY").placeSketch(cylinder).extrude(height).translate((0,0,-height/2))
part:cq.Workplane = (
    cq.Workplane("XY")
    .union(half)
    .union(half.rotate((0,1,0),(0,0,0),180))
)

part = part.translate((0,0,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')