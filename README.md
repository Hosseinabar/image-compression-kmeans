# image-compression-kmeans

Kmeans is a simple and well known clustering algorithm, but very useful in many applications.
one of its usecases is image compressing, kind of interesting, let's see how.

An image is made up of many colors, if we use RGB model then each color can be represented as 24 bits (8 bit for each main color) in digital world and there would be a huge space of possible colors, if we could reduce this space somehow then each color would be represented as only 16 or 8 or evern 2 bits hence we would have too smaller images in size.
 
To get this job done, we cluster those colors into k cluster, now there are some colors in each cluster, finally if we have the colors value replaced by the mean of their cluster then there will remain only k colors and that's our desired resault, now the image is consist of only k colors.

Algorithm:
  1. read the image as a vector of RGB values
  2. run kmeans on the RGB values
  3. repalce each RGB with the mean of its cluster
  4. reshape the RGBs into a 2D array of RGBs
  5. save them as .png or something else
