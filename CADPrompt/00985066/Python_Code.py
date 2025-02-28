import cadquery as cq

length:float = 1.175
width:float = 0.35
table_top_height:float = 0.025

leg_length:float = 0.05
leg_width:float = width
leg_height:float = 0.725

table_top:cq.Workplane = cq.Workplane("XY").box(length, width, table_top_height)
leg:cq.Workplane = cq.Workplane("XY").box(leg_length, leg_width, leg_height).translate((0, 0, -(leg_height/2)-table_top_height))

def add_leg(loc: cq.Location) -> cq.Shape:
    global leg
    return leg.val().located(loc) #type:ignore

legs:cq.Workplane = table_top.faces(">Z").workplane().rect(length - leg_length, width - leg_width, forConstruction=True).vertices().eachpoint(add_leg)
table:cq.Workplane = table_top.union(legs)

part:cq.Workplane = table.translate((0, 0, -table_top_height/2)).rotate((1,0,0),(0,0,0),180)

cq.exporters.export(part, 'Ground_Truth.stl')