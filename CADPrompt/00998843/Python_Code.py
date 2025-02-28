import cadquery as cq
length = 0.5
width = 0.75
height = 0.15

base = cq.Workplane("XY").box(length, width, height)

s_length = 0.35
s_height = 0.15
diameter = 0.2


part = (
    base
    .faces("Z")
    .workplane()
    .center(length/2-s_length/2,0)
    .rect(s_length, width)
    .extrude(s_height)
    .faces(">Z")
    .workplane()
    .circle(diameter/2)
    .extrude(-(height+s_height),combine="cut")
)

part = part.translate((length/2,width/2,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')