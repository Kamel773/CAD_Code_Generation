import cadquery as cq

length:float = 1.5
width:float = 0.153061
height:float = 0.918367

inner_length:float = 1.43878
inner_width:float = 0.229592
inner_height:float = 0.841837


box:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("-Y")
    .workplane()
    .rect(inner_length,inner_height)
    .extrude(inner_width)
)

part:cq.Workplane = box.translate((0,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')