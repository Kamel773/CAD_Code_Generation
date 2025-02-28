import cadquery as cq

length:float = 1.23418
width:float = 0.617188
height:float = 0.75

rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)

cylinder_height:float = 0.140625
diameter:float = 0.380469
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(cylinder_height, diameter/2)

padding:float = 0.118359
part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rectangle)
    .union(cylinder.translate((-(length/2-diameter/2 - padding),0,-(height/2+cylinder_height/2))))
    .union(cylinder.translate(((length/2-diameter/2 - padding),0,-(height/2+cylinder_height/2))))
)

part = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')