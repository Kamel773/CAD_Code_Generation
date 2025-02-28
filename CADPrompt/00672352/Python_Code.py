import cadquery as cq
length:float = 0.75
width:float = 0.375
height:float = 0.015611

diameter:float = 0.09375
padding:float = 0.015625
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height)
    .cut(cylinder.translate((length/2-diameter/2-padding,+width/2-diameter/2-padding,0)))
)

part = part.translate((-length/2,-width/2,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')