import cadquery as cq

length:float = 1.5
width:float =  0.83721
height:float = 0.07849

part:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')