import cadquery as cq

sides:int = 8
length:float = 1.00328
extrude:float = 0.271665

part:cq.Workplane = cq.Workplane("XY").polygon(sides, length).extrude(extrude)

part = part.rotate((0,0,1),(0,0,0),22.4).rotate((1,0,0),(0,0,0),-90).translate((-0.176576,0,0.286546))
cq.exporters.export(part, 'Ground_Truth.stl')