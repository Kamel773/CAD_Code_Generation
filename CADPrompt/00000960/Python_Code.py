import cadquery as cq

length:float = 0.75
width:float = 0.75
height:float = 0.00195

box = cq.Workplane("XY").box(length, width, height)

cut_one_length:float = 0.281257
cut_one_width:float = 0.0625
cut_one = cq.Workplane("XY").box(cut_one_length, cut_one_width, height)

cut_two_length:float = 0.25
cut_two_width:float = 0.333333
cut_two = cq.Workplane("XY").box(cut_two_length, cut_two_width, height)

part:cq.Workplane = (
    box
    .cut(cut_one.translate((length/2-cut_one_length/2, width/2-cut_one_width/2,0)))
    .cut(cut_two.translate((length/2-cut_two_length/2, -width/2+cut_two_width/2,0)))
)

part = part.rotate((0, 0, 1),(0, 0, 0), 180).translate((length/2, width/2, 0))
cq.exporters.export(part,'Ground_Truth.stl')