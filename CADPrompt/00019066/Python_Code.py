import cadquery as cq

pane_length:float = 0.345
pane_width:float = 0.0024
pane_height:float = 0.18
pane:cq.Workplane = cq.Workplane("XY").box(pane_length, pane_width, pane_height)

bar_length:float = 0.00375
bar_width:float = 0.75
bar_height:float = 0.0075
bar:cq.Workplane = cq.Workplane("XY").box(bar_length, bar_width, bar_height)

part:cq.Workplane = (
    cq.Workplane("XY")
    .union(pane.translate((pane_length/2, -pane_width/2, pane_height/2)))
    .union(bar.translate((bar_length/2, bar_width/2, bar_height/2)))
)

cq.exporters.export(part, 'Ground_Truth.stl')