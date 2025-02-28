import cadquery as cq

length:float = 0.192347
width:float = 0.592709
height:float = 0.029536
diameter:float = 0.358436

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

handle:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
)

cut_diameter:float = 0.052367
cut_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, cut_diameter/2)
cut_spacer:float = 0.048552
overlap:float = 0.02193

handle:cq.Workplane = handle.cut(cut_cylinder.translate((0,width/2-cut_diameter/2-cut_spacer,0)))

part:cq.Workplane = (
    cylinder
    .union(handle.translate((0,diameter/2+width/2-overlap,0)))
)

part = part.translate((0,0,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')