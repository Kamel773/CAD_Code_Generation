import cadquery as cq
length:float = 0.03547
width:float = 1.27689
height:float = 0.14188

rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cut_width:float = 0.5677508
cut_height:float = 0.094585
cut_rectangle:cq.Workplane = cq.Workplane("XY").box(length, cut_width, cut_height)

padding:float = 0.047292

part:cq.Workplane = (
    rectangle
    .cut(cut_rectangle.translate((0,cut_width/2+padding/2,0)))
    .cut(cut_rectangle.translate((0,-(cut_width/2+padding/2),0)))
)

part = part.translate((length/2,-0.111555,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')