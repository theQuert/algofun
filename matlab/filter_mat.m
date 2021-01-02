clc; clear;

img = imread('mat_im.jpeg');

gray_img = rgb2gray(img);

% h = ones(size(x_g));

% check the size of img
size(gray_img);
I = eye;
% check the size of filter
size(I);
img_input = uint8(img);
% Run the filter with gray_img
filtered_img = imfilter(img_input, I, 'full');
imshow(filtered_img)