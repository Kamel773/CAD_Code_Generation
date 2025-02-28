import cadquery as cq

diameter:float = 0.533654
height:float = 0.75
cut_distance:float = 0.017308
cut_diameter:float = 0.090144

shelled_cylinder:cq.Workplane = (
    cq.Workplane("XY")
    .cylinder(height, diameter/2)
    .faces("Z")
    .shell(-cut_distance)
)

part:cq.Workplane = shelled_cylinder.faces("-Z").cylinder(0.017308*2, cut_diameter/2, combine="cut")

part = part.translate((0,0,height/2))
cq.exporters.export(part, 'Ground_Truth.stl')