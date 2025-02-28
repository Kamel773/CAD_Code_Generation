import cadquery as cq

length:float = 1.1056
width:float =  1.22951
height:float =  0.122951
sub_length:float = length + 0.19721*2
sub_width:float = 0.368852


rec:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .box(sub_length,sub_width,height)
)

part:cq.Workplane = rec.translate((0,0,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')