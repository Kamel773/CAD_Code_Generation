import cadquery as cq

length:float = 0.59437
width:float =  0.44577
height:float = 0.37148

part:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cq.exporters.export(part, 'Ground_Truth.stl')