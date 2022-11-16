import numpy as np
import matplotlib.pyplot as plt

def GridCreator(Top_Coord, Bottom_Coord, CrossShoreRes, AlongShoreRes, BeachWidth=25):
    x_top = Top_Coord[0,:]; y_top = Top_Coord[1,:]
    x_bot = Bottom_Coord[0,:]; y_bot = Bottom_Coord[1,:]
    
    CrossSteps = int(BeachWidth / CrossShoreRes)

    y_coords = np.zeros((len(y_top), CrossSteps))
    x_coords = np.zeros((len(x_top), CrossSteps))
    coefs = np.zeros((CrossSteps,6))

    for i in range(len(y_top)):
        y_coords[i] = np.linspace(y_top[i], y_bot[i], CrossSteps)
        x_coords[i] = np.linspace(x_top[i], x_bot[i], CrossSteps)

    y_coords = y_coords.T;  x_coords = x_coords.T

    for j in range(CrossSteps):
        coefs[j] = np.polyfit(x_coords[j,:],y_coords[j,:],5)

    new_xcoords = np.linspace(x_top[0], x_bot[-1], AlongShoreRes)

    return y_coords, x_coords, coefs, new_xcoords

Top_Coord = np.array([[117409.381, 117261.811, 117032.068, 116557.854, 116071.970, 115824.012, 115526.010, 115306.900],
                      [560087.034, 559906.751, 559705.862, 559333.503, 558960.603, 558770.808, 558481.620, 558201.731]])

Bottom_Coord = np.array([[117429.800, 117276.787, 117043.922, 116566.903, 116083.360, 115833.942, 115535.520, 115343.973],
                         [560074.458, 559888.839, 559687.686, 559317.602, 558946.919, 558759.114, 558476.228, 558177.428]])


y_coords, x_coords, coefs, new_xcoords = GridCreator(Top_Coord, Bottom_Coord, 5, 2)

plt.plot(Top_Coord[0,:],Top_Coord[1,:], color='k')
plt.plot(Bottom_Coord[0,:],Bottom_Coord[1,:], color='k')

print(np.shape(x_coords))
for i in range(len(coefs)):
        poly1d_fn = np.poly1d(coefs[i,:])
        plt.scatter(x_coords[i], y_coords[i])
        # plt.plot(x_coords[i], poly1d_fn(x_coords[i]), label='down')



plt.show()


# x =  np.array([117409.381, 117261.811, 117032.068, 116557.854, 116071.970, 115824.012, 115526.010, 115306.900])
# y =  np.array([560087.034, 559906.751, 559705.862, 559333.503, 558960.603, 558770.808, 558481.620, 558201.731])

# x_new, y_new = np.meshgrid(x,y)
# plt.scatter(x_new, y_new)
# plt.scatter(x,y)
# plt.show()

