import cadquery as cq

cylinder_height:float = 0.0375
diameter:float = 0.15
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cylinder_height, diameter/2)

length:float = 0.691425
width:float = 0.093715
height:float = 0.02625
rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part:cq.Workplane = (
    cylinder
    .translate((0,0,cylinder_height/2))
    .union(rectangle.translate((length/2 + diameter/2 - 0.0164, 0, height/2)))
)

part = part.rotate((0,1,0),(0,0,0),90).rotate((0,0,1),(0,0,0),180)
cq.exporters.export(part, 'Ground_Truth.stl')