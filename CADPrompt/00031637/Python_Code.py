import cadquery as cq

length:float = 1.05964
width:float = 0.56859
height:float =  0.26362

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cut_length:float = 0.206758
cut_height:float = 0.186082
cut_rec:cq.Workplane = cq.Workplane("XY").box(cut_length, width, cut_height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rec)
    .cut(cut_rec.translate((-length/2 + cut_length/2, 0, height/2 - cut_height/2)))
)

part = part.translate((-0.220185, 0.058181, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')