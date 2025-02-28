import cadquery as cq

length:float = 0.75
width:float = 0.28043
height:float = 0.02045

cut_length:float = 0.318403
cut_width:float = 0.157741

center_offset:float = 0.011+0.010963

rectangle:cq.Workplane = cq.Workplane("XY").box(length,width,height)
cut_out:cq.Workplane = cq.Workplane("XY").box(cut_length,cut_width,height)

part:cq.Workplane = rectangle.cut(cut_out.translate((0,center_offset,0)))

part = part.rotate((1, 0, 0),(0, 0, 0), -90).translate((length/2, -height/2, width/2))
cq.exporters.export(part, 'Ground_Truth.stl')