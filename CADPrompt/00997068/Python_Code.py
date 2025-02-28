import cadquery as cq

length:float = 0.00875
width:float =  0.74801
height:float =  0.03125
cut_width:float =  0.1625
cut_height:float = 0.0125
left_offset:float = 0.01875

rec:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .workplane(offset=-height/2+cut_height/2)
    .center(0,-width/2+cut_width/2+left_offset)
    .box(length,cut_width,cut_height, combine="cut")
)

part:cq.Workplane = rec.translate((-length/2,width/2,height/2)).rotate((0,0,1),(0,0,0),180)


cq.exporters.export(part, 'Ground_Truth.stl')