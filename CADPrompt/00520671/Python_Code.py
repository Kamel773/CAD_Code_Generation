import cadquery as cq
base_diameter:float = 1.5
base_height:float = 0.06

top_diameter:float = 0.75
top_height:float = 0.375

base:cq.Workplane = cq.Workplane("XY").circle(base_diameter/2).extrude(base_height)
top:cq.Workplane = cq.Workplane("XY").circle(top_diameter/2).extrude(top_height) 

cut_length:float = 0.21
cut_width:float = 0.45
cut_padding:float = 0.12
cut_rectangle:cq.Workplane = cq.Workplane("XY").box(cut_length, cut_width, base_height)

part:cq.Workplane = (
    base
    .union(top.translate((0, 0, base_height)))
    .cut(cut_rectangle.translate((base_diameter/2 - cut_length/2 - cut_padding,0,base_height/2)))
)

cq.exporters.export(part, 'Ground_Truth.stl')