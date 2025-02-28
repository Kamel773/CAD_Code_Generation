import cadquery as cq

length:float = 0.75
width:float = 0.25
height:float = 0.25

base:cq.Workplane = cq.Workplane("XY").box(length, width, height)
part:cq.Workplane = base.union(base.rotate((0,1,0),(0,0,0),90).translate((0,0,length/2+height/2)))

part = part.translate((width/2, -width/2, -height/2))
cq.exporters.export(part, 'Ground_Truth.stl')