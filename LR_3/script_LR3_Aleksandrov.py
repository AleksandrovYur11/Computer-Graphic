# New scene
scene = Scene()

# Light: Point
light_lib = GetLibrary(Light) 
light_source = light_lib.GetItem("Point") 
light_source.radiometric = True
light_source.total_flux = 100
light_source.color = SpecLightColor( [1.0] * 41, range(380, 790, 10))
light_node = LightNode(light_source, name = 'pointLight', ) 
light_node.Translate(1000, 1000, -2000) 

#Color model
cm = ColorModel([it * 10 + 370 for it in range(1, 42)])
cm.SetSpectral()


# Observrer 1 : dir (0;0;-1) 30 deg
pobs = PlaneObserver()    
pobs.phenom = 1  
pobs.res = 10, 20
pobs.thresh_ang = 30                                            
pobs.org = (-1000, -2000, -10)
pobs.x_side = (2000, 0, 0)
pobs.y_side = (0, 4000, 0)
pobs.dir = (0, 0, -1000)
pobs.phenom = ObserverData.LUM
onode = ObserverNode(pobs)
onode.name = "Plane Observer_00-1_30deg"    
onode.color = (255, 255, 0)

# Observrer 2 : dir (0;0;-1) 5 deg
pobs1 = PlaneObserver()    
pobs1.phenom = 1  
pobs1.res = 10, 20
pobs1.thresh_ang = 5                                            
pobs1.org = (-1000, -2000, -10)
pobs1.x_side = (2000, 0, 0)
pobs1.y_side = (0, 4000, 0)
pobs1.dir = (0, 0, -1000)
pobs1.phenom = ObserverData.LUM
onode1 = ObserverNode(pobs1)
onode1.name = "Plane Observer_00-1_5deg"    
onode1.color = (255, 255, 0)    

# Observrer 3 : dir (0;1;-1) 30 deg
pobs2 = PlaneObserver()    
pobs2.phenom = 1 
pobs2.res = 10, 20
pobs2.thresh_ang = 5                                            
pobs2.org = (-1000, -2000, -10)
pobs2.x_side = (2000, 0, 0)
pobs2.y_side = (0, 4000, 0)
pobs2.dir = (0, 1000, -1000)
pobs2.phenom = ObserverData.LUM
onode2 = ObserverNode(pobs2)
onode2.name = "Plane Observer_01-1_30deg"    
onode2.color = (255, 255, 0) 

# Observrer 4 : dir (0;1;-1) 5 deg
pobs3 = PlaneObserver()    
pobs3.phenom = 1 
pobs3.res = 10, 20
pobs3.thresh_ang = 5                                            
pobs3.org = (-1000, -2000, -10)
pobs3.x_side = (2000, 0, 0)
pobs3.y_side = (0, 4000, 0)
pobs3.dir = (0, 1000, -1000)
pobs3.phenom = ObserverData.LUM
onode3 = ObserverNode(pobs3)
onode3.name = "Plane Observer_01-1_5deg"    
onode3.color = (255, 255, 0) 


# New Rectangle
RectangleClass = GetClass(Shape, 'Rectangle')
rec = RectangleClass(name = "myRectangle", centered = False, org = (-1000, -2000, 0), size = (2000, 4000))
rec.parts[0].surf_attrs.SetKd(0.75, BWSurfColor(0.88))
rec_node = MeshNode(rec)


#addition of the object node to a scene
scene.AddNode(rec_node) 
scene.AddNode(light_node) 
scene.AddNode(onode) 
scene.AddNode(onode1)
scene.AddNode(onode2)
scene.AddNode(onode3)
scene.color_model = cm

LoadScene(scene) # Scene loading in Lumicept viewport 

imaps = scene.IMapsParams()
imaps.req_acc = 0.01
imaps.time_limit = 12500
imaps.SetObserverAsAccSource(onode3)
kernel = GetKernel()
kernel.CalculateIMaps()