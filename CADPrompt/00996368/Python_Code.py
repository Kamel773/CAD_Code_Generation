import cadquery as cq
from typing import List,Tuple

extrude:float = 0.133054

pts:List[Tuple[float,float]] = [
       (0,0),
       (0.399631,0),
       (0.399631,0.091591),
       (0.399631-0.140768,0.091591),
       (0.399631-0.140768-0.061622-0.0001,0.188808),
       (0.399631-0.140768-0.061622-0.098345,0.188808),
       (0,0.091591)
]

shape:cq.Workplane = cq.Workplane("YZ").polyline(pts).close().extrude(extrude)

part:cq.Workplane = shape.translate((0,-0.399631-0.350837,-0.091591))

cq.exporters.export(part, 'Ground_Truth.stl')