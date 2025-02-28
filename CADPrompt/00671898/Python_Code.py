import cadquery as cq
from typing import List,Tuple

length:float = 0.676776
peak_one:float = 0.102138
trough_one:float = 0.059507
peak_two:float = 0.135891
trough_two:float = 0.05773
peak_three:float = 0.089704
width:float = 0.20312
extrude:float = 0.75

pts:List[Tuple[float, float]] = [
    (0,0),
    (length,0),
    (length,peak_one),
    (length-0.18862+0.000331,trough_one),
    (length/2+0.000888,peak_two),
    (0.214957,trough_two),
    (0.032084-0.000111,peak_three)
]

part:cq.Workplane = (
    cq.Workplane("XZ")
    .polyline(pts)
    .close()
    .extrude(extrude)
)

part = part.translate((-length/2+0.026645,0,0))
cq.exporters.export(part, 'Ground_Truth.stl')