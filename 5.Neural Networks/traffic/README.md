I experimented with 3 neural network configurations

1) NN
- one hidden layer (256 units) with relu activation
- softmax output layer

What work well: The processing time is fast
What didn't work well: High loss and very low accuracy

2) CNN
- 3x3 32 filters with 2x2 max-pooling
- one hidden layer (256 units) with relu activation
- dropout(0.5)
- softmax output layer

What work well: Improved loss and accuracy compared to NN without convolution
What didn't work well: Long processing time

3) CNN
- 3x3 32 filters with 2x2 max-pooling
- 3x3 64 filters with 2x2 max-pooling
- one hidden layer (256 units) with relu activation
- one hidden layer (128 units) with relu activation
- dropout(0.5)
- softmax output layer

What work well: The loss was low and accuracy was high
What didn't work well: Long processing time
