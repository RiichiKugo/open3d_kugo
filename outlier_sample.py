# examples/Python/ReconstrunctionSystem/outlier_sample.py

import open3d as o3d


def display_inlier_outlier(cloud, ind):#cloud:input,ind:選択された点,invert=trueにすると残す点が逆転する
    inlier_cloud = o3d.geometry.select_down_sample(cloud,ind)
    outlier_cloud = o3d.geometry.select_down_sample(cloud, ind, invert=True)

    print("Showing outliers (red) and inliers (gray): ")
    outlier_cloud.paint_uniform_color([1, 0, 0])
    inlier_cloud.paint_uniform_color([0.8, 0.8, 0.8])
    o3d.visualization.draw_geometries([inlier_cloud, outlier_cloud])
    o3d.visualization.draw_geometries([inlier_cloud])


if __name__ == "__main__":
    # (1) Load a ply point cloud, print it, and render it
    print("Load a ply point cloud, print it, and render it")
    pcd = o3d.io.read_point_cloud("./dataset/realsense/scene/integrated.ply")
    o3d.visualization.draw_geometries([pcd])
    # (2) Downsample the point cloud with a voxel
    print("Downsample the point cloud with a voxel of 0.02")
    voxel_down_pcd = o3d.geometry.voxel_down_sample(pcd, voxel_size=0.01)
    o3d.visualization.draw_geometries([voxel_down_pcd])
    # (3) Every 5th points are selected
    #print("Every 5th points are selected")
    #uni_down_pcd = pcd.uniform_down_sample(every_k_points=5)
    #o3d.visualization.draw_geometries([uni_down_pcd])
    # (4) Statistical oulier removal
    print("Statistical oulier removal")
    cl, ind = o3d.geometry.statistical_outlier_removal(voxel_down_pcd, nb_neighbors=20,
                                                        std_ratio=2.0)
    display_inlier_outlier(voxel_down_pcd, ind)
    # (5) Radius oulier removal
    print("Radius oulier removal")
    cl, ind = voxel_down_pcd.remove_radius_outlier(nb_points=16, radius=0.05)
    display_inlier_outlier(voxel_down_pcd, ind)