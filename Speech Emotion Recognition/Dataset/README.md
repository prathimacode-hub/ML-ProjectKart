# About the data:

Speech audio-only files (16bit, 48kHz .wav) from the RAVDESS. Full dataset of speech and song, audio and video (24.8 GB) available from Zenodo.RAVDESS contains 1440 files: 60 trials per actor x 24 actors = 1440. The RAVDESS contains 24 professional actors (12 female, 12 male), vocalizing two lexically-matched statements in a neutral North American accent. Speech emotions includes calm, happy, sad, angry, fearful, surprise, and disgust expressions. Each expression is produced at two levels of emotional intensity (normal, strong), with an additional neutral expression.

#Dataset:
https://www.kaggle.com/uwrfkaggler/ravdess-emotional-speech-audio

## Columns

~Modality (01 = full-AV, 02 = video-only, 03 = audio-only).
~Vocal channel (01 = speech, 02 = song).
~Emotion (01 = neutral, 02 = calm, 03 = happy, 04 = sad, 05 = angry, 06 = fearful, 07 = disgust, 08 = surprised).
~Emotional intensity (01 = normal, 02 = strong). NOTE: There is no strong intensity for the 'neutral' emotion.
~Statement (01 = "Kids are talking by the door", 02 = "Dogs are sitting by the door").
~Repetition (01 = 1st repetition, 02 = 2nd repetition).
~Actor (01 to 24. Odd numbered actors are male, even numbered actors are female).


Filename example: 03-01-06-01-02-01-12.wav

    -Audio-only (03)
    -Speech (01)
    -Fearful (06)
    -Normal intensity (01)
    -Statement "dogs" (02)
    -1st Repetition (01)
    -12th Actor (12)
    -Female, as the actor ID number is even.



