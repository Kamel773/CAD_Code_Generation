import cadquery as cq

length:float = 0.75
width:float = 0.199115

cut_rec_length:float = 0.232301
cut_rec_width:float = 0.112832

add_rec_length:float = 0.126106 
add_rec_width:float = 0.225664

extrude:float = 0.165929

sketch:cq.Sketch = (
    cq.Sketch()
    .rect(length,width)
    .push([(0,-cut_rec_width/2)])
    .rect(cut_rec_length, cut_rec_width, mode="s")
    .push([(-(0.165929/2+add_rec_length/2),width/2+add_rec_width/2), (0.165929/2+add_rec_length/2,width/2+add_rec_width/2)])
    .rect(add_rec_length, add_rec_width, mode="a")
)

part = cq.Workplane("XY").placeSketch(sketch).extrude(extrude)

part = part.translate((length/2,width/2,0)).rotate((1,0,0),(0,0,0),-90)
cq.exporters.export(part, 'Ground_Truth.stl')