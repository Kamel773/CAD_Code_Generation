import cadquery as cq

length:float = 1.5
width:float = 1.5
height:float = 0.0255

square:cq.Workplane = cq.Workplane("XY").box(length, width, height)

empty_length:float = 0.12
empty_width:float = 0.24
empty_rectangle:cq.Workplane = cq.Workplane("XY").box(empty_length, empty_width, height)

part:cq.Workplane = square.cut(empty_rectangle)

part = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')