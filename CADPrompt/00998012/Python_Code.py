import cadquery as cq

length = 0.9375
width = 1.5
height = 0.375

base = (
    cq.Workplane("XY")
    .box(length, width, height)
)

a_length = 0.234375
a_height = 0.328125
arm = cq.Workplane("XY").box(a_length, length, a_height)

part = (
    base
    .union(arm.translate((-length/2+a_length/2,width/2-length/2,height/2+a_height/2)))
    .union(arm.rotate((0,0,1),(0,0,0),90).translate((0,width/2-a_length/2,height/2+a_height/2)))
)

part = part.translate((0,0,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')