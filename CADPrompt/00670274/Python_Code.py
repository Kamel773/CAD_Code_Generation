import cadquery as cq

length:float = 0.242193 + 0.045411*2
width:float = 0.817403 + 0.045411*2
height:float = 0.006055

cut_box_dim:float = 0.045411*2

part:cq.Workplane = (
    cq.Workplane("XY")
    .box(length, width, height)
    .edges("|Z").box(cut_box_dim, cut_box_dim,height, combine="cut")
)

part = part.translate((0.022705,0.295949,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')