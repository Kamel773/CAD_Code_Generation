import cadquery as cq

length:float = 0.75
width:float = 0.5
height:float = 0.25

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("Z")
    .workplane()
    .center(height/2,0)
    .rect(length-height,width)
    .extrude(height)
    .faces(">Z")
    .workplane()
    .center(height/2,0)
    .rect(length-height*2,width)
    .extrude(height)
)

part = part.translate((length/2,-width/2,-0.020659))

cq.exporters.export(part, 'Ground_Truth.stl')