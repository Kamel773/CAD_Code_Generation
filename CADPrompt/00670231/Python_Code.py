import cadquery as cq
length:float = 0.9
width:float = 1.5
height:float = 0.75
diameter:float = 0.45
offset:float = 0.075

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .cut(cylinder.translate((-length/2 + diameter/2 + offset, 0, 0)))
)

part = part.translate((0.15, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')