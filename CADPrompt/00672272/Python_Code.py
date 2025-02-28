import cadquery as cq
length:float = 0.647727
width:float = 0.051136
height:float = 0.025568

sub_length:float = 0.75
sub_height:float = 0.008523

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height)
    .box(sub_length,width,sub_height)
)

part = part.translate((sub_length/2,-width/2,sub_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')