# Model Card

## Model Details

This model was developed through the Udacity Machine Learning DevOps course on September 10th, 2024. It is a classification model trained on publicly available Census Bureau data. It uses logistic regression and the scikit-learn library.

## Intended Use

This model is intended to be used to predict an individual's income level and if it is above or below $50K based on the Census Bureau data. It could be used for research or marketing purposes.

## Training Data

The training data with over 32k records was gathered from the UCI Machine Learning repository.

## Evaluation Data

Twenty percent of the dataset was used for evaluation and processed using the process_data function.

## Metrics

The model's performance was evaluated using precision, recall, and the F1 score. The model's precision was 0.7391, the recall was 0.6384, and the F1 score was 0.6851.

## Ethical Considerations

It is important to ensure the model follows any and all privacy regulations because it is working with personal information such as income and demographics. The model could also be biased based on out of date information.

## Caveats and Recommendations

It is recommmended that the model is retrained on a newed dataset to ensure it is able to make accurate real world predictions. 