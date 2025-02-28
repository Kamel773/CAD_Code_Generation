import cadquery as cq

height:float = 0.16071
cylinder_diameter:float = 0.75
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, cylinder_diameter/2)

rec_length:float = 0.75
rec_width:float = 0.75
rec:cq.Workplane = cq.Workplane("XY").box(rec_length, rec_width, height)

cut_diameter:float = 0.267857
cut_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, cut_diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(cylinder)
    .union(rec.translate((0, -cylinder_diameter/2, 0)))
    .cut(cut_cylinder)
)

part = part.translate((rec_length/2, 0, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')