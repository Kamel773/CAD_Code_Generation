import cadquery as cq

length:float = 1.5
width:float = 0.004152
height:float = 0.720946
fillet:float = length - 1.34429

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Y")
    .fillet(fillet/2)
)

part = part.translate((0,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')