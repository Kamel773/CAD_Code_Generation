import cadquery as cq

diameter:float = 0.02262
extrude:float = 0.75

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(extrude, diameter/2)

cut_diameter:float = 0.015476
cut_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(diameter, cut_diameter/2).rotate((0,1,0),(0,0,0),90)

one_padding:float = 0.004167
two_padding:float = 0.123228
three_padding:float = 0.06399

part:cq.Workplane = (
    cylinder
    .cut(cut_cylinder.translate((0,0,-extrude/2+cut_diameter/2+one_padding)))
    .cut(cut_cylinder.translate((0,0,-extrude/2+cut_diameter/2+two_padding)))
    .cut(cut_cylinder.translate((0,0,extrude/2-cut_diameter/2-three_padding)))
).translate((0,0,extrude/2)).rotate((1,0,0),(0,0,0),-90)

cq.exporters.export(part, 'Ground_Truth.stl')