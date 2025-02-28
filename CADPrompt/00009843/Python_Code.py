import cadquery as cq

r1_length:float = 1.40217
r1_width:float = 0.062517
r1_height:float = 0.75

r1:cq.Workplane = cq.Workplane("XY").box(r1_length, r1_width, r1_height)

r2_length:float = 1.27174
r2_width:float = 0.103421
r2_height:float = 0.75

r2:cq.Workplane = cq.Workplane("XY").box(r2_length, r2_width, r2_height)

trap_length:float = 1.33696
trap_width:float = 0.092231
trap_height:float = 0.75
trap_angle = 72

trap_sketch = cq.Sketch().trapezoid(trap_length, trap_width, trap_angle)
trap:cq.Workplane = (
    cq.Workplane("XY")
    .placeSketch(trap_sketch)
    .extrude(trap_height)
    .translate((0,0,-trap_height/2))
)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(r1.translate((0,0,0)))
    .union(r2.translate((0,r1_width/2 + r2_width/2,0)))
    .union(trap.translate((0,r1_width/2 + r2_width/2 + trap_width,0)))
)

part = part.translate((0, -r1_width/2 - r2_width - trap_width, r1_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')