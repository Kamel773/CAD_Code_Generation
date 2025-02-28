import cadquery as cq
from typing import List,Tuple

pts:List[Tuple[float, float]] = [
    (0, 0.07722659),
    (0.01489577, 0.03904715),
    (0.07129721, 0.03904715),
    (0.01778815, 0.01070181),
    ( 0.05105054, -0.0378901),
    (0, -0.0083879),
    (-0.0539429, -0.03470857),
    (-0.02183747, 0.006074),
    (-0.07071871, 0.02429601),
    (-0.01865585, 0.036444),
    (0.0, 0.0772265)

]

star:cq.Workplane = (
    cq.Workplane("XZ")
    .polyline(pts)
    .close()
    .extrude(0.0634998086654784)
    
)

star = star.val().scale(9.711714302145034) #type:ignore

part:cq.Workplane = star

cq.exporters.export(part, 'Ground_Truth.stl')