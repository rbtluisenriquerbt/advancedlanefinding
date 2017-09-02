# Advanced Lane Finding
The current project is about finding the road and painting it. Also calculating the curvature.

## Folders
1. notebooks.- Jupyter Notebooks
2. python_progs.- Python Programs
3. media.- Media Data  
a. calibration_images.- Images for Camera Calibration  
b. output_images.- Result Images  
c. output_videos.- Result Videos  
d. test_images.- Test Images  
e. test_videos.- Test Videos  
f. wrapp_images.- Images to Test Wrapper

## Steps
1. Camera Calibration
2. Camera Undistorsion
3. Thresholding
4. Region Selection
5. Image Warping
6. Road Calculation
7. Road UnWarping
8. Road Unwarped + Original Image

> NOTE
> 1. for an step by step explanation please enter notebooks/AdvancedLaneFinding

> 2. When cv2.findChessboardCorners does not work, probably it is because the number of corners you counted inside the square. In the test example is has 9 x 5 corners
