import cadquery as cq
height:float = 0.248985
diameter:float = 0.192096

two_height:float = 0.220645
two_diameter:float = 0.13302

three_height:float = 0.070261
three_diameter:float = 0.250707

cut_out_height:float = height + two_height + three_height
cut_diameter:float = 0.098666

cylinder_one:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)
cylinder_two:cq.Workplane = cq.Workplane("XY").cylinder(two_height, two_diameter/2)
cylinder_three:cq.Workplane = cq.Workplane("XY").cylinder(three_height, three_diameter/2)
cut_out:cq.Workplane = cq.Workplane("XY").cylinder(cut_out_height, cut_diameter/2)

part:cq.Workplane = (
    cylinder_one
    .union(cylinder_two.translate((0,0,height/2+two_height/2)))
    .union(cylinder_three.translate((0,0,height/2+two_height+three_height/2)))
    .translate((0,0,height/2))
    .translate((0,0,-cut_out_height/2))
    .cut(cut_out)
)

part = part.translate((0, 0, cut_out_height/2)).rotate((1, 0, 0),(0, 0, 0), -90)
cq.exporters.export(part, 'Ground_Truth.stl')