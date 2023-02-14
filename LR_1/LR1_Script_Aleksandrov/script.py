# Load classes used by script
LoadScript("classes/Box.py") # creates plate geometry
LoadScript("classes/Cylinder.py") # creates tube geometry
# Plate parameters
x=1000
y=2000
z=20
psizes = (x, y, z) # plate sizes (in mm) along X, Y, Z axes
plate_shift_z = 800 # plate shift (in mm) along Z axis
# Cylinder parameters
dia = 100 # cylinder diameter
len = 800 # cylinder length
cyl_shift_z = 400 # cylinder shift along z axis
# Construct a scene
scene = Scene()
# Create and tune plate geometry
# class from "Box.pi"
plate=Box(name="Plate", org=(0,0,0), centered=False, size=psizes, 
n_parts=3)
# Create and tune cylinder geometry
cyl = Cylinder(name = "Tube", radius = dia/2, length = len, n = 36, m = 16)
# Construct plate node
plate_node = MeshNode(plate)
plate_node.name = "Plate"
plate_node.Translate(0, 0, plate_shift_z)
# Get references to plate parts
part_plate_top = plate.parts[0]
part_plate_bottom = plate.parts[1]
part_plate_side = plate.parts[2]
# attributes handler
surf_lib = GetLibrary(SurfAttrs)
part_plate_top.surf_attrs.name = "top_surface"
# assign of dimmed glass material
part_plate_top.surf_attrs = surf_lib.GetItem("dimmed")
# surface properties for side face
plate_side_attrs = part_plate_side.surf_attrs
part_plate_side.surf_attrs.name = "side_surface"
plate_side_attrs.SetKd(0.95, RGBSurfColor(1,0,0))
plate_side_attrs.SetKs(0.03, RGBSurfColor(1,1,1))
# Construct nodes of separate cylinders 
cylinder1_node = MeshNode(cyl) 
cylinder2_node = MeshNode(cyl) 
cylinder3_node = MeshNode(cyl) 
cylinder4_node = MeshNode(cyl) 
cylinder1_node.name = "Leg1" 
cylinder2_node.name = "Leg2" 
cylinder3_node.name = "Leg3" 
cylinder4_node.name = "Leg4" 
cylinder1_node.Translate(dia/2, dia/2, cyl_shift_z) 
cylinder2_node.Translate(x-dia/2,dia/2, cyl_shift_z) 
cylinder3_node.Translate(dia/2,y-dia/2, cyl_shift_z) 
cylinder4_node.Translate(x-dia/2,y-dia/2, cyl_shift_z) 
# Leg properties 
leg = cyl.parts[0] 
leg.surf_attrs.name = "leg" 
leg.surf_attrs = surf_lib.GetItem("wood_2_ti") 
# Adding Lamp item from the library 
node_lib = GetLibrary(Node) # handler to Node library 
lamp = node_lib.GetItem("lamp") # new lamp instance 
lamp.Translate(x/2,y/2,plate_shift_z+240) # lamp positioning 
# Adding Light to the scene 
light_lib = GetLibrary(Light) 

# Light library handler 
light_source = light_lib.GetItem("Point") 
# Light SOURCE definition 
light_node = LightNode(light_source) 
# creating single light NODE (fixture) using particular light SOURCE 
light_node.Translate(x/2,y/2,plate_shift_z+300) # light Node positioning 

light_source = light_lib.GetItem("Rectangle") 
# Light SOURCE definition 
light_node_1 = LightNode(light_source) 
# creating single light NODE (fixture) using particular light SOURCE 
light_node_1.Translate(x/3,y/3,plate_shift_z+500) # light Node 1 positioning

pobs1 = PlaneObserver()    
pobs1.phenom = 0  # luminance
pobs1.res = 11, 21
pobs1.thresh_ang = 90                                            
pobs1.org = (0, 0, 821)
pobs1.x_side = (1000, 0, 0)
pobs1.y_side = (0, 2000, 0)
pobs1.dir = (0, 0, 10)                                            
onode1 = ObserverNode(pobs1)
onode1.name = "PlaneObserver0"    
onode1.color = (255, 0, 0)     

gobs = GonioObserver() # construct gonio-observer 
gobs.res = 360, 181    # resolution
gobs.thresh_ang = 180  # threshold angle                                          
gobs.org = (500, 1000, 900) # observer origin
gobs.greenwich = (400, 0, 0)  # greenwich direction
gobs.dir = (0, 0, -400)       # pole axis direction                                     
gnode = ObserverNode(gobs)    # construct observer node
gnode.name = "GonioObserver0" # observer node name   
gnode.color = (255, 255, 0)   # observer node color 

# Fill scene 
scene.AddNode(onode1) # add observe1 node
scene.AddNode(gnode) # add observer node to the scene
scene.AddNode(plate_node) # addition of plate node 
scene.AddNode(cylinder1_node) # addition of cylinder node 
scene.AddNode(cylinder2_node) 
scene.AddNode(cylinder3_node) 
scene.AddNode(cylinder4_node) 
scene.AddNode(lamp) # adding lamp to the scene 
scene.AddNode(light_node) # adding light Node to the scene
scene.AddNode(light_node_1) # adding light Node 1 to the scene
# Scene loading in Lumicept viewport 
LoadScene(scene)
