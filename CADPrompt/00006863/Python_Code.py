import cadquery as cq

length:float = 0.66788
width:float = 0.75
extrude:float = 0.32847

sketch:cq.Sketch = cq.Sketch().rect(length,width)
part:cq.Workplane = cq.Workplane("XY").placeSketch(sketch).extrude(extrude)

part = part.translate((length/2, width/2, 0))
cq.exporters.export(part, 'Ground_Truth.stl')