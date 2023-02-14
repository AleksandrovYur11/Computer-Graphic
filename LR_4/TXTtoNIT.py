input_txt = open('C:\\\\LR4_Aleksandrov_render.txt', 'r')
data = input_txt.readlines()
input_txt.close()

size_x = 800
size_y = 600

def readTXT(start_y):
	colorRGB = [[[] for _ in range(800)] for _ in range(600)]

	for index_y in range(size_y):
		index_x = 0
		for index_x in range(size_x):
			if data[start_y][36] != " ":
				value_first_symbol = 35 + 15 * index_x
			else:
				value_first_symbol = 36 + 15 * index_x
			value_last_symbol = value_first_symbol + 9
			value = float(data[start_y + index_y][value_first_symbol:value_last_symbol])
			colorRGB[index_y][index_x] = value
	return colorRGB

r = readTXT(25)
g = readTXT(630)
b = readTXT(1235)

output_file_name = "C:\\\\LR4_Aleksandrov_render_from_txt.nit"

pp = PostProcessor(PPDataUnits.LUMINANCE, [], r, g, b) 
pp.SaveToHDR(output_file_name, overwrite = OverwriteMode.OVERWRITE) 

