

**Automatic Music Generation**

**GOAL**

To generate automatic music from previous notes.

**DATASET**

https://www.kaggle.com/anubhavjin/midi-data-containing-melodies

**DESCRIPTION**

Deep Learning is a field of Machine Learning which is inspired by a human mind and its neural structure. These networks extract features automatically from the dataset and are capable of learning any non-linear function. 
This project proposes the use of 2 models, Wavenet and LSTM.


WaveNet is an audio generative model based on the PixelCNN architecture. In order to deal with long-range temporal dependencies needed for raw audio generation, architectures are developed based on dilated causal convolutions, which exhibit very large receptive fields.


LSTM is a novel recurrent network architecture training with an appropriate gradient-based learning algorithm. LSTM is designed to overcome error back-flow problems.

**WHAT I HAD DONE**

WaveNet takes the chunk of a raw audio wave as an input. Raw audio wave refers to the representation of a wave in the time series domain. Given the sequence of the amplitude values, WaveNet tries to predict the successive amplitude value.We can infer from the above that the output of every chunk depends only on the past information ( i.e. previous timesteps) but not on the future timesteps. Hence, this task is known as Autoregressive task and the model is known as an Autoregressive model.I created input and  output sequences using music 21 toolkit and passed it through the respective models. The predicted output was then converted to an audio file.

Another approach for automatic music generation is based on the Long Short Term Memory (LSTM) model. The preparation of input and output sequences is similar to WaveNet. At each timestep, an amplitude value is fed into the Long Short Term Memory cell – it then computes the hidden vector and passes it on to the next timesteps.Another approach for automatic music generation is based on the Long Short Term Memory (LSTM) model. The preparation of input and output sequences is similar to WaveNet. At each timestep, an amplitude value is fed into the Long Short Term Memory cell – it then computes the hidden vector and passes it on to the next timesteps. 

**MODELS USED**

Wavenet

LSTM

**LIBRARIES NEEDED**

Music 21 toolkit

Numpy

Keras

Pickle

Pandas

**ACCURACIES**

The Wavenet architecture produces more synchronised and melodious music.


**YOUR NAME**

Pranjal Gadge


