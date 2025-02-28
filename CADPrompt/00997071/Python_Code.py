import cadquery as cq

length:float = 0.636792
width:float =  0.56638
height:float =  0.099057

sub_length:float = length + 0.113207*2
sub_width:float = 0.141509

diameter:float = 0.318396

rec:cq.Workplane = (
    cq.Workplane("YZ")
    .box(length, width, height)
    .box(sub_length, sub_width, height)
    .cylinder(height, diameter/2, combine="cut")
)

part = rec.translate((height/2,length/2,width/2))

cq.exporters.export(part, 'Ground_Truth.stl')