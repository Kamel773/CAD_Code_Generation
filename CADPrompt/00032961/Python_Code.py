import cadquery as cq

length:float = 1.49973
width:float = 0.16071
extrude:float = 0.05357
slot:cq.Workplane = cq.Workplane("XY").slot2D(length,width).extrude(extrude)

cut_diameter:float = 0.080357
cut_hole:cq.Workplane = cq.Workplane("XY").cylinder(extrude, cut_diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(slot.translate((0, 0, -extrude/2)))
    .cut(cut_hole.translate(((length/2 - width/2), 0, 0)))
    .cut(cut_hole.translate((-(length/2 - width/2), 0, 0)))
)

part = part.rotate((0,0,1),(0,0,0),90).rotate((1,0,0),(0,0,0),90).translate((0, -extrude/2, 0))
cq.exporters.export(part, 'Ground_Truth.stl')