import cadquery as cq
from typing import List, Tuple

length:float = 0.886095
width:float = 0.354438
offset:float = 0.6147
extrude:float = .425326

points:List[Tuple[float, float]] = [
    (offset + 0, 0),
    (length + offset, 0),
    (length, width),
    (0, width)
]

sketch:cq.Sketch = cq.Sketch().polygon(points)

cut_length:float = 0.306589
cut_width:float = 0.25874
cut_box:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, extrude)

part:cq.Workplane = (
    cq.Workplane("XY")
    .placeSketch(sketch)
    .extrude(extrude)
    .translate((-(length + offset)/2, -width/2, -extrude/2))
    .cut(cut_box)
).rotate((1,0,0),(0,0,0), 90)

part = part.translate((0,-extrude/2,0))
cq.exporters.export(part, 'Ground_Truth.stl')