# New scene

def setTexture(part, r, g, b, typeMapp):
    part.surf_attrs.front_side.kd = 0.66
    part.surf_attrs.front_side.kd_color = RGBSurfColor(r, g, b)
    modifier = TxtModifier()
    part.tma = 1
    textu = StdTexture('chess_bw.png', 1, 0)
    modifier.mapping.texture = textu
    part.surf_attrs.front_side.kd_mod = modifier
    m3d = Mapping3D()
    m3d.type = typeMapp
    m3d.size = 100
    m3d.inher_mode = 2
    part.own_mapping3d = m3d

scene = Scene()

# Light 1: Parallel
light_lib = GetLibrary(Light)
light_source_1 = light_lib.GetItem("Parallel")
light_node_1 = LightNode(light_source_1, name = 'parallelLight_1', ) 
light1_transform = Transform()
light1_transform.azim = 90
light1_transform.tilt = 45
light1_transform.rot = 90
light_node_1.tr = light1_transform
light_node_1.Translate(-170, 0, 0)

# Light 2: Parallel
light_source_2 = light_lib.GetItem("Parallel") 
light_node_2 = LightNode(light_source_2, name = 'parallelLight_2', )
light2_transform = Transform()
light2_transform.azim = 135
light2_transform.tilt = 55
light2_transform.rot = 135
light_node_2.tr = light2_transform
light_node_2.Translate(10, 0, 0)

# Observrer 1 : lens 160
lobs = LensObserver()    
lobs.phenom = ObserverData.ILLUM
lobs.pupil_diam = 20
lobs.focal_length = 80
lobs.focusing_dist = 160
lobs.view_angle = 70
lobs.res = 600, 600
lobs.image_dist = 160
onode = ObserverNode(lobs)
onode.name = "Lens Observer_160" 
onode.Translate(110, -100, 0)
onode.Rotate(-95, 0, -110)

# Observrer 2 : lens 220
lobs1 = LensObserver()
lobs1.phenom = ObserverData.ILLUM
lobs1.pupil_diam = 20
lobs1.focal_length = 80
lobs1.focusing_dist = 220
lobs1.view_angle = 70
lobs1.res = 600, 600
lobs1.image_dist = 125.7143
onode1 = ObserverNode(lobs1)
onode1.name = "Lens Observer_220"
onode1.Translate(110, -100, 0)
onode1.Rotate(-95, 0, -110)

# Observrer 3 : lens 370
lobs2 = LensObserver()
lobs2.phenom = ObserverData.ILLUM
lobs2.pupil_diam = 20
lobs2.focal_length = 80
lobs2.focusing_dist = 450
lobs2.view_angle = 70
lobs2.res = 600, 600
lobs2.image_dist = 97
onode2 = ObserverNode(lobs2)
onode2.name = "Lens Observer_370"
onode2.Translate(110, -100, 0)
onode2.Rotate(-95, 0, -110)


# Cone
ConeClass = GetClass(Shape, 'Cone')
cone = ConeClass(name = "myCone", length = 150, radius1 = 10, radius2 = 50)
setTexture(cone.parts[0], 1, 0, 0, 2)
cone_node = MeshNode(cone)
cone_transform = XYZTransform()
cone_transform.pos = (-50, 0, 0)
cone_node.tr = cone_transform

BoxClass = GetClass(Shape, 'Box')
box = BoxClass(name = "myBox", centered = True, size = (150, 150, 150))
setTexture(box.parts[0], 0, 1, 0, 3)
setTexture(box.parts[1], 0, 1, 0, 3)
setTexture(box.parts[2], 0, 1, 0, 3)
box_node = MeshNode(box)
box_transform = XYZTransform()
box_transform.pos = (-170, -10, 0)
box_node.tr = box_transform

# Sphere
SphereClass = GetClass(Shape, 'Sphere')
sphere = SphereClass(name = "mySphere", radius = 100)
setTexture(sphere.parts[0], 0, 0, 1, 1)
sphere_node = MeshNode(sphere)
sphere_transform = XYZTransform()
sphere_transform.pos = (-300, -90, 0)
sphere_node.tr = sphere_transform

# Camera ideals_160
ideal_lens_160 = Camera(70, 160)
ideal_lens_160.is_lens = True
ideal_lens_160.lens_locks = (CameraLensParamLock.FOCAL_LENGTH or CameraLensParamLock.TARGET_DISTANCE)
ideal_lens_160.lens_type = IDEAL
ideal_lens_160.pupil_diam = 20
ideal_lens_160.SetLensParams(80, 160, 160)
ideal_lens_160_transform = XYZTransform()
ideal_lens_160_transform.pos = (110, -100, 0)
ideal_lens_160_transform.x_rot_ang = -95
ideal_lens_160_transform.y_rot_ang = 0
ideal_lens_160_transform.z_rot_ang = -110
ideal_lens_160.tr = ideal_lens_160_transform
ideal_lens_160.name = "ideal_160"

# Camera ideals_220
ideal_lens_220 = Camera(70, 220)
ideal_lens_220.is_lens = True
ideal_lens_220.lens_loks = (CameraLensParamLock.FOCAL_LENGTH or CameraLensParamLock.TARGET_DISTANCE)
ideal_lens_220.lens_type = IDEAL
ideal_lens_220.pupil_diam = 20
ideal_lens_220.SetLensParams(80, 125.7143, 220)
ideal_lens_220_transform = XYZTransform()
ideal_lens_220_transform.pos = (110, -100, 0)
ideal_lens_220_transform.x_rot_ang = -95
ideal_lens_220_transform.y_rot_ang = 0
ideal_lens_220_transform.z_rot_ang = -110
ideal_lens_220.tr = ideal_lens_220_transform
ideal_lens_220.name = "ideal_220"

# Camera ideals_370
ideal_lens_370 = Camera(70, 370)
ideal_lens_370.is_lens = True;
ideal_lens_370.lens_lonks = (CameraLensParamLock.FOCAL_LENGTH or CameraLensParamLock.TARGET_DISTANCE)
ideal_lens_370.lens_type = IDEAL
ideal_lens_370.pupil_diam = 20
ideal_lens_370.SetLensParams(80, 102.069, 370)
ideal_lens_370_transform = XYZTransform()
ideal_lens_370_transform.pos = (110, -100, 0)
ideal_lens_370_transform.x_rot_ang = -95
ideal_lens_370_transform.y_rot_ang = 0
ideal_lens_370_transform.z_rot_ang = -110
ideal_lens_370.tr = ideal_lens_370_transform
ideal_lens_370.name = "ideal_370"



#addition of the object node to a scene
scene.AddNode(light_node_1) 
scene.AddNode(light_node_2) 
scene.AddNode(onode) 
scene.AddNode(onode1)
scene.AddNode(onode2)
scene.AddNode(box_node)
scene.AddNode(cone_node)
scene.AddNode(sphere_node)
scene.Notebook().AddCamera(ideal_lens_160)
scene.Notebook().AddCamera(ideal_lens_220)
scene.Notebook().AddCamera(ideal_lens_370)
scene.CreateBackground().col_intensity = 0

LoadScene(scene) # Scene loading in Lumicept viewport 

# Path Tracing
pt_params = scene.PTRenderParams()
pt_params.res = (600, 600)
kernel = GetKernel()
kernel.PTRenderNotebook(scene.Notebook(), "ideal_lens_20.jpg", OverwriteMode.OVERWRITE)

# IMAPS
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 2000
imaps.SetObserverAsAccSource(onode)
kernel.CalculateIMaps()
