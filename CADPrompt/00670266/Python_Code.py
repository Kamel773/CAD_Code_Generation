import cadquery as cq
length:float = 1.08869
width:float = 0.870954
height:float = 0.108869
diameter:float = 0.195965
offset:float = 0.228625
fillet_distance:float = 0.217746


cylinder:cq.Workplane = cq.Workplane("XY").cylinder(height, diameter/2)

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .cut(cylinder.translate((-length/2+diameter/2+offset,0,0)))
)

part = part.faces("<X").edges("Z").fillet(fillet_distance)
part = part.rotate((0,1,0),(0,0,0),-90).translate((height/2,0.037745,0.229328-0.023676))
cq.exporters.export(part, 'Ground_Truth.stl')