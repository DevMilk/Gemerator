# Gemerator
---
## UPDATE (08/12/2020):

My Google Cloud Credits are over so website cannot display images any more.

---
## UPDATE (15/08/2020): 
---
![alt text](https://github.com/DevMilk/Gemixture/blob/master/gemeratorwebsite.PNG)

- Added Generative adversarial networks to generate more realistic and less mixed gemstone images.
<p style="text-align: center;"><b>https://gemerator.pythonanywhere.com/</b></p>
                                                                                               

I developed a <b >Flask Web Service</b> and a <b>Django Website</b> and deployed them using <b>Google Cloud</b> and <b>PythonAnywhere</b>, every time you refresh the page, my deep autoencoder model generates 80 images of mixed Gemstones.
<br>
</br>


-You can also use my API's to get generated images as a response:


! API for generated mixed gem images with AutoEncoder: https://gemerrator.ey.r.appspot.com/generate

! API for generated gem images with GAN: https://gemerrator.ey.r.appspot.com/GANgenerate    

---
## What is Gemerator?

Gemerator is an autoencoder and GAN based mixed gem image generator, it trained with 87 different gem types, 2800 gem image and tested with 364 gem image.

An autoencoder is a type of artificial neural network used to learn efficient data codings in an unsupervised manner.The aim of an autoencoder is to learn a representation (encoding) for a set of data, typically for dimensionality reduction, by training the network to ignore signal “noise”.

Autoencoder can be used to generate images like GAN, but it uses bottleneck of neural network model to generate new images.

A generative adversarial network is a class of machine learning frameworks. Given a training set, this technique learns to generate new data with the same statistics as the training set.

Generating images can be done by Variational Autoencoders and Generative Adversarial Neural Network. But autoencoders can be used for noise reduction for images, deepfakes, dimensional reduction and also for calculating difference between trained features and given input image.

Other Solutions to improve model: 

1. Generating Generator inputs based on all gem images' color distribution

2. Using convolution, flattening and upsampling in keras model

A website about that project is under development.
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
 

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/feature15compare.png)


Last:

![alt text](https://github.com/DevMilk/Gemixture/blob/master/Generated/last.PNG)
 

It contains 87 gem types:

* Alexandrite

* Almandine

* Amazonite

* Amber

* Amethyst

* Ametrine

* Andalusite

* Andradite

* Aquamarine

* Aventurine

* Aventurine Green

* Benitoite

* Beryl Golden

* Beryl Red

* Bloodstone

* Blue Lace Agate

* Carnelian

* Cats Eye

* Chalcedony

* Chalcedony Blue

* Chrome Diopside

* Chrysoberyl

* Chrysocolla

* Chrysoprase

* Citrine

* Coral

* Danburite

* Diamond

* Diaspore

* Dumortierite

* Emerald

* Fluorite

* Garnet Red

* Goshenite

* Grossular

* Hessonite

* Hiddenite

* Iolite

* Jade

* Jasper

* Kunzite

* Kyanite

* Labradorite

* Lapis Lazuli

* Larimar

* Malachite

* Moonstone

* Morganite

* Onyx Black

* Onyx Green

* Onyx Red

* Opal

* Pearl

* Peridot

* Prehnite

* Pyrite

* Pyrope

* Quartz Beer

* Quartz Lemon

* Quartz Rose

* Quartz Rutilated

* Quartz Smoky

* Rhodochrosite

* Rhodolite

* Rhodonite

* Ruby

* Sapphire Blue

* Sapphire Pink

* Sapphire Purple

* Sapphire Yellow

* Scapolite

* Serpentine

* Sodalite

* Spessartite

* Sphene

* Spinel

* Spodumene

* Sunstone

* Tanzanite

* Tigers Eye

* Topaz

* Tourmaline

* Tsavorite

* Turquoise

* Variscite

* Zircon

* Zoisite
