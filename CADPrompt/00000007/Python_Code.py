import cadquery as cq

radius:float = 1.5/2
height:float = 0.20923

sketch:cq.Sketch = cq.Sketch().circle(radius)
part:cq.Workplane = cq.Workplane("XY").placeSketch(sketch).extrude(height)
cq.exporters.export(part, 'Ground_Truth.stl')