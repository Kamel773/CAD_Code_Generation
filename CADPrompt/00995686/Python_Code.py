import cadquery as cq

width:float = 0.75
diameter:float = 0.702675
inner_diameter:float = 0.702675 - 0.049281*2

cylinder:cq.Workplane = (
    cq.Workplane("XZ")
    .cylinder(width, diameter/2)
    .faces("Y")
    .circle(inner_diameter/2)
    .extrude(width, combine="cut")
)

cut_box:cq.Workplane = cq.Workplane("XY").box(diameter, width, diameter)
part = (
    cq.Workplane("XY")
    .union(cylinder.translate((0.008514,-width/2,-0.0145)))
    .cut(cut_box.translate((-diameter/2,-width/2,diameter/2)))
)


cq.exporters.export(part, 'Ground_Truth.stl')