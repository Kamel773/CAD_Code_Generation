import cadquery as cq

length = 1.19143
height = 0.085714

diameter = 0.094286
outer_diameter = 0.094286 + 0.060159*2


sketch = (
    cq.Sketch()
    .push([
        (-length/2-diameter/2,0),
        (length/2+diameter/2,0),
        (0,length/2.8552+diameter/2)
    ])
    .circle(outer_diameter/2)
    .wires()
    .hull()
    .push([
        (-length/2-diameter/2,0),
        (length/2+diameter/2,0),
    ])
    .circle(diameter/2, mode="s")
)

cut_box = cq.Workplane("XY").box(0.3,0.3,height)
cut_hole = cq.Workplane("XY").cylinder(height, 0.102857/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .placeSketch(sketch)
    .extrude(height)
    .cut(cut_box.translate((0,length/2.8552+0.3/1.35-0.001094,height/2)))
    .cut(cut_hole.translate((0,0.325506,height/2)))
)

part = part.rotate((0,0,1),(0,0,0),-90).translate((0.48581-0.008832,0,0))

cq.exporters.export(part, 'Ground_Truth.stl')