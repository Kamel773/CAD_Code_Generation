import cadquery as cq

length:float = 0.337772
width:float = 0.75
height:float = 0.021792

box:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cut_margin:float = 0.01816
cut_length:float = length - cut_margin*2
cut_width:float = width - cut_margin
cut_box:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, height)

part:cq.Workplane = box.cut(cut_box.translate((0,cut_margin/2,0)))

part = part.translate((-length/2,width/2,0))
cq.exporters.export(part, 'Ground_Truth.stl')