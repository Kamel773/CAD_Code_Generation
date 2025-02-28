import cadquery as cq

h_length:float = 1.15342
h_height:float = 0.249723
hexagon:cq.Workplane = (
    cq.Workplane("XY")
    .polygon(6, h_length)
    .extrude(h_height)
)

hex_loc:cq.Location = hexagon.faces(">Z").workplane().plane.location

smh_length:float = 0.865066
smh_height:float = 0.199778
sm_hexagon:cq.Workplane = (
    cq.Workplane("XY",obj=hex_loc)
    .polygon(6, smh_length)
    .extrude(smh_height)
)

sm_loc:cq.Location = sm_hexagon.faces(">Z").workplane().plane.location

tiny_length:float = 0.576711
tiny_height:float = 0.099889
tiny_hexagon:cq.Workplane = (
    cq.Workplane("XY",obj=sm_loc)
    .polygon(6, tiny_length)
    .extrude(tiny_height)
)

tiny_loc:cq.Location = tiny_hexagon.faces(">Z").workplane().plane.location

tri_length:float = 0.342081*2 / 1.50000126581958
tri_height:float = 0.079911
triangle:cq.Workplane = (
    cq.Workplane("XY", obj=tiny_loc)
    .polygon(3, tri_length)
    .extrude(tri_height)
)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(hexagon.rotate((0,0,1),(0,0,0),90 - 0.530932))
    .union(sm_hexagon.rotate((0,0,1),(0,0,0),-45/2 + 6.5675))
    .union(tiny_hexagon.rotate((0,0,1),(0,0,0),45/4 + 1.19))
    .union(triangle.translate((-0.000379 + 0.008291 - 0.001416 - 0.001224,-0.000537 + 0.023766 - 0.001249 ,0)).rotate((0,0,1),(0,0,0),45/8 + -23.133 - 0.02))
).rotate((0,1,0),(0,0,0),180)

cq.exporters.export(part, 'Ground_Truth.stl')