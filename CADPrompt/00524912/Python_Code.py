import cadquery as cq

lg_length:float = 0.416808
lg_width:float = 0.033235
lg_height:float = 0.75
lg_box:cq.Workplane = cq.Workplane("XY").box(lg_length, lg_width, lg_height)

sm_length:float = 0.211685
sm_width:float = 0.065736
sm_height:float = 0.411987
sm_box:cq.Workplane = cq.Workplane("XY").box(sm_length,sm_width,sm_height).rotate((0,0,1),(0,0,0),90)


where_to_find_padding:float = 0.0065309

part:cq.Workplane =(
    cq.Workplane("XY")
    .union(lg_box)
    .union(sm_box.translate((-lg_length/2+sm_width/2,-sm_length/2-lg_width/2,where_to_find_padding)))
)

part = part.translate((-lg_length/2,lg_width/2,lg_height/2)).rotate((0,0,1),(0,0,0),180)
cq.exporters.export(part, 'Ground_Truth.stl')