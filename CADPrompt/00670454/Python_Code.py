import cadquery as cq

length:float = 1.125
width:float = 1.5
height:float = 0.039474

padding_length:float = 0.108553
padding_width:float = 0.098684
hole_diameter:float = 0.059211

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height).faces(">Z")
    .workplane()
    .rect(length - padding_length*2 - hole_diameter, width - padding_width*2 - hole_diameter, forConstruction=True)
    .edges("<X")
    .vertices()
    .hole(hole_diameter)
)

part = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')