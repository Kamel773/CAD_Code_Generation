import cadquery as cq

length:float = 1.5
width:float =  0.40625
height:float =  0.023438

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

diameter:float = 0.046875
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height,diameter/2)

side_padding:float = 0.048699

width_padding:float = 0.039062
left_padding:float = 0.242188
right_padding:float = 0.242228

part:cq.Workplane = (
    rec
    .cut(cylinder.translate((length/2-diameter/2-left_padding,-width/2+diameter/2+width_padding,0)))
    .cut(cylinder.translate((-length/2+diameter/2+right_padding,-width/2+diameter/2+width_padding,0)))
    .cut(cylinder.translate((0,width/2-diameter/2-width_padding,0)))
)


part = part.translate((0, 0, height/2))


cq.exporters.export(part, 'Ground_Truth.stl')