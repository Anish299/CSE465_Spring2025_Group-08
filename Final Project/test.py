   import tensorflow as tf
   import pandas as pd
   from sklearn.preprocessing import StandardScaler

   # Load the saved model
   model = tf.keras.models.load_model('trained_model.h5') 

   # Load your test data
   test_data = pd.read_csv('test_data.csv')  # Replace 'test_data.csv' with your test data file

   # Preprocess the test data (same as during training)
   X_test = test_data.drop('EventCKD35', axis=1)  # Replace 'EventCKD35' with your target column name
   scaler = StandardScaler()
   X_test = scaler.fit_transform(X_test)

   # Make predictions
   predictions = model.predict(X_test)

   # Convert predictions to class labels (0 or 1)
   predicted_classes = (predictions > 0.5).astype(int)

   # Add predicted classes to the test data DataFrame
   test_data['Predicted_EventCKD35'] = predicted_classes

   # Save the test data with predictions
   test_data.to_csv('test_data_with_predictions.csv', index=False)

   print("Predictions saved to test_data_with_predictions.csv")
