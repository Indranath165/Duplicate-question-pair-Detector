<h1>Duplicate-question-pair-Detector</h1>
This repository contains a Python application built with Streamlit that uses a machine learning model to predict if two questions are duplicates or not. The application is trained on the Quora dataset, which is publicly available on Kaggle. Quora is a popular question-and-answer site where users ask, answer, edit, and organize questions. However, due to the large number of users and the similarity of many questions, there is a need to detect duplicate question pairs to improve efficiency and user experience. The problem statement for this project is to develop an automated way of detecting if pairs of question text actually correspond to semantically equivalent queries. 
<img width="957" alt="duplicatequespair" src="https://github.com/Indranath165/Duplicate-question-pair-Detector/assets/121590717/84dbf0e7-24cb-45dc-a6a8-e43cabf81013"><br> <br>
<b>Check out the live demo of this model at</b> <a href="https://indranath165-duplicate-question-pair-detector-main-unspg4.streamlit.app/" target="_blank">https://indranath165-duplicate-question-pair-detector-main-unspg4.streamlit.app/</a>.
<h2>Dataset</h2>
The Quora dataset used for training and evaluation can be found on Kaggle at the following link: <a href="https://www.kaggle.com/competitions/quora-question-pairs/data?select=train.csv.zip" target="_blank">Quora Question Pairs Dataset</a>. The dataset consists of pairs of questions along with labels indicating whether they are duplicates or not.
<h2>Installation</h2>
<ol>
    <li>Clone or download this repository to your local machine.</li>
    <li>Navigate to the project directory: <br> <code>cd Duplicate-question-pair-Detector</code></li>
    <li>Install the required dependencies: <br> <code>pip install -r requirements.txt</code></li>
</ol>
<h2>Usage</h2>
<ol>
    <li>Run the application: <code>streamlit run app.py</code></li>
    <li>The application will launch in your browser. You can now enter two questions into the provided input fields and click the "Predict" button. The application will use the pre-trained machine learning model to predict if the questions are duplicates or not and display the result.</li>
</ol>
<h2>Model Training</h2>
If you are interested in training the machine learning model yourself or experimenting with different models, follow these steps:
<h3>Preprocessing</h3>
<ol>
  <li>Preprocess the data: Implement data preprocessing steps such as cleaning, tokenization, and vectorization.</li>
</ol>
<h3>Training</h3>
<ol>
    <li>Split the dataset: Split the dataset into training and validation sets.</li>
    <li>Train the model: Use the training set to train the machine learning model. You can try various models and techniques such as logistic regression, random forests, or neural networks.</li>
    <li>Evaluate the model: Evaluate the model's performance on the validation set using appropriate evaluation metrics such as accuracy, precision, recall, or F1 score</li>
</ol>
<h3>Saving the Model</h3>
<ol>
    <li>Save the trained model: Save the trained model to disk.</li>
    <li>Replace the pre-trained model file (model.pkl) in the project directory with your trained model file.</li>
</ol>
<h2>Contributions</h2>
Contributions to this project are welcome! If you find any bugs or want to enhance the functionality, please feel free to submit a pull request. Additionally, you can open an issue for any questions or suggestions you may have.
