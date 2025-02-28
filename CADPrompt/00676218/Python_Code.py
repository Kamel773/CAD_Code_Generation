import cadquery as cq

length:float = 1.5
width:float = 1.5
height:float = 0.023438
margin:float = 0.05625

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height)
    .faces("Z")
    .rect(length-margin*2,width-margin*2)
    .extrude(height)
)

part = part.translate((0,0,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')