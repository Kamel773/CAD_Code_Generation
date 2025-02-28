import cadquery as cq

length:float = 0.5
width:float = 0.5
height:float = 0.633333

rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cylinder_height:float = 0.116667
diameter:float = 0.316667
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cylinder_height, diameter/2)

cut_length:float = length - 0.044167*2
cut_width:float = width - 0.044167*2
cut_height:float = height - 0.1
cut_rectangle:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, cut_height)

padding:float = 0.118359
part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rectangle)
    .union(cylinder.translate((0,0,(height/2+cylinder_height/2))))
    .cut(cut_rectangle.translate((0,0,-0.1/2)))
)

part = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')