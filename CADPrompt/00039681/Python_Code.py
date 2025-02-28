import cadquery as cq

diameter:float = 1.5
height:float = 0.56371

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

cut_top_height:float = 0.242143
cut_top_diameter:float = diameter - 0.198214*2
cut_top_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cut_top_height, cut_top_diameter/2)

cut_bottom_height:float = height - cut_top_height
cut_bottom_diameter:float = 0.728571
cut_bottom_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cut_bottom_height, cut_bottom_diameter/2)

part:cq.Workplane = (
    cylinder
    .cut(cut_top_cylinder.translate((0, 0, height/2 - cut_top_height/2)))
    .cut(cut_bottom_cylinder.translate((0, 0 ,-height/2 + cut_bottom_height/2)))
)

part= part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')