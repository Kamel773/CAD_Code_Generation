import cadquery as cq

length:float = 0.42
width:float = 0.75
extrude:float = 0.015

part = cq.Workplane("XY").rect(length, width).extrude(extrude)

part = part.translate((length/2, width/2, -extrude)).rotate((0, 1, 0),(0, 0, 0), 90)
cq.exporters.export(part, 'Ground_Truth.stl')