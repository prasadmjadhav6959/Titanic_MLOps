# Titanic MLOps Project

This project automates an end-to-end machine learning pipeline for the Titanic dataset, including data preprocessing, model training, Streamlit app deployment, and data drift monitoring. The pipeline is scheduled to run daily at 12:00 AM UTC using GitHub Actions, with the front-end hosted on Streamlit Cloud and drift detection powered by Alibi Detect.

## Project Overview

The goal is to predict survival on the Titanic using a machine learning model, deploy an interactive Streamlit app for user predictions, and monitor for data drift in incoming inputs. The pipeline includes:

- **Data Preprocessing**: Cleaning and encoding the Titanic dataset.
- **Model Training**: Training a machine learning model and saving artifacts.
- **Streamlit App**: A user-friendly interface for making predictions.
- **Data Drift Monitoring**: Detecting drift in incoming data using Alibi Detect.
- **Automation**: Daily retraining and drift monitoring via GitHub Actions.

## Prerequisites

- **Python**: Version 3.9 or higher.
- **Git and GitHub**: Git installed and a GitHub account with the repository `titanic-streamlit` set up.
- **Titanic Dataset**: Download `train.csv` from [Kaggle](https://www.kaggle.com/c/titanic/data) and place it in the project folder.
- **Libraries**: Install required Python packages using:
  ```bash
  pip install pandas scikit-learn joblib streamlit mlflow alibi-detect
  ```
- **Streamlit Cloud**: Account set up and linked to the `titanic-streamlit` GitHub repository.
- **GitHub Repository**: Initialized in the `titanic-streamlit` folder and pushed to GitHub.

## Folder Structure

```plaintext
titanic-streamlit/
├── app.py                 # Streamlit app for predictions
├── train.py               # Script for data preprocessing and model training
├── monitor.py             # Script for data drift monitoring
├── parse_logs.py          # Script to parse prediction logs
├── train.csv              # Titanic dataset
├── current_inputs.csv     # Generated from prediction logs
├── titanic_model.pkl      # Trained model artifact
├── le_sex.pkl            # Label encoder for 'Sex'
├── le_embarked.pkl       # Label encoder for 'Embarked'
├── requirements.txt       # Python dependencies
├── predictions.log        # Log of user predictions
├── drift_report.txt       # Data drift monitoring report
├── .github/workflows/automate.yml  # GitHub Actions workflow
├── README.md              # This file
```

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/titanic-streamlit.git
   cd titanic-streamlit
   ```

2. **Download Titanic Dataset**:
   - Download `train.csv` from [Kaggle](https://www.kaggle.com/c/titanic/data).
   - Place it in the `titanic-streamlit` folder.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Streamlit Cloud**:
   - Log in to [Streamlit Cloud](https://streamlit.io/cloud).
   - Connect your GitHub repository (`titanic-streamlit`).
   - Deploy `app.py` as the main app file.

5. **Configure GitHub Actions**:
   - Ensure `.github/workflows/automate.yml` is in the repository.
   - The workflow triggers daily at 12:00 AM UTC to run `train.py` and `monitor.py`.

## Usage

### Running Locally
- **Train the Model**:
  ```bash
  python train.py
  ```
  This preprocesses `train.csv`, trains a model, and saves `titanic_model.pkl`, `le_sex.pkl`, and `le_embarked.pkl`.

- **Run the Streamlit App**:
  ```bash
  streamlit run app.py
  ```
  Access the app at `http://localhost:8501` to make predictions.

- **Monitor Data Drift**:
  ```bash
  python monitor.py
  ```
  This checks for drift between `train.csv` and `current_inputs.csv`, saving results to `drift_report.txt`.

- **Parse Prediction Logs**:
  ```bash
  python parse_logs.py
  ```
  This converts `predictions.log` to `current_inputs.csv` for drift monitoring.

### Automation
- The GitHub Actions workflow (`automate.yml`) runs daily at 12:00 AM UTC:
  - Executes `train.py` to retrain the model.
  - Executes `monitor.py` to check for data drift.
  - Commits updated artifacts and reports to the repository.

### Streamlit Cloud
- The Streamlit app is automatically deployed from `app.py` when changes are pushed to the `main` branch.
- Access the app via the URL provided by Streamlit Cloud.

## Files Description

- **`app.py`**: Streamlit app for interactive predictions using the trained model.
- **`train.py`**: Preprocesses data, trains a model, and saves artifacts (`titanic_model.pkl`, `le_sex.pkl`, `le_embarked.pkl`).
- **`monitor.py`**: Uses Alibi Detect to monitor data drift and generates `drift_report.txt`.
- **`parse_logs.py`**: Parses `predictions.log` to create `current_inputs.csv` for drift monitoring.
- **`train.csv`**: The Titanic dataset from Kaggle.
- **`current_inputs.csv`**: Generated from user inputs logged by the Streamlit app.
- **`titanic_model.pkl`**: Saved machine learning model.
- **`le_sex.pkl`, `le_embarked.pkl`**: Label encoders for categorical features.
- **`requirements.txt`**: Lists Python dependencies.
- **`predictions.log`**: Logs user inputs and predictions from the Streamlit app.
- **`drift_report.txt`**: Reports data drift detection results.
- **`.github/workflows/automate.yml`**: GitHub Actions workflow for daily automation.

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Create a Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For issues or questions, open an issue on the [GitHub repository](https://github.com/your-username/titanic-streamlit) or contact [your-email@example.com](mailto:your-email@example.com).