import cadquery as cq

length:float = 0.475652
width:float = 0.049547
height:float = 0.317101

b_height:float = 0.198188
b_length:float = length
b_width:float = 0.049547

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("-Y")
    .workplane()
    .center(0,0.000515)
    .rect(b_length,b_height)
    .extrude(b_width)
)

part = part.translate((-length/2,width/2+b_width+0.011569,0)).rotate((0,0,1),(0,0,0),-90)


cq.exporters.export(part, 'Ground_Truth.stl')