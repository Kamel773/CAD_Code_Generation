import cadquery as cq
from typing import List,Tuple

height:float = 0.32592
length:float = 0.75
top_length:float = 0.280098
width:float = 0.023387

pts:List[Tuple[float, float]] = [
    (0,0),
    (0,height),
    (top_length,height),
    (length,0)
]

angle:cq.Workplane = (
    cq.Workplane("ZY")
    .polyline(pts)
    .close()
    .extrude(width)
)

part:cq.Workplane = angle.rotate((0,0,1),(0,0,0),180)
cq.exporters.export(part, 'Ground_Truth.stl')