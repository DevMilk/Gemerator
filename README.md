# Gemixture
Gemixture is an autoencoder based mixed gem image generator, it trained with 87 different gem types, 2800 gem image and tested with 364 gem image.

An autoencoder is a type of artificial neural network used to learn efficient data codings in an unsupervised manner.The aim of an autoencoder is to learn a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore signal “noise”.

Autoencoder can be used to generate images like GAN, but it uses bottleneck of neural network model to generate new images.

Images resized to 30x30 shape. I used sigmoid function for bottleneck and linear function for other layers, also used "adamax" as optimizer and "mean squared error" for loss function which is suitable for image.

If neuron count in bottleneck is low, generated images are more similiar to dimentionally reduced images of real gem images. If
high then dimentionally reduced images are more similiar to real gem images but generated gem images contains more edges etc. so looks less pure.

Generating images can be done by Variational Autoencoders and Generative Adversarial Neural Network. But autoencoders can be used for noise reduction for images, deepfakes, dimensional reduction and also for calculating difference between trained features and given input image.

Other Solutions to improve model: 

1. Generating Generator inputs based on all gem images' color distribution

2. Using convolution, flattening and upsampling in keras model


EXPERIMENTS
 

------------------------------

Feature size is neuron count in the bottleneck layer aka PCA result

Generated images when featureSize parameter is 10:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature10sigmoidloss0.0176.png)

------------------------------

Generated images when featureSize parameter is 30:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature30sigmoidloss0.0126.png)


------------------------------

Generated images when autoencoder trained with only Amethysts:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature5OnlyAmethyst.png)

------------------------------

Compare of test image and compressed image of test image when featureSize is 15:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature15compare.png)


Generated images when featuresize is 15:
![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature15sigmoidloss0.0137.png)
 

It contains 87 gem types:

Alexandrite

Almandine

Amazonite

Amber

Amethyst

Ametrine

Andalusite

Andradite

Aquamarine

Aventurine

Aventurine Green

Benitoite

Beryl Golden

Beryl Red

Bloodstone

Blue Lace Agate

Carnelian

Cats Eye

Chalcedony

Chalcedony Blue

Chrome Diopside

Chrysoberyl

Chrysocolla

Chrysoprase

Citrine

Coral

Danburite

Diamond

Diaspore

Dumortierite

Emerald

Fluorite

Garnet Red

Goshenite

Grossular

Hessonite

Hiddenite

Iolite

Jade

Jasper

Kunzite

Kyanite

Labradorite

Lapis Lazuli

Larimar

Malachite

Moonstone

Morganite

Onyx Black

Onyx Green

Onyx Red

Opal

Pearl

Peridot

Prehnite

Pyrite

Pyrope

Quartz Beer

Quartz Lemon

Quartz Rose

Quartz Rutilated

Quartz Smoky

Rhodochrosite

Rhodolite

Rhodonite

Ruby

Sapphire Blue

Sapphire Pink

Sapphire Purple

Sapphire Yellow

Scapolite

Serpentine

Sodalite

Spessartite

Sphene

Spinel

Spodumene

Sunstone

Tanzanite

Tigers Eye

Topaz

Tourmaline

Tsavorite

Turquoise

Variscite

Zircon

Zoisite
