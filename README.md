# CS 201 Data Structures II, Spring 2021
# Final Project: Footprint Calculator
# Group Members:
- _Muhammad Ammar Khan_
- _Ahsan Ali_
- _Wasiq Hussain_
- _Aliza_
-------

The final project for this course required implementation of assigned data structure using application.

## Youtube Demo Link

## Background

Greenhouse emission is one the major crisis the world is facing at the moment caused by factors ranging from automotive, industrial machinery to agricultural practices. Therefore, and urgent demand for solution has risen. With this application we intend to help user identify the footprint consumption for their products and minimize it. 

## ScapeGoat Trees

Scapegoat trees are self-balancing binary search trees. The main idea of the structure is based on the concept of scapegoat. Scapegoat is literally defined as someone who is blamed for the wrongdoings of others. Few insert and delete operations can make the tree unbalanced and to rebalance the tree, scapegoat, a node, is searched. When the scapegoat is found the entire subtree rooted at the scapegoat can be rebuilt at zero cost, in an amortized sense. Scapegoat trees have O(log n) worst-case search time without storing any extra information like red-black trees. 

## Application

The application will provide on the spot footprint calculator to allow user to capture an image using the cellphone camera and hit the compute button to let our algorithm perform carbon and water footprint analyss which will tell they user how sustainable and envionrmental friendly using a footprint health progress bar to make the output interactive. The application designed used image detection method using OCR to detect items and ingredients within food products to estimate carbon and water footprint. These deetected foods are searched in the created scapegoat datastructure to extract the paramaters for rainwater, agircultural feed and undergound water for water fooprint. And similarly CarbonDioxide, SulphurDioxide and Phosphorous Oxides emission for Carbon footprint.

## Application Usage

- About: Details usage and purpose of application
- Calculate: Lead user to calculator

- Upload Image: Loads image into program
- Reset: Clear all entries
- Add Item: Add additional ingredient to detected items
- Compute: Compute the footprint for the given food

## OCR Implementation

## Libraries Used

## References for Dataset Used

- https://science.sciencemag.org/content/suppl/2018/05/30/360.6392.987.DC1
- https://www.kaggle.com/selfvivek/environment-impact-of-food-production
- https://resourcewatch.org/data/explore/Foo_046-Food-Footprint-in-Calories
