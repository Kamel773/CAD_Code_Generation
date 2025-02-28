import cadquery as cq

height:float = 0.152284
cylinder_diameter:float = 0.86802
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, cylinder_diameter/2)

rec_length:float = 0.63198
rec_width:float = cylinder_diameter
rec:cq.Workplane = cq.Workplane("XY").box(rec_length, rec_width, height)


part:cq.Workplane = (
    cq.Workplane("XY")
    .union(cylinder)
    .union(rec.translate((-rec_length/2,0, 0)))
)

part = part.translate((rec_length/2, 0, height/2)).rotate((0,0,1),(0,0,0),-90)


cq.exporters.export(part, 'Ground_Truth.stl')