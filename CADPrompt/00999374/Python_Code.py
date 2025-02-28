import cadquery as cq
from typing import List,Tuple

pts = [
    (-0.215997 , -0.071707),
    ((0.283196/2)-0.086266, (-0.571139/2)+0.128415),
    ((0.283196/2)+0.154673, (0.571139/2)-0.103869),
    ((0.283196/3)-0.094331, (0.571139)-0.45031)
]

extrude = 0.493701

pick = (
    cq.Workplane("XY")
    .polyline(pts)
    .close()
    .extrude(extrude)
)

handle = cq.Workplane("XY").box( 0.1323,0.78659, 0.203642).rotate((0,0,1),(0,0,0),-41.7).translate((0.223543 ,-0.361526,0.301748))

part = pick.union(handle)


cq.exporters.export(part, 'Ground_Truth.stl')