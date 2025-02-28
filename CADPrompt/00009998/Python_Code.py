import cadquery as cq

box_length:float = 0.333333
box_width:float = 1.16667
box_height:float = 0.083333

box:cq.Workplane = cq.Workplane("XY").box(box_length, box_width, box_height)

cylinder_diameter:float = 0.166667
cylinder_height:float = 0.666667
cylinder_left_padding:float = 0.052435
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cylinder_height, cylinder_diameter/2)

part:cq.Workplane = box.add(cylinder.translate((
    0, 
    -box_width/2 + cylinder_diameter/2 + cylinder_left_padding, 
    box_height/2 + cylinder_height/2
)))

part = part.translate((-box_length/2, -0.075832, box_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')