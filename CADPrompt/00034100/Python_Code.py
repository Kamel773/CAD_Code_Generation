import cadquery as cq

length:float = 0.47368
width:float =  0.31579
height:float =  0.75

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

diameter:float = 0.196206
top_padding:float = 0.146132
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(width,diameter/2).rotate((1,0,0),(0, 0, 0),90)


cut_rec_length:float = 0.007895
cut_rec_height = top_padding + 0.05
cut_rec:cq.Workplane = cq.Workplane("XY").box(cut_rec_length, width, cut_rec_height)

part:cq.Workplane = (
    rec
    .cut(cylinder.translate((0, 0, height/2 - diameter/2 - top_padding)))
    .cut(cut_rec.translate((0, 0, height/2 - cut_rec_height/2)))
)

part = part.translate((0, -width/2, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')