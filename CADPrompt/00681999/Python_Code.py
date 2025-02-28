import cadquery as cq

length:float = 0.75
width:float = 0.25
height:float = 0.5

dim:float = 0.25

cube:cq.Workplane = cq.Workplane("XY").box(dim,dim,dim)

part:cq.Workplane = (
    cq.Workplane("XY").box(length, width, height)
    .cut(cube.translate((0,0,dim/2)))
)

part = part.translate((-length/2,-width/2,height/2))

cq.exporters.export(part, 'Ground_Truth.stl')