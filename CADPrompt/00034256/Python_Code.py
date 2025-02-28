import cadquery as cq

width:float = 0.3

base_length:float = 0.75
base_height:float = 0.15
base:cq.Workplane = cq.Workplane("XY").box(base_length, width, base_height)

diameter:float = 0.45
padding:float = -0.075769
cylinder:cq.Workplane = cq.Workplane("XY").cylinder(width, diameter/2).rotate((1,0,0),(0,0,0),90)

connector_height:float = diameter/2 + padding
connector:cq.Workplane = cq.Workplane("XY").box(diameter,width, connector_height)

part:cq.Workplane = (
    base
    .union(cylinder.translate((0, 0, base_height/2 + diameter/2 + padding)))
    .union(connector.translate((0, 0, base_height/2 + connector_height/2)))
)

part = part.translate((-base_length/2, -width/2, -base_height/2))
cq.exporters.export(part, 'Ground_Truth.stl')