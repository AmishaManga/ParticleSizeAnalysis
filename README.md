# ParticleSizeAnalysis

A script to process a directory of images. Each image will be a black 800x600 image containing a number of grey circles, representing ore particles.

•	Find all of the ore particles for each image in a directory of images.
•	Produce a histogram indicating particle size distribution in 10 groups/buckets from minimum to maximum particle size.
•	Identify all images that contain particles over a specifiable maximum allowable particle size.

The command-line parameters to be passed to the application are:
•	Path to the images.
•	Maximum allowable particle size (in pixels).

Expected output:
•	Number of ore particles detected.
•	Minimum and maximum particle size.
•	The histogram as a dictionary of groups/buckets and particle counts.
•	A list of all filenames that contain particles over the maximum particle size.
