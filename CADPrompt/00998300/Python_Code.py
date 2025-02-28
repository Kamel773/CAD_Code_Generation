import cadquery as cq

length:float = 0.036
width:float = 0.0135
height:float = 0.9

post:cq.Workplane = cq.Workplane("XY").box(length, width, height)

s_length:float = 0.24
s_height:float = 0.036
sign:cq.Workplane = cq.Workplane("XY").box(s_length, width, s_height)

part:cq.Workplane = post.union(sign.translate((-length/2-s_length/2,0,height/2-s_height/2-0.15)))
part = part.translate((length/2,-width/2,-height/2+0.15)).rotate((0,0,1),(0,0,0),-90)

cq.exporters.export(part, 'Ground_Truth.stl')