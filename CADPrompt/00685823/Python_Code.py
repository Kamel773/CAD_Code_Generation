import cadquery as cq

length:float = 0.668421
width:float = 0.334211
height:float = 0.668421
diameter:float = .375

cut:cq.Workplane = cq.Workplane("XZ").cylinder(width, diameter*.7)
box:cq.Workplane = (
    cq.Workplane("XY")
    .box(length,width,height)
    .cut(cut.translate((length/2-diameter/2+0.1,0,height/2-diameter/2+0.1)))
)

part:cq.Workplane = box.translate((-length/2-0.081579,-width/2,0.179688))

cq.exporters.export(part, 'Ground_Truth.stl')