import cadquery as cq

length:float = 1.5
width:float =  1.37143
height:float =  0.078171

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

groove_length:float = 0.085714
groove_height:float = 0.042857
groove_left:float = 0.685714
groove = cq.Workplane("XY").box(groove_length,width,groove_height)

part:cq.Workplane = (
    rec
    .cut(groove.translate((length/2-groove_length/2-groove_left,0,height/2-groove_height/2)))
)

part = part.translate((0,0, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')