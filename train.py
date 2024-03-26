import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Load and preprocess images
def load_and_preprocess_images(image_paths, target_size):
    images = []
    for path in image_paths:
        img = load_img(path, target_size=target_size)
        img_array = img_to_array(img) / 255.0  # Normalize pixel values
        images.append(img_array)
    return np.array(images)

# Load image paths and corresponding labels
image_paths = [...]  # List of paths to your images
labels = [...]  # List of corresponding labels

# Split data into training and testing sets
X_train_paths, X_test_paths, y_train, y_test = train_test_split(image_paths, labels, test_size=0.2, random_state=42)

# Load and preprocess training and testing images
X_train = load_and_preprocess_images(X_train_paths, target_size=(224, 224))  # Example target size
X_test = load_and_preprocess_images(X_test_paths, target_size=(224, 224))

# Convert labels to numpy arrays
y_train = np.array(y_train)
y_test = np.array(y_test)

# Train your model using X_train and y_train
# Evaluate your model using X_test and y_test
