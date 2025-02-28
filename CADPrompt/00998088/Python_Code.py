import cadquery as cq

length:float = 1.5
width:float = 0.413793
height:float = 0.031034
fillet:float = 0.025

box:cq.Workplane = cq.Workplane("XY").box(length, width, height)

c_length:float = (length - 1.28276)/2
c_width:float = width - 0.31034
corner_cut:cq.Workplane = (
    cq.Workplane("XY")
    .box(c_length, c_width, height)
    .faces("X")
    .edges("<Y")
    .fillet(fillet)
)

part:cq.Workplane = (
    box
    .cut(corner_cut.translate((-length/2+c_length/2,width/2-c_width/2,0)))
    .cut(corner_cut.rotate((0,1,0),(0,0,0),180).translate((length/2-c_length/2,width/2-c_width/2,0)))
)

part = part.translate((0,width/2,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')