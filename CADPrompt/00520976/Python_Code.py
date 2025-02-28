import cadquery as cq

length:float = 0.75
width:float = 0.25
height:float = 0.75

part:cq.Workplane = cq.Workplane("XY").box(length, width, height).faces("Z").edges(">X").box(.5,.25,.5, combine ="cut")

part = part.translate((-length/2,-width/2,-height/2))
cq.exporters.export(part, 'Ground_Truth.stl')