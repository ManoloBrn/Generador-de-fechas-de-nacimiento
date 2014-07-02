nombre = raw_input("Nombre de archivo: ")
f = open(nombre, 'w')
a =  input("Dame tu anio inicial: ")
a2 = input("Dame tu anio final: ")
m = 1
d = 1
while (a <= a2):
	m = 1
	while (m <=12):
		d = 1
		while(d<=31):
			if (d < 10 and m < 10):
				f.write("%d0%d0%d\n" % (a ,m, d))
			if (d < 10 and m >=10):
				f.write("%d%d0%d\n" % (a ,m, d))
			if (d >= 10 and m < 10):
				f.write("%d0%d%d\n" % (a ,m, d))
			if (d >=10 and m >=10):
				f.write("%d%d%d\n" % (a ,m, d))
			d = d+1

		m = m+1

	a = a +1
f.close()