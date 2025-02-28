import cadquery as cq

height:float = 0.75
diameter:float = 0.503822
inner_diameter:float = 0.426316
inner_height:float = 0.710526

cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height,diameter/2)
    .faces("Z")
    .workplane()
    .circle(inner_diameter/2)
    .extrude(-inner_height,combine="cut")
)

handle_length:float = 0.631579
handle_diameter:float = 0.05921
handle:cq.Workplane = cq.Workplane("XZ").cylinder(handle_length, handle_diameter/2)

handle_top_margin:float = 0.049342

part:cq.Workplane = (
    cylinder
    .union(handle.translate((0, 0, height/2 - handle_diameter/2 - handle_top_margin)))
)

part = part.translate((0, 0, height/2))

cq.exporters.export(part, 'Ground_Truth.stl')