import cadquery as cq
from typing import List,Tuple

plate_length:float = 0.75
plate_width:float = 0.605769
plate_height:float = 0.018035
plate:cq.Workplane = cq.Workplane("XY").box(plate_length, plate_width, plate_height)

length:float = 0.432692
width:float = 0.028846 
height:float = plate_height
top_length:float = 0.375

top_x:float = (length - top_length)/2

points:List[Tuple[float, float]] = [
    (0,0),
    (top_x, width),
    (top_x + top_length, width),
    (length, 0)
]

outline:cq.Workplane = (
    cq.Workplane("XY").center(-(length/2),-(width/2))
    .polyline(points).close()
)

trapezoid:cq.Workplane = outline.extrude(height).rotate((0,0,1),(0,0,0),90)
tab_offset:float = 0.030288

part:cq.Workplane = plate.union(trapezoid.translate((plate_length/2+width/2,-plate_width/2+length/2+tab_offset,-height/2)))

part = part.translate((-plate_length/2,plate_width/2,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')