import cadquery as cq

base_height:float = 0.681818
base_diameter:float = 0.681818
base_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(base_height, base_diameter/2)

mid_height:float = 0.252273
mid_diameter:float = 1.5
mid_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(mid_height, mid_diameter/2)

top_height:float = 0.068182
top_diameter:float = 0.681818
top_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(top_height, top_diameter/2)

padding:float = 0.247881

part:cq.Workplane = (
    cq.Workplane("XY")
    .add(base_cylinder.translate((0,0,0)))
    .add(mid_cylinder.translate((0,0,base_height/2+mid_height/2)))
    .add(top_cylinder.translate((0,0,base_height/2+mid_height+top_height/2)))
)

part = part.translate((0,0,-base_height/2)).rotate((0,1,0),(0,0,0),-90)
part = part.rotate((0,1,0),(0,0,0),90)


cq.exporters.export(part, 'Ground_Truth.stl')