import cadquery as cq
from typing import List,Tuple

base_height:float = 0.625913
base_length:float = 1.11043
base_top_length:float = 0.55953
base_width:float = 1.0011

base_pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, base_height),
    (base_top_length, base_height),
    (base_length, 0)
]

base_angle:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(base_pts)
    .close()
    .extrude(base_width)
)

side_height:float = 0.75
side_length:float = 1.27908
side_top_length:float = 0.619642
side_width:float = 0.201835

side_pts:List[Tuple[float, float]] = [
    (0, 0),
    (0, side_height),
    (side_top_length, side_height),
    (side_length, 0)
]

side_angle:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(side_pts)
    .close()
    .extrude(side_width)
)

part:cq.Workplane = base_angle.union(side_angle.translate((0,0,-side_width)))

part = part.translate((0,0,-base_width/4)).rotate((1,0,0),(0,0,0),-90).translate((-side_length/2-0.110211,0.149355,0))
cq.exporters.export(part, 'Ground_Truth.stl')