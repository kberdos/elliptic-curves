# define the elliptic curve
E = EllipticCurve(GF(37), [1, 0])

# plot the curve
P = E.plot(pointsize = 45, color = 'black')
P += point((10, 14), color = 'blue', size = 50)
P += point((24, 26), color = 'blue', size = 50)
P += point((24, 11), color = 'red', size = 50)

P += text(r"$P$", (11.2, 14), color='blue', fontsize=20)
P += text(r"$Q$", (25.3, 26), color='blue', fontsize=20)
P += text(r'$P + Q$', (27.1, 12.1), color='red', fontsize=20)

# show the plot
P.show(xmin = -5, xmax = 37, ymin = -5, ymax = 37)
