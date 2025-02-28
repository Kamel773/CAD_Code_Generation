import cadquery as cq

length:float = 1.5
width:float = 1.02857
height:float = 0.17143

padding_length:float = 0.263507
padding_width:float = 0.219429
hole_diameter:float = 0.095635

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height).faces(">Z")
    .workplane()
    .rect(length -padding_length*2 -hole_diameter, width -padding_width*2 -hole_diameter, forConstruction=True)
    .vertices()
    .hole(hole_diameter)
)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')