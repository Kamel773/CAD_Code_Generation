import cadquery as cq

diameter:float = 1.5
extrude:float = 0.1

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(extrude, diameter/2)

cut_diameter:float = 0.1124
padding:float = 0.041187
cut_cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(extrude, cut_diameter/2)
    .translate((0, diameter/2 - cut_diameter/2 - padding, 0))
)

part:cq.Workplane = (
    cylinder
    .cut(cut_cylinder)
    .cut(cut_cylinder.rotate((0,0,1),(0,0,0),90))
    .cut(cut_cylinder.rotate((0,0,1),(0,0,0),180))
    .cut(cut_cylinder.rotate((0,0,1),(0,0,0),270))
).rotate((0,0,1),(0,0,0),45)

part = part.rotate((0,1,0),(0,0,0),90).translate((-extrude/2,0,0))
cq.exporters.export(part, 'Ground_Truth.stl')