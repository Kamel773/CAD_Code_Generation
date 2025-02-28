import cadquery as cq

length:float = 1.5
width:float = 0.416667
table_top_height:float = 0.083333

leg_length:float = 0.166667
leg_width:float = width
leg_height:float = 0.475

diameter:float = 0.1375

table_top:cq.Workplane = cq.Workplane("XY").box(length, width, table_top_height).cylinder(table_top_height,diameter/2, combine="cut")
leg:cq.Workplane = cq.Workplane("XY").box(leg_length, leg_width, leg_height).translate((0, 0, -(leg_height/2)-table_top_height))

def add_leg(loc: cq.Location) -> cq.Shape:
    global leg
    return leg.val().located(loc) #type:ignore

legs:cq.Workplane = table_top.faces(">Z").workplane().rect(length - leg_length, width - leg_width, forConstruction=True).vertices().eachpoint(add_leg)
table:cq.Workplane = table_top.union(legs)

part:cq.Workplane = table.translate((0, 0, -table_top_height/2)).rotate((1,0,0),(0,0,0),180)

cq.exporters.export(part, 'Ground_Truth.stl')