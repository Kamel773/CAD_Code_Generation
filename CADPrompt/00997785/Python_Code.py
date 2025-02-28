import cadquery as cq

b_length:float = 0.867904
b_height:float = 0.272921

hex_length:float = 1.50001
hex_height:float = 0.409382
sides:int = 6

hexagon:cq.Workplane = (
    cq.Workplane("XY")
    .polygon(sides, hex_length)
    .extrude(hex_height)
    .rotate((0,0,1),(0,0,0),45)
    .faces("Z")
    .rect(b_length,b_length)
    .extrude(b_height)
    .rotate((0,0,1),(0,0,0),45)
)

part:cq.Workplane = hexagon

cq.exporters.export(part, 'Ground_Truth.stl')