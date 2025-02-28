import cadquery as cq

length:float = 0.75
width:float = 0.5
height:float = 0.375

diameter:float = 0.5357

box:cq.Workplane = cq.Workplane("XY").box(length, width, height)
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

part:cq.Workplane = box.cut(cylinder.translate((0,width/2,0)))

part = part.translate((0,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')