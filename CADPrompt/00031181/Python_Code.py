import cadquery as cq

length:float = 0.61135
width:float = 0.36026
height:float =  0.33843

part:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part = part.translate((length/2, width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')