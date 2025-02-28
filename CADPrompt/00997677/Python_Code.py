import cadquery as cq

b_length:float = 1.5
b_width:float = 0.75
b_height:float = 0.034954

base:cq.Workplane = cq.Workplane("XY").box(b_length, b_width, b_height)

length:float = 0.35911
width:float = 0.581568
height:float =  0.699153
box:cq.Workplane = cq.Workplane("XY").box(length, width, height)
margin:float = 0.055864

part:cq.Workplane = (
    base
    .union(box.translate((-b_length/2 + length/2, b_width/2 - width/2 - margin, b_height/2 + height/2)))
    .union(box.translate((+b_length/2 - length/2, b_width/2 - width/2 - margin, b_height/2 + height/2)))
)

part = part.translate((0, 0, b_height/2))

cq.exporters.export(part, 'Ground_Truth.stl')