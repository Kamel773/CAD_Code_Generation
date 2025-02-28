import cadquery as cq

base_height:float = 0.75
base_diameter:float = 0.470339
base_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(base_height, base_diameter/2)

mid_height:float = 0.082627
mid_diameter:float = 0.152542
mid_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(mid_height, mid_diameter/2)

top_height:float = 0.190678
top_diameter:float = 0.075981
top_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(top_height, top_diameter/2)

padding:float = 0.247881

part:cq.Workplane = (
    cq.Workplane("XY")
    .add(base_cylinder.translate((0,0,0)))
    .add(mid_cylinder.translate((-base_diameter/2 + mid_diameter/2 + padding, 0, base_height/2 + mid_height/2)))
    .add(top_cylinder.translate((-base_diameter/2 + mid_diameter/2 + padding, 0 ,base_height/2 + mid_height + top_height/2)))
)

part = part.translate((0,0,-base_height/2)).rotate((0,1,0),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')