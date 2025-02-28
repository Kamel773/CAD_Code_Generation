import cadquery as cq

length:float = 0.21429
width:float =  0.75
height:float =  0.21429

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

diameter:float = 0.05371
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(length, diameter/2).rotate((0,1,0),(0, 0, 0),90)

side_padding:float = 0.048699

part:cq.Workplane = (
    rec
    .cut(cylinder.translate((0,-width/2 + diameter/2 + side_padding,0)))
    .cut(cylinder.translate((0,width/2 - diameter/2 - side_padding,0)))
)

part = part.translate((length/2, width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')