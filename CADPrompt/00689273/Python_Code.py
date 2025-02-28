import cadquery as cq

width:float = 0.325804
diameter:float = 0.651607

length:float = 0.839006
box_width:float = 0.201998
height:float = 0.065161
box_margin:float = 0.791217
height_margin:float = 0.480984

cylinder:cq.Workplane = cq.Workplane("XZ").cylinder(width, diameter/2)
box:cq.Workplane = cq.Workplane("XY").box(length, box_width, height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .add(cylinder)
    .add(box.translate((box_margin/2+0.564309/2-0.020395,0,height/2-diameter/2+height_margin+0.003495)))
)

part = part.translate((-diameter/2-0.09946,-width/2,0.207149))

cq.exporters.export(part, 'Ground_Truth.stl')