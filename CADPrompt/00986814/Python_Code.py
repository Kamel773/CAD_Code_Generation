import cadquery as cq

length:float = 0.25
width:float = 0.75
height:float = 0.02
diameter:float = 0.07
cylinder_height:float = 0.04
padding:float = 0
bottom_padding:float = 0.005
side_padding:float = 0.0275

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cylinder_height,diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .union(cylinder.translate((
        length/2-diameter/2-side_padding,
        width/2-diameter/2-bottom_padding,
        height/2+cylinder_height/2)
    ))
    .union(cylinder.translate((
        -(length/2-diameter/2-side_padding),
        width/2-diameter/2-bottom_padding,
        height/2+cylinder_height/2)
    ))
)

part = part.translate((length/2,width/2,height/2))


cq.exporters.export(part, 'Ground_Truth.stl')