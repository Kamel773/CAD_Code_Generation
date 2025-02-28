import cadquery as cq

extrude:float = 0.440903
diameter:float = 1.5

part:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(extrude, diameter/2)
)

part = part.translate((0, 0, extrude/2)).rotate((1,0,0),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')