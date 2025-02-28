import cadquery as cq

base_length:float = 0.75
base_width:float = 0.658737
base_height:float = 0.284211
base:cq.Workplane = cq.Workplane("XY").box(base_length,base_width,base_height)

top_length:float = 0.347368
top_width:float = base_width
top_height:float = 0.135789
top:cq.Workplane = cq.Workplane("XY").box(top_length,top_width,top_height)

part:cq.Workplane = base.union(top.translate((base_length/2-top_length/2,0,base_height/2+top_height/2)))

part = part.translate((base_length/2,0,base_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')