# Instagram Ad Engagement - Semester Project

## Overview
This repository contains a comprehensive data science project analyzing user interactions with sponsored posts and advertisements on Instagram. The objective is to measure the effectiveness of ad campaigns, investigate specific engagement metrics, evaluate qualitative sentiment using NLP, and engineer a Custom Engagement Scoring Matrix to rank ads based solely on the provided Kaggle dataset.

## Project Structure
```text
├── data/                                 # Central location for your provided dataset
│   └── comments_cleaned.csv              # ✅ Required core Kaggle dataset (Ensured to be placed here)
├── notebooks/                            # Jupyter Notebooks containing partitioned logic
│   ├── 01_Exploratory_Data_Analysis.ipynb# EDA, Visualizations, and Predictive ML Shootout
│   ├── 02_Sentiment_Analysis.ipynb       # NLP scoring of comment polarity (-1.0 to +1.0)
│   └── 03_Feature_Engineering_and_Scoring.ipynb  # Custom engagement ranking logic to sum scores and rank Ad campaigns
├── reports/                              # Automated pipeline output directory (Generates HTML upon executed app.py)
├── src/                                  # Central Application Logic
│   └── app.py                            # Execution script to run the entire pipeline seamlessly
├── requirements.txt                      # Detailed environment dependency listing
└── README.md                             # Project instructions and summaries
```

## Setup and Running the Project Pipeline

This project is built to execute in a single smooth flow, processing everything from the single `comments_cleaned.csv` entry point. 

### Step 1: Install Dependencies
Ensure you have Python 3.8+ installed. Open a terminal directly in this project directory and install the necessary libraries:
```bash
pip install -r requirements.txt
```
*(**Libraries utilized:** pandas, matplotlib, seaborn, scikit-learn, xgboost, lightgbm, textblob (for Sentiment NLP), and jupyter/nbconvert (for report generation).*

### Step 2: Ensure Data is in Place
Please ensure that the `comments_cleaned.csv` dataset is present inside the `/data/` folder. The notebooks will fetch the data relatively using `../data/comments_cleaned.csv` exclusively.

### Step 3: Verify Notebook Kernels (Optional but Recommended)
For the background execution script (`app.py`) to run successfully, each Jupyter Notebook (`.ipynb` files inside `notebooks/`) needs to know which Python kernel to use. If you encounter kernel errors, please open each notebook briefly in VSCode or Jupyter Lab, select your Python environment as the active Kernel, and save the notebook.

### Step 4: Run the Central Pipeline Application
To evaluate the models and parse all visual analysis programmatically, we've provided a single execution pipeline tool via `src/app.py`. 
Run the following command:
```bash
python src/app.py
```
**What does `app.py` do?**
1. It validates that the dataset exists.
2. It iteratively traverses through `Notebook 01`, `02`, and `03` in order.
3. It natively executes the Python kernels computationally in the background.
4. It converts the output of the executed notebooks into elegant standalone HTML files.

### Step 5: View the Reports
Once the script has finished running, navigate to the newly created `/reports/` folder. **For TAs:** Please use the Live Server extension in VS Code to view these HTML reports (`01_Exploratory_Data_Analysis.html`, `02_Sentiment_Analysis.html`, and `03_Feature_Engineering_and_Scoring.html`) on localhost. Right-click the HTML file and select "Open with Live Server" to view the comprehensive graphical representations right inside any web browser without needing to initialize Jupyter!

*(Alternatively, you can manually open and run the `.ipynb` files sequentially inside the `notebooks/` directory using VSCode or Jupyter Lab if you wish to inspect the code cells interactively).*

## Key Findings (Example Output)
- **Time on App & Engagement:** Posting hours dictate hashtag engagement with deep correlations linking comment length to hashtag counts.
- **Advanced Ensemble Modeling (High Distinction):** Engineered a highly performant **Voting Classifier (Soft Ensemble)** combining the power of LightGBM, XGBoost, and Random Forest which outperforms individual architectures. Included multi-model Receiver Operating Characteristic (ROC) curve visualizations to justify model selection explicitly.
- **Modeling Ad Engagement:** The **LightGBM/XGBoost Classifier** systematically processes feature complexities to accurately forecast engagement intent, out-performing linear models like Logistic Regression.
- **Feature Importance:** Advanced tree-based models indicate that `hour_posted` and `comment_length` are the top driving features indicating qualitative ad responses.

## Conclusion
This framework models effective ad strategies by assessing specific textual and temporal user interactions (Emojis/Hashtags). Stakeholders can leverage these best-in-class algorithms to decode the temporal habits and intensity of audience sentiment on Instagram Ad campaigns.