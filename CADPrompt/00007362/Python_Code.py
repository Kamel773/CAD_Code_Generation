import cadquery as cq

length:float = 0.75
width:float = 0.06429
height:float = 0.03929

part:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part = part.translate((length/2, -width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')