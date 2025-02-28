import cadquery as cq

length:float = 1.5
width:float = 1.5
height:float = 0.655147
fillet:float = (1.5 - 1.18553)/2

inner_length:float = 1.44759
inner_width:float = 1.44759
height:float = 0.655147
inner_fillet:float = (inner_length - 1.18553)/2

box:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z")
    .fillet(fillet)
)

cut_box:cq.Workplane = (
    cq.Workplane("XY")
    .box(inner_length, inner_width, height)
    .edges("|Z")
    .fillet(inner_fillet)
)

part:cq.Workplane = box.cut(cut_box)

part = part.translate((0, 0, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')