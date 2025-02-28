import cadquery as cq

height:float = 0.375
diameter:float = 1.5
inner_diameter:float = 0.1875

body:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .cylinder(height, inner_diameter/2, combine="cut")
)

cut_diameter:float = 0.1125
offset:float = 0.24375
cut_cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, cut_diameter/2)
    .translate((0,diameter/2-cut_diameter/2-offset,0))
)

part:cq.Workplane = (
    body
    .cut(cut_cylinder)
    .cut(cut_cylinder.rotate((0,0,1),(0,0,0),120))
    .cut(cut_cylinder.rotate((0,0,1),(0,0,0),-120))
)

part = part.translate((0,0,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')