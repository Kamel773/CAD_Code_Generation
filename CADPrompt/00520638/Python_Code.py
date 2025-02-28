import cadquery as cq
from typing import List, Tuple

length:float = 1.10769
width:float = 0.474725
height:float = 0.18989
base:cq.Workplane = cq.Workplane("XY").box(length, width, height)

diameter:float = length / 2
padding:float = 0.056126 + 0.091513 +0.003033

r_top:cq.Workplane = cq.Workplane("XY").cylinder(width, diameter/2).rotate((1,0,0),(0,0,0),90)
connector:cq.Workplane = cq.Workplane("XY").box(diameter, width, diameter/2)

inner_diameter:float = 0.194358
inner_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(width, inner_diameter/2).rotate((1,0,0),(0,0,0),90)
inner_box:cq.Workplane = cq.Workplane("XY").box(inner_diameter, width, inner_diameter)

pts:List[Tuple[float, float]] = [
    (0, 0.316484),
    (-0.056, 0.483119),
    (length/2, 0.613244),
    (length/2, .434708)
]

arm:cq.Workplane = cq.Workplane("XY").polyline(pts).close().extrude(width)

part:cq.Workplane = (
    base
    .union(r_top.translate((-length/4,0,height/2 + diameter/2 - padding)))
    .union(connector.translate((-length/4, 0, height/2 + diameter/4 - padding)))
    .cut(inner_cylinder.translate((-length/2 + diameter/2 -0.033206, 0, height/2 + diameter/2 - padding-0.008798)))
    .cut(inner_box.translate((-length/2 + diameter/2 -0.033206,0, height/2 + diameter/2 - padding-0.008798 - inner_diameter/2)))
    .union(arm.rotate((1,0,0),(0,0,0),-90).translate((0, width/2, -height/2)))
)

part = part.rotate((0,1,0),(0,0,0),-90).translate((-0.658088+0.003033,-width/2,0))
cq.exporters.export(part, 'Ground_Truth.stl')