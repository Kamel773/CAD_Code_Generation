import cadquery as cq

b_length:float = 0.037173
b_width:float = 0.191178
b_height:float = 0.015931
s_height:float = 0.759401
base:cq.Workplane = (
    cq.Workplane("XY")
    .box(b_length, b_width ,b_height)
)

p_length:float = b_length
p_width:float = .015931
p_height:float = .764712
plank:cq.Workplane = cq.Workplane("XY").box(p_length, p_width, p_height)

part:cq.Workplane = (
    base
    .faces("Z")
    .workplane(offset = -b_height)
    .center(0,b_width/2-b_height/2)
    .rect(b_length,b_height)
    .extrude(s_height)
).add(plank.translate((0,-p_width/2,p_height/2)).rotate((1,0,0),(0,0,0),12).translate((0,-b_width/2+0.0173,b_height/2)))

part = part.translate((b_length/2+0.000301-0.00031,0.000301,-b_height/2-0.001009))

cq.exporters.export(part, 'Ground_Truth.stl')