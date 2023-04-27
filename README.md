
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

In this project, we successfully detected violent behavior in videos using image processing and CNNs. We used a simple CNN architecture and achieved an accuracy of around 86% with the augmented image data. We can further improve our model's accuracy by experimenting with different architectures and hyperparameters.



## Database Management System
In the Database Management System the trained machine learning model was used to create a SQL databse using the Table format.
**Step 1**: Code for connecting Mysql server and Python is written in the VS Code to establish connection between Mysql database and the ML Model. 

**Step 2**: Creating a Table in MySql Server 8.0 using the Sql workbench and further updating that table using the Sql command line client and the Sql workbench credentials.

**Step 3** : The table created in the Mysql workbench contains four columns i.e. nature of crime, risk factor, location of crime and nearest police station. The data from the Machine learning model i.e. the Pyhton code written in the VS code would be displayed onto the table created everytime any event is triggered.

**Step 4** : The table created would be then exported to the excel format i.e. google spreadsheet format because evetyime the data is updated would then simultaneoulsy be reflected onto the spreadsheet which then further be transferred to the next API process. 

## API
### Step 1:Determine
Determine the Risk percentage for database management system (Risk >50%)
On Identification of (Risk > 50%)  the database management system MySQL a trigger is setup up.
Trigger will set up, such as insert, update.

### Step 2: API
Trigger code that sends the notification when the condition is met.
Use an API to send the notification to an app or SMS, depending on your requirements.
For SMS notifications, use Twilio API: Use API key or credentials to authenticate your requests. Twilio API Start sends SMS
For app notifications, use the Firebase Cloud Messaging (FCM) API for Android, iOS, and web apps. FCM API starts send notifications.

### Step 3: Test
Test the trigger to ensure it works as expected.
Create a test entry in your database that meets the trigger condition to observe the notification being sent.
Postman to test your SMS or app notification API integration to ensure it's working correctly.
Monitor your SMS or app notification logs to ensure the notifications are being sent and received correctly




## GPS
The Crime Dectection Alert System is designed to enhance the security in a particular area by automatically detecting crimes and informing the nearest police station. This is done by finding the geolocation of the camera using its IP address, and then using the coordinates of the camera as input to find the nearest police station within a radius of 2 km.

### Step 1: Geolocate the camera
We first detect the crime then the system geolocates the camera (i.e location of crime) using the IP address of the camera with the help of IP-API.com 

### Step 2: Search for nearby Police Stations
After the location of camera is returned we search for nearby Police staions with the help of Google Cloud API key using the geocoding api and places api services of google.

### Step 3: Informing the nearest Police Station
Once the nearest Police sation is found then the Police authorites are informed about the crime with its location and to take necessary actions.

## Application Development
