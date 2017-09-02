# Advanced Lane Finding

The current project is about finding the road and painting it. Also calculating the curvature.

# Steps
1. Camera Calibration
2. Camera Undistorsion
3. Thresholding
4. Region Selection
5. Image Warping
6. Road Image Calculation
7. Road UnWarping
8. Road Unwarped + Original Image

> NOTE
> 1. When cv2.findChessboardCorners does not work, probably it is because the number of corners you counted inside the square. In the test example is has 8 x 4 corners
