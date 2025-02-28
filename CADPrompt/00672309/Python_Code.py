import cadquery as cq

height:float = 0.6
diameter:float = 1.49414+0.003906
hole_diameter:float = diameter - 0.372218*2 - 0.001805*2

cut_box_length:float = 0.188827
cut_box_padding:float = 0.141966 + 0.002996 - 0.002508
cut_box:cq.Workplane = cq.Workplane("XY").box(cut_box_length, diameter/2,height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces(">Z")
    .hole(hole_diameter, height)
    .cut(cut_box.translate((0,-diameter/2-cut_box_padding,0)))
)

part = part.translate((0, 0, height/2))
cq.exporters.export(part, 'Ground_Truth.stl')