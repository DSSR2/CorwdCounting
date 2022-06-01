# A quick way to count the number of pepole in a crowded image.

## Getting Started
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tt2u-Oki6XO7vM5GKCs5QOtaY17wz98p)

Use the button above to open the notebook in Colab and get started! It's a simple notebook with just two cells. The first cell imports and downloads all the pre-requisites for predictions. The second cell allows you to upload your own image and get a count on the number of people in it. There's also a little heatmap to see how the model makes it's predictions. 

## The Model
The model used to predict the count is taken from the Official Implementation of ["Encoder-Decoder Based Convolutional Neural Networks with Multi-Scale-Aware Modules for Crowd Counting"](https://arxiv.org/abs/2003.05586)