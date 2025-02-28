import cadquery as cq

length:float = 0.982759
width:float = 0.124138
height:float = 0.827586

b_height:float = 0.672414
b_length:float = 0.444828

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("-Z")
    .workplane()
    .rect(b_length,width)
    .extrude(b_height)
)


part = part.translate((0,width/2,height/2-0.077586))

cq.exporters.export(part, 'Ground_Truth.stl')