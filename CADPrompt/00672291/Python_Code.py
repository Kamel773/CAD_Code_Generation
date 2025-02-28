import cadquery as cq

length:float = 0.75
width:float = 0.015
height:float = 0.3

top_width:float = 0.15
top_height:float = width

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height)
    .faces("Z")
    .workplane(offset=-top_height/2)
    .center(0,top_width/2-width/2)
    .box(length,top_width,top_height)
)

part = part.translate((length/2,width/2,-height/2))
cq.exporters.export(part, 'Ground_Truth.stl')