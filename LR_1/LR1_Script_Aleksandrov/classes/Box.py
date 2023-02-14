class Box(PMesh):
	# Definition of parameters
	n_parts = Param("Number of parts", Int(1, 6), 3, init = True)
	centered = Param("Centered", Bool, True, init = True)
	org = Param("Origin", VectType(Size))
	size = Param("Size", VectType(Size(0.001)), (300, 200, 100))

	# Creation method
	def Init(self):
		print("Box construction")
		# Create parts
		np = self.n_parts
		if np > 1:
			self.AddPart("Top")
			self.parts[0].surf_attrs.name = "Top"
		if np > 2:
			self.AddPart("Bottom")
			self.parts[1].surf_attrs.name = "Bottom"
		if np > 3:
			self.AddPart("Front")
			self.parts[2].surf_attrs.name = "Front"
		if np > 4:
			self.AddPart("Back")
			self.parts[3].surf_attrs.name = "Back"
		if np > 5:
			self.AddPart("Right")
			self.AddPart("Left")
			self.parts[4].surf_attrs.name = "Right"
			self.parts[5].surf_attrs.name = "Left"
		else:
			self.AddPart("Side")
		if np == 0:
			self.parts[0].surf_attrs.name = "Side"
		if np == 2:
			self.parts[1].surf_attrs.name = "Side"
		if np == 3:
			self.parts[2].surf_attrs.name = "Side"
	# Evaluation method
	def Eval(self):
		print("Box evaluation")
		# Calculate box boundaries
		x1, y1, z1 = self.org
		length, width, height = self.size
		if self.centered:
			x1 -= length / 2; y1 -= width / 2; z1 -= height / 2
		x2 = x1 + length; y2 = y1 + width; z2 = z1 + height
		# Reconstruct box geometry
		self.ClearGeometry()
		self.AddVerts(0, [[x1, x2]], [[y1], [y2]], [[z2]], False)
		self.AddVerts(1, [[x1, x2]], [[y1], [y2]], [[z1]], True)
		self.AddVerts(2, [[x1, x2]], [[y1]], [[z1], [z2]], False)
		self.AddVerts(3, [[x1, x2]], [[y2]], [[z1], [z2]], True)
		self.AddVerts(4, [[x2]], [[y1, y2]], [[z1], [z2]], False)
		self.AddVerts(5, [[x1]], [[y1, y2]], [[z1], [z2]], True)