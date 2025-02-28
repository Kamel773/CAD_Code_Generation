import cadquery as cq

diameter:float = 0.979642
inner_diameter:float = diameter - 0.170198*2
height:float = 0.006808

cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
)

cut_cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, inner_diameter/2)
)

part = (
    cq.Workplane("XY")
    .union(cylinder.translate((-0.260308,0,0)))
    .union(cylinder.translate((0.260308,0,0)))
    .cut(cut_cylinder.translate((-0.260308,0,0)))
    .cut(cut_cylinder.translate((0.260308,0,0)))
)

cq.exporters.export(part, 'Ground_Truth.stl')