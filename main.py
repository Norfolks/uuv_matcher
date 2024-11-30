from positions import *
import matplotlib.pyplot as plt
from icp import get_distance_after_icp

EXPECTED_MOVEMENT = 5

INITIAL_ANGEL_HORIZONTAL = 3
INITIAL_ANGEL_VERTICAL = 3
INITIAL_DISTANCE_MIN = 5
INITIAL_DISTANCE_MAX = 10

NEW_ANGEL_HORIZONTAL = 3
NEW_ANGEL_VERTICAL= 3
NEW_DISTANCE_MIN = 3
NEW_DISTANCE_MAX = 7



def run():
    init_coordinates = np.loadtxt("init_coordinates", dtype=float)
    new_coordinates = np.loadtxt("new_coordinates", dtype=float)

    # filtered_init = filter_polar_coordinates(init_coordinates, INITIAL_DISTANCE_MIN, INITIAL_DISTANCE_MAX, INITIAL_ANGEL_HORIZONTAL, INITIAL_ANGEL_VERTICAL)
    # filtered_new = filter_polar_coordinates(new_coordinates, NEW_DISTANCE_MIN, NEW_DISTANCE_MAX, NEW_ANGEL_HORIZONTAL, NEW_ANGEL_VERTICAL)

    # fig = plt.figure()
    # ax = fig.add_subplot(projection='3d')
    # xs = init_coordinates[:, 0]
    # ys = init_coordinates[:, 1]
    # zs = init_coordinates[:, 2]
    # ax.scatter(xs, ys, zs, marker='o')
    # xs = new_coordinates[:, 0]
    # ys = new_coordinates[:, 1]
    # zs = new_coordinates[:, 2]
    # ax.scatter(xs, ys, zs, marker='^')
    #
    # ax.set_xlabel('X Label')
    # ax.set_ylabel('Y Label')
    # ax.set_zlabel('Z Label')
    #
    # plt.show()



    init_cart_3d = pol2cart(init_coordinates)
    new_cart_3d = pol2cart(new_coordinates)

    write_coords2file(init_cart_3d, "init.pcd")
    write_coords2file(new_cart_3d, "target.pcd")

    meters_moved = get_distance_after_icp()
    print(f"Meters moved: {meters_moved}")







if __name__ == "__main__":
    run()