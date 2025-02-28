import cadquery as cq

length:float = 0.75
width:float = 0.75
height:float = 0.1875

rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rectangle.translate((-length/2+height/2,0,0)))
    .union(rectangle.translate((-length/2+height/2,0,0)).rotate((0,1,0),(0,0,0),90))
)

part = (
    part.translate((-height/2,0,-height/2))
    .rotate((0,1,0),(0,0,0),180)
    .rotate((0,0,1),(0,0,0),90)
    .translate((length/2-0.042461,0,0))
)
cq.exporters.export(part, 'Ground_Truth.stl')