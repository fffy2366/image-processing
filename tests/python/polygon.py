import matplotlib.path as mplPath
import numpy as np

poly = [190, 50, 500, 310]
bbPath = mplPath.Path(np.array([[poly[0], poly[1]],
                     [poly[1], poly[2]],
                     [poly[2], poly[3]],
                     [poly[3], poly[0]]]))

print bbPath.contains_point((400, 100))



poly = [[25,127],[235,127],[200,77],[125,77]]
bbPath = mplPath.Path(np.array([poly[0],
                     poly[1],
                     poly[2],
                     poly[3]]))

print bbPath.contains_point((180, 80))