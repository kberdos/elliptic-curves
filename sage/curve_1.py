# define the elliptic curve
E = EllipticCurve([-5, 4])

# plot the curve
P = E.plot(color='black', thickness = 3)

# add the points to the plot
P += point((1, 0), color = 'blue', size= 70)
P += point((0, 2), color = 'blue', size= 70)
P += point((3, 4), color = 'red', size = 70)
P += point((3, -4), color = 'black', size = 70)
P += text(r"$P$", (1.25, 0.4), color='blue', fontsize=20)
P += text(r"$Q$", (0.3, 2.2), color='blue', fontsize=20)
P += text(r'$P + Q$', (4, 4), color='red', fontsize=20)

# draw lines 
# define two points
p1 = (1, 0)
p2 = (0, 2)

# compute the slope and y-intercept of the line through P and Q
m = (p2[1] - p1[1])/(p2[0] - p1[0])
b = p1[1] - m*p1[0]

# plot the line through P and Q, extended to x = -10 and x = 10
P += line([(-6.5, m*(-6.5) + b), (6.5, m*(6.5) + b)], color = 'black')
P += line([(3, -10), (3, 10)], color='black')

# show the plot
P.show(xmin = -6, xmax = 6, ymin = -6, ymax = 6)
