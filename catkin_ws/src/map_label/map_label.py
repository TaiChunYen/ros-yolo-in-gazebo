import cv2
import math
import numpy as np
from sklearn.cluster import DBSCAN
##### read marker data #####
marker_set = []
f = open("my_marker_file.txt")
lines = f.readlines()
for line in lines:
    marker = line.split(',')
    marker.pop()
    marker_set.append(marker)

##### DBSCAN #####

np_marker_set = np.array(marker_set).astype(np.float64)
#print(np_marker_set.shape)#(marker num,2)
clustering = DBSCAN(eps=0.2, min_samples=1).fit(np_marker_set)
labels = clustering.labels_
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
#print(n_clusters_)

##### show marker cluster result plot #####

'''core_samples_mask = np.zeros_like(labels, dtype=bool)
core_samples_mask[clustering.core_sample_indices_] = True
import matplotlib.pyplot as plt
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = np_marker_set[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = np_marker_set[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()'''

##### marker filter #####

label_cursor = 0
marker_filter = []
for i in range(len(labels)):
    if labels[i]==label_cursor:
        marker_filter.append(i)
        label_cursor+=1
    
filted_marker = [marker_set[index] for index in marker_filter]

##### calculate position accurancy #####

ground_truth = [[-1.4256+0.248,-0.120952],[-1.4256-0.248,-0.120952],[0.453669+0.248,1.91165],[0.453669-0.248,1.91165],[0.453708+0.248,2.42551],[0.453708-0.248,2.42551]]
np_ground_truth = np.array(ground_truth).astype(np.float64)

np_filted_marker = np.array(filted_marker).astype(np.float64)

all_error = []

for marker in np_marker_set:#np_filted_marker or np_marker_set
    min_error=float('Inf')
    for truth in np_ground_truth:
        tmp = truth - marker
        position_error = math.hypot(tmp[0],tmp[1])
        if position_error < min_error:
            min_error = position_error
    
    if min_error < 0.8:
        all_error.append(min_error)

avg_error = np.mean(all_error)
print(avg_error)

##### show different marker on map #####
'''
height = 217
img = cv2.imread('passion.jpg')
origin_x = -4.681169
origin_y = -3.636700

for point in filted_marker:
    map_c_x = int((float(point[0])-origin_x)/0.05)
    map_c_y = height - int((float(point[1])-origin_y)/0.05)
    
    color_plate = (list(np.random.choice(range(256), size=3)))
    cv2.circle(img,(map_c_x, map_c_y), 3, (int(color_plate[0]), int(color_plate[1]), int(color_plate[2])), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)
'''
##### show marker on map #####
'''height = 217
img = cv2.imread('passion.jpg')
origin_x = -4.681169
origin_y = -3.636700

for point in marker_set:
    map_c_x = int((float(point[0])-origin_x)/0.05)
    map_c_y = height - int((float(point[1])-origin_y)/0.05)
    
    cv2.circle(img,(map_c_x, map_c_y), 3, (0, 0, 255), -1)

cv2.imshow('My Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(1)'''
