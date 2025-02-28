import cadquery as cq
length:float = 0.02812
width:float = 0.02812
extrude:float = 0.75

part:cq.Workplane = (
    cq.Workplane("XY" )
    .rect(length, width)
    .extrude(extrude)
)

part = part.translate((length/2, width/2, 0))
cq.exporters.export(part, 'Ground_Truth.stl')