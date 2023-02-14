class Cylinder(PMesh):

    radius = Param("Radius", Size, 2)
    length = Param("Length", Size, 10)
    n = Param("Radial Subdivision", Int(3, 1000), 36)
    m = Param("Length Subdivision", Int(3, 1000), 3)

    def Init(self):
        self.AddPart("Cylinder")
        self.parts[0].surf_attrs.name = "Cylinder"

    def Eval(self):
        self.ClearGeometry()
        r = self.radius
        l = self.length
        n = self.n
        m = self.m

        xx = []
        for i in range(n):
            xx.append([r * cos(i * 2 * pi / n)])
        xx.append(xx[0])

        yy = []
        for i in range(n):
            yy.append([r * sin(i * 2 * pi / n)])
        yy.append(yy[0])
        zz = []

        for i in range(m + 1):
            zz.append(i * l / m - l / 2)
        zz = [zz]
 
        self.AddVerts(0, xx, yy, zz, True)