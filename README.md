
# Crime Dectection Alert System

## Summary 

The Kotlin-based application is designed to improve the response time of police responders in the event of a crime. The application uses machine learning to detect the nature of the crime, risk level, and GPS coordinates of the CCTV where the crime has been detected. This information is then used to alert the nearest police station, allowing for a faster response time.

Each crime incident is stored in a database table, which includes the associated nature of the crime and risk level. This information is valuable for analyzing crime trends and patterns over time, allowing authorities to make more informed decisions and take proactive measures to prevent future incidents.

Whenever a new crime incident is added to the database, an alert is triggered in the application in the form of an SMS and push notification. This ensures that authorities are notified of the crime as soon as possible, further improving the response time.

Overall, the Kotlin-based application is an innovative and effective way to improve the efficiency of law enforcement agencies and promote safer communities.


### This Project is Divided into 6 Major Parts
1. Image Pre-Processing
2. Machine Learning Model
3. Database Management
4. GPS
5. API
6. App Development

## Image Pre-Processing
This project aims to detect violent behavior in videos using image processing and Convolutional Neural Networks (CNNs). The dataset used in this project is called **"A Dataset for Automatic Violence Detection in Videos"**, which contains videos with both violent and non-violent behaviors.

## Prerequisites
1. TensorFlow 
2. imgextract
3. opencv-python
4. scikit-learn
5. moviepy
6. matplotlib

## Data Preprocessing

### Step 1: Clone the Dataset
Clone the [A-Dataset-for-Automatic-Violence-Detection-in-Videos](https://github.com/airtlab/A-Dataset-for-Automatic-Violence-Detection-in-Videos) repository to get the dataset.

### Step 2: Extract Frames from Videos
We extracted frames from each video to create our dataset. We wrote an `Extractor` class to do this, and then used multiprocessing to extract frames from all of the videos in the dataset. This step generated a large number of images in a training directory.

### Step 3: Organize Images
We then organized the extracted frames by creating two directories for our training data - one for violent images and one for non-violent images. 
The images are organized into `V` and `NV` directories based on their corresponding video labels.

### Step 4: Image Augmentation
We applied image augmentation techniques such as rotation, width shift, height shift, horizontal flip, and shear to increase the diversity of the training data.

## Machine Learning 
## Building the Model

### Step 1: Model Architecture
We used a simple CNN architecture consisting of 4 Convolutional layers and 2 Fully Connected layers. The final layer used a sigmoid activation function to give us the probability of the image being violent or non-violent.

### Step 2: Model Compilation and Training
We compiled our model with binary cross-entropy as the loss function and used the Adam optimizer. We trained our model using our augmented image data and achieved an accuracy of around 90%.

### Step 3: Saving the Model
We saved our trained model in the Keras format using the `model.save()` function.

## Conclusion
In this project, we successfully detected violent behavior in videos using image processing and CNNs. We used a simple CNN architecture and achieved an accuracy of around 90% with the augmented image data. We can further improve our model's accuracy by experimenting with different architectures and hyperparameters.

## Database Management System

## API

## GPS

## Application Development
