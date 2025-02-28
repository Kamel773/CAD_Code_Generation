import cadquery as cq

length:float = 1.5
width:float = 0.016304
height:float = 1.22283
diameter:float = 0.130435

left_margin:float = 0.433378
spacer:float = 0.195652

pane:cq.Workplane = cq.Workplane("XY").box(length, width, height)
hole:cq.Workplane = cq.Workplane("XZ").cylinder(width, diameter/2)

part:cq.Workplane = (
    pane
    .cut(hole.translate((-length/2 + diameter/2 + left_margin, 0, 0)))
    .cut(hole.translate((-length/2 + diameter/2 + left_margin, 0, diameter + spacer)))
    .cut(hole.translate((-length/2 + diameter/2 + left_margin, 0, -(diameter + spacer))))
)

part = part.translate((0, -width/2, 0))
cq.exporters.export(part, 'Ground_Truth.stl')