import cadquery as cq

height:float = 0.75
outer_diameter:float = 0.078575
inner_diameter:float = 0.058318

ellipse_diameter:float = 0.078654

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, outer_diameter/2)
inner_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, inner_diameter/2)

ellipse:cq.Workplane = cq.Workplane().cylinder(1, ellipse_diameter/2).rotate((0,1,0),(0,0,0),90)

part:cq.Workplane = (
    cylinder
    .cut(inner_cylinder)
    .cut(ellipse.translate((1/2,-.002,.001867)))
    .translate((0,0,height/2))
)

part = part.rotate((0,0,1),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')