import cadquery as cq

width:float = 0.5625
diameter:float = 0.567213

smaller_width:float = 0.1875 
smaller_diameter:float = 0.266022


part:cq.Workplane = (
    cq.Workplane("XZ")
    .cylinder(width, diameter/2)
    .faces("-Y")
    .workplane()
    .circle(smaller_diameter/2).extrude(smaller_width)
)

part = part.translate((0,-width/2,0))

cq.exporters.export(part, 'Ground_Truth.stl')