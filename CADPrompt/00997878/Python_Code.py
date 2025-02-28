import cadquery as cq

length:float = 0.448905
width:float = 0.75
height:float = 0.136861

box:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
)

c_length:float = 0.328467
c_width:float = 0.229927
fillet:float = (c_length - 0.29562)/2

cut_box:cq.Workplane = (
    cq.Workplane("XY")
    .box(c_length,c_width,height)
    .edges("|Z")
    .fillet(fillet)
)

space:float = 0.104015

part:cq.Workplane = (
    box
    .cut(cut_box.translate((0,c_width/2+space/2,0)))
    .cut(cut_box.translate((0,-c_width/2-space/2,0)))
)

part = part.translate((length/2,width/2,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')