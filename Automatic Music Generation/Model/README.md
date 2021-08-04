
<br />
<p align="center">
  <h2>Automatic Music Generation with Deep Learning using Wavenet and LSTM</h3>
</p>



<!-- ABOUT THE PROJECT -->
## Introduction

Deep Learning is a field of Machine Learning which is inspired by a human mind and its neural structure. These networks extract features automatically from the dataset and are capable of learning any non-linear function. 
This project proposes the use of 2 models, Wavenet and LSTM.


WaveNet is an audio generative model based on the PixelCNN architecture. In order to deal with long-range temporal dependencies needed for raw audio generation, architectures are developed based on dilated causal convolutions, which exhibit very large receptive fields.


LSTM is a novel recurrent network architecture training with an appropriate gradient-based learning algorithm. LSTM is designed to overcome error back-flow problems.


Dataset: https://www.kaggle.com/anubhavjin/midi-data-containing-melodies
## Wavenet Approach

WaveNet takes the chunk of a raw audio wave as an input. Raw audio wave refers to the representation of a wave in the time series domain. Given the sequence of the amplitude values, WaveNet tries to predict the successive amplitude value.We can infer from the above that the output of every chunk depends only on the past information ( i.e. previous timesteps) but not on the future timesteps. Hence, this task is known as Autoregressive task and the model is known as an Autoregressive model.

## LSTM Approach
Another approach for automatic music generation is based on the Long Short Term Memory (LSTM) model. The preparation of input and output sequences is similar to WaveNet. At each timestep, an amplitude value is fed into the Long Short Term Memory cell – it then computes the hidden vector and passes it on to the next timesteps.

## Comparison
After comapring the output music generated from LSTM and Wavenet, Wavenet produces more melodious and synchronised music.
