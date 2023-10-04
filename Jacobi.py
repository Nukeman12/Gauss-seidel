from tabulate import tabulate

eq1x1 = float(input('Ingrese el valor de x: '))
eq1x2 = float(input('Ingrese el valor de y: '))
eq1x3 = float(input('Ingrese el valor de z: '))
eq1c = float(input('Ingrese el valor de a: '))
eq2x1 = float(input('Ingrese el valor de x: '))
eq2x2 = float(input('Ingrese el valor de y: '))
eq2x3 = float(input('Ingrese el valor de z: '))
eq2c = float(input('Ingrese el valor de b: '))
eq3x1 = float(input('Ingrese el valor de x: '))
eq3x2 = float(input('Ingrese el valor de y: '))
eq3x3 = float(input('Ingrese el valor de z: '))
eq3c = float(input('Ingrese el valor de c: '))


f1 = lambda x, y, z: (500 + 2 * y + 3 * z) / 17
f2 = lambda x, y, z: (200 + 5 * x + 2 * z) / 21
f3 = lambda x, y, z: (30 + 5 * x + 5 * y) / 22
x0 = 0
y0 = 0
z0 = 0
count = 1

e = float(input('Error de tolerancia: '))
print('\n-\tx\ty\tz\tError X\tError Y\tError Z\n')

condition = True
datos = []
datos.append(["Iteracion", "X1", "Error", "X2", "Error", "X3", "Error"])
datos.append([count - 1, x0, '', y0, '', z0, ''])


while condition:
    x1 = f1(x0, y0, z0)
    y1 = f2(x0, y0, z0)
    z1 = f3(x0, y0, z0)
    e1 = abs(x0 - x1)
    e2 = abs(y0 - y1)
    e3 = abs(z0 - z1)

    datos.append([count, x1, e1 / abs(x1), y1, e2 / abs(y1), z1, e3 / abs(z1)])
    count += 1
    x0 = x1
    y0 = y1
    z0 = z1

    condition = e1 > e or e2 > e or e3 > e

tabla = tabulate(datos, headers="firstrow", tablefmt="grid")
print(tabla)

print('\nSolución: x=%0.6f, y=%0.6f and z=%0.6f\n' % (x1, y1, z1))