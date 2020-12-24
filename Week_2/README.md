# Week_2 Image and video compression

## JPEG

In week 2, we are going to learn image compression by JPEG, which is probably the most important image processing algorithm overall. Its procedure is attatched below.

<div align="center"> 

![JPEG_procedure](./Image/JPEG.jpg)
(Picture 0) 
</div>

## Construct n x n subimages
In this stage, we are going to cut the image into several blocks, and each one of these blocks has n x n pixels. You can chose what's the value of N, but basically jpeg uses 8 x 8 block. It's easy for a greyscale image because you only have one channel, but for colour image, which has 3 channels of RGB, we just do the same thing to each of them. 

But normally, there are a lot of coorelation between the channels, so jpeg, instead of calling RGB, goes to another dimention called Y, Cb, CR. It is an easy transform, and you can easily get information on the internet but here we just focus on jpeg. Now we've got an image in Y, Cb, CR domain, and the next step will be doing a Forward transform called Discrete Cosine Transform(DCT).

<br>

## Forward transform
Before DCT, let's talk about why we need to do a forward transform, and introduce Karhunen-Loeve transform(KLT). 

First of all, let us explain how do we measure the error that we create in images when we're doing a lossy compression. The basic idea is that the way we measure error is called mean squared error(MSE).

Now, why are we going to do a transform ? Our goal is to compress the image as much as we could and send it out. By doing so, we try to transmit just only one pixel to represent a 8x8 block. Obviously, we should get a tremendous  error in MSE by sending only one pixel. But, we might be able to transform the original 8x8 block into a different 8x8 block in different domain which should be reversable to achieve this goal, and this is the reason why we are doing a forward transform.

There is a transform that allows us to take only the first pixel and still could get the smallest MSE called the Karhunen-Loeve transform(KLT). But, it has a major problem of its speed. It's very slow, and it can not allow us to do thing on the fly as the data is passing. So to solve this problem, we are going to replace the optimal one, Karhunen-Loeve transform, into the the suboptimal one, Discrete Cosine Transform(DCT).

Why Discrete Cosine Transform? Why not Fourier Transform(FT) or any other transforms? There is a couple of reasons why we use the DCT. One of them is that, although we want to do a Karhunen-Loeve transform, we need to do a DCT. It turns out that the DCT is for particular cases, actually exactly equal to the Karhunen-Loeve transform. Those particular cases are when the images what's called Markovian. 

Another sensable reason is that FT has a underlying assumption of periodicity. It assumes that an image repeats itself, but apparently it's not gonna happen in each image or even in our nxn block. For example, look at the upper curve in the Picture 1. You may notice the discontinuity between the boundary points, which makes FT no sense in this situation.

<div align="center"> 

![why_DCT](./image/why_dct.png)

(Picture 1) 
</div>
<br>

How about DCT? Does it do better than FT? Let's see the formula for DCT.
<div align="center">

We assume that we have a NxN image, and its grey value on the position (x,y) is f(x,y)
![DCT_formula](./image/dct_formula.png)

(Formula 1)
</div>

Let's start with 1D array. Now, let's just focus on first cosine function and ignore other parameters and constants. The formula of the cosine function is attached below.
<div align="center">

![cosine_function](./image/cosine_function.png)

(Formula 2)
</div>

By running cosine_value.py, we can get an result of that signs and values of the outcome of the cosine function are almost symmetrical. For i = 0, the outcome always eqauls to 1, which means we will get all information without scaling or noise. For i = 1, it becomes the first 4 elements minus the last 4. Then, you may notice the sign of outcomes change faster as the increase of the value of i.

<div align="center">

![cosine_value](./image/cosine_value.png)

(Picture 2)
</div>

Until now we already know the underlying significance of cosine function is basically weighting and reversing some pixels in a approximately symmetrical way. Let's go back to the context of processing an image, using the equation from Formula 1 but just ignore the coefficent and the parameters related to j and y, which looks like Formula 3. 

<div align="center">

![without_y_j](./image/without_y_j.png)

(Formula 3)
</div>

When the value of i equals to one, we will get an original image. When the value of i comes to 1, we use the first 4 pixels minus the last 4, so if we get a great number from the Formula 3 it means that the grey value within this region changes significantly, and we may can consider this region as an image with noise or edges. In contrast, if we get a low number from the Formula 3, it means that this region is basically a smooth, constant part of the picture.

So, what about we get a large value from the Formula 3 when the value of i is quite high? Let's pay attention on the last table in Picture 2. Signs of adjacent outcomes change superfast(or you can say the frequency is high), which means comparing with i=1, if we still get a great value from the Formula 3, the possibility of getting edges or noise in this region is much higher(because most of the grey value of edges or noise change significantly even in a small region or adjacent pixels). And maybe that's the reason why people consider high frequency region as the place that edges and noise existing.

Combining all the things above together, we can make a conclusion of that if an array in x-domain(spacial domain) is an approximately constant background, we will only get a relatively higher value in the beginning of i-domain(frequency domain) array and rest of the value in this i-domain array should be low. On the other hand, we will have a large number in i-domain if the x-domain array has a high variation, where the edges or noise may exist.

Now, we can just put all the things back to the formula, and its concept is exactly the same with the easier version, because most of them are constant or close to constant. Firtly, We just take the grey value from special domain. Secondly, use cosine function to weigh and reverse it. Finally, multiply them with some coefficents to get the result. The value situated in the upper-left corner called DC value should have a relatively higher value to the others due to the formula. As the coordination move from the upper-left corner to the lower-right corner, the value in the position should be getting lower and lower, until 0. 

<br>

## Quantization
why are we doing quantization? We are doing quantization because we are going to do Huffman coding after that. And remember, in Huffman coding, we want a non-uniform distribution. We want some coefficients to appear a lot, so we're going to give a short code, and some coefficients to appear not much, so we can give them a long code. for example, if we quantize a load, we might find out that 7, 8, 9, 10 all become 0. And then we're going to be able to basically compress a lot

<br>

## Huffman coding

This is a sort of prefix-free code which will simplify the process of reconstructuring the original signal and save the memory with a very simple conputation. 
![Huffman_intro](./Image/Huffman_coding_1.JPG)
<div align="center"> (Picture 1) </div>

<br>

![Huffman_practise](./Image/Huffman_coding_1.JPG)
<div align="center"> (Picture 2) </div>

For example, look at the column Code, and you might notice that there is always a digit that is different from the other digits in every column. When the decoder receives the first digit which is one, then the decoder should know that its no need to wait for another digit to identify which symbol it is. 

Otherwise, in the same context, if the first digit that decoder receives is zero, then it should wait for another digit to determine whether it should stop waiting or not. And so on, until we are able to indentify every symbol in the list.

