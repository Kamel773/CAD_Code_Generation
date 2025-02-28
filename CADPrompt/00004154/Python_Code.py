import cadquery as cq

length:float = 0.70588
width:float =  0.40809
height:float = 0.22059
fillet:float = 0.08

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z")
    .fillet(fillet)
)

part = part.translate((length/2, width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')