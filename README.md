# AIML426-Project2: EA for optimisation, computer vision, and machine learning
This project delivers the requirements of the Victoria University of Wellington AIML426 - Evolutionary computation and learning (2024 ) project 2.  The goal of this project is to review and practise evolutionary computation technologies for optimisation, computer vision and machine learning.  The project will require:
  - Design evolutionary programming (EP) and evolution strategy (ES) to solve optimisation problems to understand and analyse their behaviour
  - Implement the differential evolution (DE) algorithm and the partical swarm optimisation (PSO) algorithm and study their performance at solving continuous optimisation problems
  - Study the effectiveness of using estimation of distribution (EDA) algorithms for solving combinatorial optimisation problems with properly designed fitness functions
  - Explore genetic programming algorithms for computer vision applications (image classification).

The project comprises four portions:
  1. __Evolutionary programming and evolution strategy:__  Use both EP and ES to minimise two functions, where $D$ is the number of variables, i.e. $x_1, x_2, ..., x_D$, choosing any specific algorithm variations of EP and ES.
  2. __Differential evolution and particle swarm optimisation:__  implement DE algorithm and PSO algortihm and apply to minimise two functions, where $D$ is the number of variables i.e. $x_1, x2, ..., x_D$.
  3. __Estimation of distribution algorithm:__ develop a simple EDA, e.g. base on either the univariate marginal distribution (UDMA) or the population based incremental learning (PBIL) algorithm to solve the 0-1 knapsack problem, for three provided knapsacks.
  4. __Genetic programming for image classification:__  build an image classifier for each dataset that can accurately classify any image into two different classes ('smile' and 'neutral') using:
     - __automatic feature extraction through GP__ (i.e. FLGP) using strongly-typed GP code in python  to automatically learn suitable image features, identify the best feature extractors and interpret why the evolved feature extractors can extract useful features; create two pattern files ('training' and 'test').
     - __image classification using features extracted by GP__, train an image classifier of choice (e.g. Linear SVM or Naive Bayes classifier) using the training data and test its performance on the unseen test data (from previous step).  Using a chosen evaluation criteria (e.g. classification accuracy), measure the performance of the trained classifier on both training and test data.
     - study the best GP trees from the feature extraction step to:
       - identify and briefly describe all the global and local image features that can be extracted by the GP trees,
       - explain why the extracted global and local image features can enable the image classifier to achieve good classification accuracy.
  
