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

def setSimpleMedium(part, name_inside, inside_refr_ind, env_medium):
    inside = SimpleMedium(name = name_inside, refr_ind = inside_refr_ind)
    part.back_medium = inside
    part.front_medium = env_medium


def setEnvSimpleMedium(part, env_medium):
    part.back_medium = env_medium
    part.front_medium = env_medium

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



# Observrer 1 
pobs = PlaneObserver()    
pobs.phenom = 1  
pobs.res = 600, 600
pobs.thresh_ang = 70                                            
pobs.org = (-112, -112, 145)
pobs.x_side = (224, 0, 0)
pobs.y_side = (0, 224, 0)
pobs.dir = (0, 0, 100)
pobs.phenom = ObserverData.ILLUM
onode = ObserverNode(pobs)
onode.name = "Plane Observer_160"    
onode.color = (255, 255, 0)

# Observrer 2 
pobs1 = PlaneObserver()    
pobs1.phenom = 1  
pobs1.res = 600, 600
pobs1.thresh_ang = 70                                            
pobs1.org = (-88, -88, 110.7143)
pobs1.x_side = (176, 0, 0)
pobs1.y_side = (0, 176, 0)
pobs1.dir = (0, 0, 100)
pobs1.phenom = ObserverData.ILLUM
onode1 = ObserverNode(pobs1)
onode1.name = "Plane Observer_220"    
onode1.color = (255, 255, 0)

# Observrer 2 
pobs2 = PlaneObserver()    
pobs2.phenom = 1  
pobs2.res = 600, 600
pobs2.thresh_ang = 70                                            
pobs2.org = (-71, -71, 87.069)
pobs2.x_side = (142, 0, 0)
pobs2.y_side = (0, 142, 0)
pobs2.dir = (0, 0, 100)
pobs2.phenom = ObserverData.ILLUM
onode2 = ObserverNode(pobs2)
onode2.name = "Plane Observer_370"    
onode2.color = (255, 255, 0)

# Aspherical Surface 1 lens
AsphericalSurfaceClass = GetClass(Shape, 'Aspherical Surface')
asphericalSurface_1 = AsphericalSurfaceClass(name = "AsphericalSurface1_Lens", h = 20, h0 = 0, r = 62)
asphericalSurface_1.parts[0].surf_attrs.front_side.kd = 0
asphericalSurface_1.parts[0].surf_attrs.front_side.kts = 1
asphericalSurface_1.parts[0].surf_attrs.front_side.gs = 100000
asphericalSurface_1.parts[0].surf_attrs.front_side.gm = 100000
setSimpleMedium(asphericalSurface_1.parts[0], "glass", 1.4,scene.GetMedium("env"))
asphericalSurface_1_node_lens = MeshNode(asphericalSurface_1, name = "AsphericalSurface1_Lens")
asphericalSurface_1_transform = XYZTransform()
asphericalSurface_1_transform.pos = (0, 0, 0)
asphericalSurface_1_node_lens.tr  = asphericalSurface_1_transform

# Aspherical Surface 2 lens
asphericalSurface_2 = AsphericalSurfaceClass(name = "AsphericalSurface2_Lens", h = 20, h0 = 0, r = -62)
asphericalSurface_2.parts[0].surf_attrs.front_side.kd = 0
asphericalSurface_2.parts[0].surf_attrs.front_side.kts = 1
asphericalSurface_2.parts[0].surf_attrs.front_side.gs = 100000
asphericalSurface_2.parts[0].surf_attrs.front_side.gm = 100000
setSimpleMedium(asphericalSurface_2.parts[0], "glass", 1.4, scene.GetMedium("env"))
asphericalSurface_2_node_lens = MeshNode(asphericalSurface_2,  name = "AsphericalSurface2_Lens")
asphericalSurface_2_transform = XYZTransform()
asphericalSurface_2_transform.pos = (0, 0, 15)
asphericalSurface_2_node_lens.tr  = asphericalSurface_2_transform

# Cylinder lens
CylinderClass = GetClass(Shape, 'Cylinder')
cylinder_lens = CylinderClass(name = "Cylinder_Lens", radius = 20, length = 8.3712)
cylinder_lens.parts[0].surf_attrs.front_side.kd = 0
cylinder_lens.parts[0].surf_attrs.front_side.kts = 1
cylinder_lens.parts[0].surf_attrs.front_side.gs = 100000
cylinder_lens.parts[0].surf_attrs.front_side.gm = 100000
setSimpleMedium(cylinder_lens.parts[0], "glass", 1.4, scene.GetMedium("env"))
cylinder_node_lens = MeshNode(cylinder_lens,  name = "Cylinder_Lens")
cylinder_transform = XYZTransform()
cylinder_transform.pos = (0, 0, 7.5)
cylinder_node_lens.tr  = cylinder_transform

# Cone lens
ConeClass = GetClass(Shape, 'Cone')
cone_lens = ConeClass(name = "Cone_Lens", radius1 = 20, radius2 = 215, length = 200)
cone_lens.parts[0].surf_attrs.front_side.kd = 0
cone_lens.parts[0].surf_attrs.front_side.kts = 0
cone_lens.parts[0].surf_attrs.front_side.gs = 100000
cone_lens.parts[0].surf_attrs.front_side.gm = 100000
setEnvSimpleMedium(cone_lens.parts[0], scene.GetMedium("env"))
cone_node_lens = MeshNode(cone_lens,  name = "Cone_Lens")
cone_transform = XYZTransform()
cone_transform.pos = (0, 0, 103.3144)
cone_node_lens.tr = cone_transform

