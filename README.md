# Gemixture
Gemixture is an autoencoder based mixed gem image generator, it trained with 87 different gem types, 28000 gem image and tested with 364 gem image.

An autoencoder is a type of artificial neural network used to learn efficient data codings in an unsupervised manner.The aim of an autoencoder is to learn a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore signal “noise”.

Autoencoder can be used to generate images like GAN, but it uses bottleneck of neural network model to generate new images.

Images resized to 30x30 shape. I used sigmoid function for bottleneck and linear function for other layers, also used "adamax" as optimizer and "mean squared error" for loss function which is suitable for image.


Training loss plot:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/HistoryPlot.png)

Feature size is neuron count in the bottleneck layer aka PCA result

Generated images when featureSize parameter is 10:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature10sigmoidloss0.0176.png)

Generated images when featureSize parameter is 30:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature30sigmoidloss0.0126.png)


Generated images when autoencoder trained with only Amethysts:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature5OnlyAmethyst.png)

Compare of test image and compressed image of test image when featureSize is 15:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature15compare.png)

Generated images when featuresize is 15:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature15sigmoidloss0.0160.pngVER2.png)
