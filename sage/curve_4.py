# define the elliptic curve
E = EllipticCurve([-3, 3])

# plot the curve
P = E.plot(color='black', thickness = 3)

# define three collinear points on the curve
p1 = (-2, 1)
p2 = (0, sqrt(3))
p3 = (2.134, 2.513)
p4 = (2.134, -2.513)

# plot the points
P += point(p1, color='blue', size=50)
P += point(p2, color='blue', size=50)
P += point(p3, color='blue', size=50)
P += point(p4, color ='red', size =50)

P += text(r"$P$", (-2.5, 1.5), color='blue', fontsize=20)
P += text(r"$Q$", (0.3, 2.3), color='blue', fontsize=20)
P += text(r"$R$", (2.7, 3.1), color='blue', fontsize=20)
P += text(r"$P + Q$", (3.1, -2.513), color ='red', fontsize = 20)

m = (p2[1] - p1[1])/(p2[0] - p1[0])
b = p1[1] - m*p1[0]

# plot the line through P and Q, extended to x = -10 and x = 10
P += line([(-6.5, m*(-6.5) + b), (6.5, m*(6.5) + b)], color = 'black')
P += line([(2.134, -10), (2.134, 10)], color='black')

# show the plot
P.show(xmin = -6, xmax = 6, ymin = -6, ymax = 6)
