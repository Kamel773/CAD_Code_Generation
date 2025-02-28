import cadquery as cq

height:float = 0.75
diameter:float = 0.419231

cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

cylinder = cylinder.translate((-0.09259 ,-0.022198,height/2))
part = cylinder.union(cylinder.translate((0.175164  ,0.040918 ,0)))
cq.exporters.export(part, 'Ground_Truth.stl')