import cadquery as cq

length:float = 0.75
width:float = 0.5
height:float = 0.75

dim_length:float = 0.25
dim_height:float = 0.5


cube:cq.Workplane = cq.Workplane("XY").box(dim_length,width,dim_height)

part:cq.Workplane = (
    cq.Workplane("XY").box(length, width, height)
    .cut(cube.translate((0,0,00.25/2)))
)

part = part.translate((0.172956,-width/2,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')