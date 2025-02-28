import cadquery as cq

length:float = 1.5
width:float = 1.5

inside_padding:float = 0.17649
extrude:float = 0.00265

outline:cq.Sketch = (
    cq.Sketch()
    .rect(length, width)
    .rect(length - inside_padding*2, width - inside_padding*2, mode="s")
)

part:cq.Workplane = cq.Workplane("XY").placeSketch(outline).extrude(extrude)
cq.exporters.export(part, 'Ground_Truth.stl')