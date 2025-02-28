import cadquery as cq

sides:int = 6
length:float = 1.5
extrude:float = 0.016238

part:cq.Workplane = cq.Workplane("XY").polygon(sides, length).extrude(extrude)

cq.exporters.export(part, 'Ground_Truth.stl')