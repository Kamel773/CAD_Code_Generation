import cadquery as cq

length:float = 0.75
width:float =  0.042
height:float =  0.0018

rec:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("Z")
    .workplane()
    .center(0,width/2-0.0228/2)
    .rect(length,0.0228)
    .extrude(0.0192)
    .faces(">Z")
    .workplane()
    .center(0,0.0228/2-0.021/2)
    .rect(length, 0.021)
    .extrude(0.015)
)

part:cq.Workplane = rec.translate((-length/2,-width/2,height/2)).rotate((0,0,1),(0,0,0),-90)


cq.exporters.export(part, 'Ground_Truth.stl')