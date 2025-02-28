import cadquery as cq

length:float = 1.5
width:float =   1.2
height:float =  0.15

rec:cq.Workplane = cq.Workplane("XY").box(length, width, height)

center_diameter:float = 0.675
center_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, center_diameter/2)

side_diameter:float = 0.1968
side_padding:float = 0.033
side_cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, side_diameter/2)

part:cq.Workplane = (
    rec
    .cut(center_cylinder)
    .cut(side_cylinder.translate((length/2 - side_diameter/2 - side_padding, 0, 0)))
    .cut(side_cylinder.translate((-1*(length/2 - side_diameter/2 - side_padding), 0, 0)))
)

part = part.translate((0, 0, -height/2))
cq.exporters.export(part, 'Ground_Truth.stl')