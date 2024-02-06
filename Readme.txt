At this project we are detecting the color range we specified and deleting it.

Convert the picture so that only the pixels with green or yellow are retained, while excluding the blue. Set pixels that are within the range of 0 to 255 for the main color and up to 100 for the adjacent colors to black. Specifically, if we talk about the blue color, for example, if our pixel is [200, 98, 98], it should be set to black, i.e., [0, 0, 0].

Set the green sensitivity between 20 and 50 for optimal results.

Set the blue sensitivity between 70 and 100.

Set the red sensitivity between 50 and 100.

As the values decrease, sensitivity increases, with 100 being ideal for all.

