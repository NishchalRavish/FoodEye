FoodEye
Worried about what's on your plate? Worry no more with FoodEye, an application designed to analyze and classify food items using advanced machine learning models.

About
FoodEye is an innovative application aimed at providing accurate food classification to help users identify various food items on their plates. This application leverages the EfficientNet-B2 model for robust image classification.

Features
Food Classification
Identify different types of food items from images.

Pre-trained Model
Utilizes EfficientNet-B2 for high accuracy.

User-Friendly Interface
Easy to use and interact with.

Installation
To get started with FoodEye, follow these steps:

Clone the repository
git clone https://github.com/NishchalRavish/FoodEye.git
cd FoodEye
		
Create a virtual environment and activate it
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
		
Install the required dependencies
pip install -r requirements.txt
		
Usage
Run the application:

python app.py
		
Follow the instructions on the interface to upload an image and get the classification results.

Model
The model used in this application is EfficientNet-B2, a powerful and efficient deep learning model for image classification. The pre-trained model weights are stored in effnetb2_model.pth.

Dependencies
The project requires the following dependencies, which are listed in requirements.txt:

torch
torchvision
flask
PIL (Pillow)
Ensure all dependencies are installed by running:

pip install -r requirements.txt
		
Contributing
We welcome contributions from the community. To contribute:

Fork the repository.
Create a new branch for your feature or bugfix.
Commit your changes and push the branch to your fork.
Open a pull request with a detailed description of your changes.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Testing
To test the application, go to FoodEye on Hugging Face.
