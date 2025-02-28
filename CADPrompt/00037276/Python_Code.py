import cadquery as cq

lg_diameter:float = 0.485133
sm_diameter:float = 0.157385
length:float = 0.993343 - lg_diameter/2 - sm_diameter/2
width:float = 0.243343

result:cq.Sketch = (
    cq.Sketch()
    .push([(length/2, 0)])
    .circle(lg_diameter/2)
    .push([(-length/2, 0)])
    .circle(sm_diameter/2)
    .wires()
    .hull()
)

part:cq.Workplane = (
    cq.Workplane("XY")
    .placeSketch(result)
    .extrude(width)
)

part = part.rotate((1,0,0),(0,0,0), 90).translate((-length/2,0,0)).rotate((0,0,1),(0,0,0),180)
cq.exporters.export(part, 'Ground_Truth.stl')