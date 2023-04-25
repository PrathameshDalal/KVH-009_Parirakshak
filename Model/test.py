# Import necessary libraries
import cv2
import mysql.connector 
from tensorflow import keras
import numpy as np

from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model

# Load the trained model
model = load_model('modelnew.h5')

try:
    # Connect to the database
    mydb = mysql.connector.connect(
      host="localhost:3306",
      user="root",
      password="",
      database="crimesss"
    )

    # Get a cursor object
    mycursor = mydb.cursor()

    # Define the table name and columns
    table_name = "people"
    columns = ["nature", "risk_level"]
    
    Threshold = 0.25
    Alert = 0.01
    risk = 100
    counter = 0

    # Read in the custom video
    cap = cv2.VideoCapture('V76.mp4')

    # Loop through each frame of the video
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Preprocess the image for input to the model
        frame = cv2.resize(frame, (640, 640))
        rgb = frame
        frame = cv2.resize(frame, (128, 128))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2RGB)
        frame = img_to_array(frame)
        frame = preprocess_input(frame)
        frame = np.expand_dims(frame, axis=0)

        # Use the trained model to predict whether a violent crime is occurring
        prediction = model.predict(frame)[0]
        frame = np.squeeze(frame, axis=0)
        frame = cv2.resize(frame, (480, 480))
        
        if prediction < Threshold:
            counter = counter + 1
            if risk > (prediction*100):
                risk = int((1-prediction)*100)
            cv2.putText(rgb, f"Violent crime detected. Risk Level: {risk} %", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            
        else:
            cv2.putText(rgb, "No violent crime detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            counter = 0
            
        # Display the processed frame
        cv2.imshow("frame", rgb)
        
        if cv2.waitKey(100) == ord('q') or (counter == 60):
            break

    if prediction > Threshold:
        print("Crime Not Detected")
        nature = None
        risk_level = None
    else:
        print("Crime Detected: Nature of Crime - Violence")
        print(f"Risk Factor: {risk} %")
        nature = "Violence- Fight"
        risk_level = risk

    # Define the insert query and values
    sql = "INSERT INTO {} ({}, {}) VALUES (%s, %s)".format(table_name, columns[0], columns[1])
    val = (nature, risk_level)

    # Execute the insert query
    mycursor.execute(sql, val)

    # Commit the changes to the database
    mydb.commit()

except mysql.connector.Error as error:
    print("Failed to insert record into MySQL table:", error)

finally:
    # Release the database connection and cursor
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()
