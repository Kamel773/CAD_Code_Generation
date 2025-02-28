import cadquery as cq
length:float = 1.5
width:float = 1.5
extrude:float = 0.75

part:cq.Workplane = (
    cq.Workplane("XY" )
    .rect(length, width)
    .extrude(extrude)
)

part = part.translate((0, 0, -extrude/2))
cq.exporters.export(part, 'Ground_Truth.stl')