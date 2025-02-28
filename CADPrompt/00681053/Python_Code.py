import cadquery as cq

length:float = 0.46077
width:float = 0.75
height:float = 0.048077

rectangle:cq.Workplane = cq.Workplane("XY").box(length, width, height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(rectangle.translate((-length/2,0,-height/2)))
    .union(rectangle.translate((length/2,0,-height/2)).rotate((0,1,0),(0,0,0),-60))
).translate((length,0,height)).rotate((0,1,0),(0,0,0),30).translate((-0.75/2,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')