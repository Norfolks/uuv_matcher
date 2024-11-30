import numpy as np


def write_coords2file(coords, filename):
    with open(filename, "wt") as f:
        f.writelines(["VERSION .7\n",
                      "FIELDS x y z\n",
                      "SIZE 4 4 4\n",
                      "TYPE F F F\n",
                      "COUNT 1 1 1\n",
                      f"WIDTH {coords.size}\n",
                      "HEIGHT 1\n",
                      "VIEWPOINT 0 0 0 1 0 0 0\n",
                      f"POINTS {coords.size}\n",
                      "DATA ascii\n"])
        arr_str = np.array2string(coords, formatter={'float': lambda x: f'{x:.5f}'}, separator=' ', threshold=np.inf).replace("[",
                                                                                                             "").replace(
            "]", "").replace("\n ", "\n")
        f.writelines([arr_str])


def filter_polar_coordinates(coords, min_distance, max_distance, max_rad_hor, max_rad_ver):
    return coords[
        (coords[:, 0] > min_distance) & (coords[:, 0] < max_distance) & (np.abs(coords[:, 1]) < max_rad_hor) & (
                np.abs(coords[:, 2]) < max_rad_ver)]


def pol2cart(coordinates):
    # x = radius * cos(phi) * sin(theta)
    # y = radius * sin(phi) * sin(theta)
    # z = radius * cos(theta)
    x = coordinates[:, 0] * np.sin(coordinates[:, 1]) * np.cos(coordinates[:, 2])
    y = coordinates[:, 0] * np.sin(coordinates[:, 1]) * np.sin(coordinates[:, 2])
    z = coordinates[:, 0] * np.cos(coordinates[:, 2])

    cartesian_coordinates = np.stack((x, y, z), axis=-1)

    return cartesian_coordinates


def projection(coordinates, focal_length=1.0):
    # Apply the perspective projection formula
    x_proj = coordinates[:, 0] / (1 + coordinates[:, 2] / focal_length)
    y_proj = coordinates[:, 1] / (1 + coordinates[:, 2] / focal_length)

    return np.stack((x_proj, y_proj), axis=1)
