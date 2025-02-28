import cadquery as cq

length:float = 1
width:float = 0.1
height:float = 1.25

cut_length:float = 0.5
cut_height:float = 0.075
cut_rectangle:cq.Workplane = cq.Workplane("XY").box(cut_length, width, cut_height)
bottom_padding:float = 0.25

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .cut(cut_rectangle.translate((0,0,-height/2+cut_height/2+bottom_padding)))
)

part = part.translate((0,-width/2,-0.125))
cq.exporters.export(part, 'Ground_Truth.stl')