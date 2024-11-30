import open3d as o3d
import numpy as np
import copy


def draw_registration_result(source, target, transformation):
    source_temp = copy.deepcopy(source)
    target_temp = copy.deepcopy(target)
    source_temp.paint_uniform_color([1, 0.706, 0])
    target_temp.paint_uniform_color([0, 0.651, 0.929])
    source_temp.transform(transformation)
    o3d.visualization.draw_geometries([source_temp, target_temp])


def get_distance_after_icp():
    source = o3d.io.read_point_cloud("./init.pcd")
    target = o3d.io.read_point_cloud("./target.pcd")
    threshold = 0.02
    print("Initial alignment")
    default_transformation = np.asarray([[1, 0, 0, 0],
                                       [0, 1, 0, 0],
                                       [0, 0, 1, 0],
                                       [0, 0, 0, 1]])
    evaluation = o3d.pipelines.registration.evaluate_registration(source, source,
                                                                  threshold, default_transformation, )
    print(evaluation)
    print(evaluation.transformation)
    return evaluation.transformation[0][0]

    # print("Apply point-to-point ICP")
    # reg_p2p = o3d.registration.registration_icp(
    #     source, target, threshold,
    #     estimation_method=o3d.registration.TransformationEstimationPointToPoint())
    # print(reg_p2p)
    # print("Transformation is:")
    # print(reg_p2p.transformation)
    # print("")
    # draw_registration_result(source, target, reg_p2p.transformation)
    #
    # print("Apply point-to-plane ICP")
    # reg_p2l = o3d.registration.registration_icp(
    #     source, target, threshold,
    #     estimation_method=o3d.registration.TransformationEstimationPointToPlane())
    # print(reg_p2l)
    # print("Transformation is:")
    # print(reg_p2l.transformation)
    # print("")
    # draw_registration_result(source, target, reg_p2l.transformation)
