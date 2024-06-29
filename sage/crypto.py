# define the elliptic curve
E = EllipticCurve(GF(563), [1, -3])
# plot the curve
P = E.plot(pointsize = 20, color = 'black')
# generator
G = (161, 263)
# plot and label the generator
P += point(G, color = 'blue', size = 20)
P += text(r"$G$", (161.1, 280), color='blue', fontsize=15)
# define private keys 
dA = 13410
dB = 43191
# perform operations
Gp = E([161, 263]) 
QA = Gp * dA
QB = Gp * dB
# plot and label the points
P += point((528, 188), color = 'red', size = 20)
P += point((337, 318), color = 'red', size = 20)
P += text(r"$Q_A$", (515, 170), color='red', fontsize=15)
P += text(r"$Q_B$", (325, 335), color='red', fontsize=15)
# generate shared secret
S = QB * dA
# plot and label shared secret
P += point((445, 414), color = 'green', size = 20)
P += text(r"$S$", (455, 425), color='green', fontsize=15)
# show the plot
P.show(xmin = -5, xmax = 565, ymin = -5, ymax = 565)
# print the points 
QA
QB
S
# verify the secret is shared 
QA * dB