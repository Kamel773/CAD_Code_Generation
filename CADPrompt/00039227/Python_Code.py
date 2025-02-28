import cadquery as cq

diameter:float = 1.27949
length:float = 0.787604
width:float = 0.506095

extrude:float = 0.75

outline = cq.Sketch().circle(diameter/2).rect(length,width, mode="s")
part = cq.Workplane("XZ").placeSketch(outline).extrude(extrude)

cq.exporters.export(part, 'Ground_Truth.stl')