# Income Prediction Model

## Overview
This project focuses on developing a classification model to predict whether an individual's income is above or below $50,000 using census data. The model was created as part of Udacity's Machine Learning DevOps course. The dataset is publicly available and sourced from the UCI Machine Learning repository.

## Technologies Used
- **Python#**: The primary programming language used for model development and deployment.
- **Scikit-learn**: Utilized to build the to build and train the model.
- **FastAPI**: A modern web framework used to deploy the model as an API, enabling real-time predictions via HTTP requests.
- **Uvicorn**: ASGI server used to run the FastAPI application.

## Skills Demonstrated
- **Supervised Learning Models**: Used logistic regression to predict binary outcomes (income above or below $50K).
- **API Development**: Developed an API with FastAPI to serve the model, allowing users to submit input data and receive predictions via HTTP requests.
- **Model Evaluation**: Evaluated model performance using precision, recall, and F1 score to ensure reliable predictions.