import cadquery as cq

length:float = 0.875
width:float = 0.15
height:float = 1.5
fillet:float = 0.25
diameter:float = 0.3
padding:float = -.65+ 0.035355 - 0.007163 - 0.002263

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .tag("body")
    .faces(">Y")
    .workplane()
    .rect(length+padding, height+padding, forConstruction=True)
    .edges("Z")
    .vertices()
    .circle(diameter/2).extrude(-width, combine = "cut")
    .faces("-X", tag="body")
    .edges("|Y")
    .fillet(fillet)
)

part = part.translate((0,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')