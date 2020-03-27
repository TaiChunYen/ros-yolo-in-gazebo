
def img2cam(u,v):
    center_x = 494.261#cx
    center_y = 385.166#cy
    constant_x = 1 / 1128.11742#fx
    constant_y = 1 / 1122.4038#fy
    depth = 89

    cam_origin_x = (float(u) - center_x) * depth * constant_x#left,right
    cam_origin_y = (float(v) - center_y) * depth * constant_y#up,down
    cam_origin_z = depth#front
    print([cam_origin_x,cam_origin_y,cam_origin_z])

img2cam(377.215,248.375)
