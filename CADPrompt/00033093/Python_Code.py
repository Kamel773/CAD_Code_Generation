import cadquery as cq

length:float = 1.16102
width:float =  0.0729
height:float =  1.5

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

diameter:float = 0.072899
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(width, diameter/2).rotate((1,0,0),(0, 0, 0),90)

left_padding:float = 0.252909
right_padding:float = 0.127776
top_padding:float = 0.595655

part:cq.Workplane = (
    rec
    .cut(cylinder.translate((-length/2 + diameter/2 + left_padding, 0, height/2 - diameter/2 - top_padding)))
    .cut(cylinder.translate((length/2 - diameter/2 - right_padding, 0, height/2 - diameter/2 - top_padding)))
)

part = part.translate((0, -width/2, 0))
cq.exporters.export(part, 'Ground_Truth.stl')