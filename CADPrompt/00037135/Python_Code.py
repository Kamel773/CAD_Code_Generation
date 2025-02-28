import cadquery as cq
from typing import List,Tuple

pts:List[Tuple[float, float]] = [
    (-0.05430806, 0.05735744),
    (-0.05430806, -0.05851911),
    (-0.04704762, -0.05851911),
    (-0.0383351, -0.00217813),
    (0.00232334, -0.00217813),
    (0.0116167, -0.06200412),
    (0.01742505, -0.06200412),
    (0.01452087, 0.01030982),
    (-0.02875133, 0.01030982),
    (-0.0450147, 0.05735744),
    (-0.05430806, 0.05735744)
]

bench:cq.Workplane = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(0.10160000000000001)
)

bench = bench.val().scale(7.38186180173805) #type:ignore

part = bench.rotate((1,0,0),(0,0,0),-90).rotate((0,0,1),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')