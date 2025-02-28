import cadquery as cq
from typing import List,Tuple

box_length:float = 0.75
box_height:float = 0.704219
bottom_padding:float =  0.329992
height:float = box_height - 0.329992
length:float = 0.280836
top_length:float = box_length - 0.187163

width:float = 0.664347

pts:List[Tuple[float, float]] = [
    (0,0),
    (0,height),
    (top_length,height),
    (length,0)
]

angle:cq.Workplane = (
    cq.Workplane("XZ")
    .polyline(pts)
    .close()
    .extrude(width)
).rotate((0,0,1),(0,0,0),180).translate((top_length-box_length/2+0.187163,-width/2,-box_height/2+bottom_padding))

box:cq.Workplane = cq.Workplane("XY").box(box_length,width,box_height)

part:cq.Workplane = box.cut(angle)
part = part.translate((box_length/2,width/2,-box_height/2))

cq.exporters.export(part, 'Ground_Truth.stl')