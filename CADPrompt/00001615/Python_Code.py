import cadquery as cq

height:float = 1.5
diameter:float = 0.6
radius:float = diameter / 2

cut_length:float = diameter / 2.55
cut_width:float = diameter 
cut_height:float = height / 5.125

position_top:float = height / 2

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, radius)
cut_portion:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, cut_height)

part:cq.Workplane = cylinder.cut(cut_portion.translate((radius-cut_length/2,0,position_top - cut_height/2)))

cq.exporters.export(part, 'Ground_Truth.stl')