import cadquery as cq

length:float = 0.1875
width:float = 0.1875

inside_padding:float = 0.014063
extrude:float = 0.75

outline:cq.Sketch = cq.Sketch().rect(length, width).rect(length - inside_padding*2, width - inside_padding*2, mode="s")
part:cq.Workplane = cq.Workplane("XY").placeSketch(outline).extrude(extrude)

part = part.rotate((1,0,0),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')