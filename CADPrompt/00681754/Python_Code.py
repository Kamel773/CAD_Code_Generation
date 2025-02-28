import cadquery as cq

length:float = 1.09115
width:float = 1.5
height:float = 0.361568
diameter:float = 0.427203
extrude:float = 0.271176

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("Z")
    .workplane()
    .circle(diameter/2)
    .extrude(extrude)
)

part = part.translate((0,0,height/2))


cq.exporters.export(part, 'Ground_Truth.stl')