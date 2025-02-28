import cadquery as cq

length:float = 0.058594
width:float = 0.75
height:float = 0.216797
fillet:float = 0.216797 - 0.1875

box:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("Z").edges("X").fillet(fillet)
)

part:cq.Workplane = box

part = part.translate((length/2, width/2, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')