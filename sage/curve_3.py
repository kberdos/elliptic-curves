# define the elliptic curve
E = EllipticCurve([-5, 4])

# plot the curve
P = E.plot(color='black', thickness = 3)

# add the points to the plot
P += point((1, 0), color = 'blue', size= 70)
P += text(r"$P$", (1.25, 0.4), color='blue', fontsize=20)

P += line([(1, -10), (1, 10)], color='black')

# show the plot
P.show(xmin = -6, xmax = 6, ymin = -6, ymax = 6)
