import cadquery as cq

length:float = 1.05
width:float = 0.375
height:float = 0.9

box:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cut_length:float = 0.6
cut_width:float = 0.15
cut_box:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, height)

part:cq.Workplane = box.cut(cut_box.translate((0, -width/2 + cut_width/2, 0)))

part = part.translate((0, 0, height/2)).rotate((0, 0, 1),(0, 0, 0), -90).translate((-0.062655,-0.075414,0))
cq.exporters.export(part, 'Ground_Truth.stl')