# Ring lens
RingClass = GetClass(Shape, 'Ring')
ring_lens = RingClass(name = "Ring_Lens", org = (0, 0, 0),  centered = True, radius1 = 20, radius2 = 31)
ring_lens.parts[0].surf_attrs.front_side.kd = 0
ring_lens.parts[0].surf_attrs.front_side.kts = 0
ring_lens.parts[0].surf_attrs.front_side.gs = 100000
ring_lens.parts[0].surf_attrs.front_side.gm = 100000
setEnvSimpleMedium(ring_lens.parts[0],scene.GetMedium("env"))
ring_node_lens = MeshNode(ring_lens, name = "Ring_lens")
ring_transform = XYZTransform()
ring_transform.pos = (0, 0, 15)
ring_node_lens.tr = ring_transform

# Cone
ConeClass = GetClass(Shape, 'Cone')
cone = ConeClass(name = "myCone", length = 150, radius2 = 50, radius1 = 10)
setTexture(cone.parts[0], 1, 0, 0, 2)
cone_node = MeshNode(cone)
cone_transform = XYZTransform()
cone_transform.pos = (-50, 0, 0)
cone_node.tr = cone_transform

# Box
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
real_lens_160 = Camera(70, 160)
real_lens_160.is_lens = True
real_lens_160.lens_unlocks = (CameraLensParamLock.FOCAL_LENGTH or CameraLensParamLock.TARGET_DISTANCE)
real_lens_160.lens_type = REAL
real_lens_160.lens_thickness = 15
real_lens_160.pupil_diam = 40
real_lens_160.image_dist = 160
real_lens_160.object_dist = 160
real_lens_160.focal_length = 80
real_lens_160_transform = XYZTransform()
real_lens_160_transform.pos = (110, -100, 0)
real_lens_160_transform.x_rot_ang = -95
real_lens_160_transform.y_rot_ang = 0
real_lens_160_transform.z_rot_ang = -110
real_lens_160.tr = real_lens_160_transform
real_lens_160.name = "real_160"

# Camera ideals_220
real_lens_220 = Camera(70, 220)
real_lens_220.is_lens = True
real_lens_220.lens_loks = (CameraLensParamLock.FOCAL_LENGTH or CameraLensParamLock.TARGET_DISTANCE)
real_lens_220.lens_type = REAL
real_lens_220.lens_thickness = 15
real_lens_220.pupil_diam = 40
real_lens_220.SetLensParams(80, 125.7143, 220)
real_lens_220_transform = XYZTransform()
real_lens_220_transform.pos = (110, -100, 0)
real_lens_220_transform.x_rot_ang = -95
real_lens_220_transform.y_rot_ang = 0
real_lens_220_transform.z_rot_ang = -110
real_lens_220.tr = real_lens_220_transform
real_lens_220.name = "real_220"

# Camera ideals_370
real_lens_370 = Camera(70, 370)
real_lens_370.is_lens = True
real_lens_370.lens_lonks = (CameraLensParamLock.FOCAL_LENGTH or CameraLensParamLock.TARGET_DISTANCE)
real_lens_370.lens_type = REAL
real_lens_370.lens_thickness = 15
real_lens_370.pupil_diam = 40
real_lens_370.SetLensParams(80, 102.069, 370)
real_lens_370_transform = XYZTransform()
real_lens_370_transform.pos = (110, -100, 0)
real_lens_370_transform.x_rot_ang = -95
real_lens_370_transform.y_rot_ang = 0
real_lens_370_transform.z_rot_ang = -110
real_lens_370.tr = real_lens_370_transform
real_lens_370.name = "real_370"



lens_wrapper = Node(name = 'lens_wrapper')
lens_wrapper.AddNode(cone_node_lens)
lens_wrapper.AddNode(ring_node_lens)
lens_wrapper.AddNode(cylinder_node_lens)
lens_wrapper.AddNode(asphericalSurface_1_node_lens)
lens_wrapper.AddNode(asphericalSurface_2_node_lens)
lens_wrapper.AddNode(onode)
lens_wrapper.AddNode(onode1)
lens_wrapper.AddNode(onode2)
lens_wrapper_transform = XYZTransform()
lens_wrapper_transform.pos = (110, -100, 0)
lens_wrapper_transform.x_rot_ang = -95
lens_wrapper_transform.y_rot_ang = 0
lens_wrapper_transform.z_rot_ang = -110
lens_wrapper.tr = lens_wrapper_transform

#addition of the object node to a scene
scene.AddNode(light_node_1) 
scene.AddNode(light_node_2) 
scene.AddNode(lens_wrapper)
scene.AddNode(box_node)
scene.AddNode(sphere_node)
scene.AddNode(cone_node)
scene.Notebook().AddCamera(real_lens_160)
scene.Notebook().AddCamera(real_lens_220)
scene.Notebook().AddCamera(real_lens_370)
scene.CreateBackground().col_intensity = 0



LoadScene(scene) # Scene loading in Lumicept viewport 

# Path Tracing
pt_params = scene.PTRenderParams()
pt_params.res = (600, 600)
kernel = GetKernel()
kernel.PTRenderNotebook(scene.Notebook(), "real_lens_40.jpg", OverwriteMode.OVERWRITE)

# IMAPS
imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 2000
imaps.SetObserverAsAccSource(onode)
kernel.CalculateIMaps()
