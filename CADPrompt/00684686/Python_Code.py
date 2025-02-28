import cadquery as cq

length:float = 0.231564
width:float = 0.028954
height:float = 0.926255

cut_length:float = 0.12897
cut_height:float = 0.479215
bottom_margin:float = 0.005463

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .faces("-Z")
    .workplane(offset=-cut_height/2-bottom_margin)
    .center(0.003764,0)
    .box(cut_length,width,cut_height,combine="cut")
)

part = part.translate((-0.050509,-width/2,0.286873))

cq.exporters.export(part, 'Ground_Truth.stl')