import cadquery as cq

length:float = 0.23077
width:float = 0.23077

inside_padding:float = 0.023077
extrude:float = 0.75

outline:cq.Sketch = (
    cq.Sketch()
    .rect(length, width)
    .rect(length - inside_padding*2, width - inside_padding*2, mode="s")
)

part:cq.Workplane = cq.Workplane("XY").placeSketch(outline).extrude(extrude)

cq.exporters.export(part, 'Ground_Truth.stl')