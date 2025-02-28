import cadquery as cq

base_length:float = 0.307377
base_width:float = 0.307377
base_height:float = 0.012295
base:cq.Workplane = cq.Workplane("XY").box(base_length, base_width, base_height)

plinth_length:float = 0.307377
plinth_width:float = 0.184426
plinth_height:float = 0.737705
plinth:cq.Workplane = cq.Workplane("XY").box(plinth_length, plinth_width, plinth_height)

part:cq.Workplane = base.union(plinth.translate((0, 0, base_height/2 + plinth_height/2)))

part = part.translate((0,0,base_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')