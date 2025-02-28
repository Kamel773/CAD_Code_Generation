import cadquery as cq

length:float = 1.125
width:float = 1.5
height:float = 0.06

inner_length:float = 0.3825
inner_width:float = 0.7575
inner_depth:float = 0.03

box:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("Z")
    .rect(inner_length, inner_width)
    .extrude(-inner_depth, combine="cut")
)

part:cq.Workplane = box.translate((0, 0, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')