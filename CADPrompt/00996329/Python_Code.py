import cadquery as cq

width:float = 0.333333
height:float = 0.083333
length:float = 0.75 - height

plank:cq.Workplane = cq.Workplane("XY").box(length,width,height)

part = (
    cq.Workplane("XY")
    .union(plank.translate((0,0,height/2)))
    .union(plank.rotate((0,1,0),(0,0,0),90).translate((length/2-height/2,0,length/2+height)))
)

cq.exporters.export(part, 'Ground_Truth.stl')