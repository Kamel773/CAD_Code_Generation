import cadquery as cq
from typing import List, Tuple

height:float = 0.103604
length:float = 0.725228

points:List[Tuple[float, float]] = [
    (0, 0),
    (length, 0),
    (0.932436, length/4 + 0.0155),
    (1.05676, length/2),
    (0.932436, length - (length/4 + 0.0155)),
    (0.725228, length),
    (0, length)
]

sketch:cq.Sketch = cq.Sketch().polygon(points)

part:cq.Workplane = (
    cq.Workplane("XY")
    .placeSketch(sketch)
    .extrude(height)
).translate((-length/2,0,0))

part = part.rotate((0,0,1),(0,0,0),-90).translate((-0.024772,0,0))
cq.exporters.export(part, 'Ground_Truth.stl')