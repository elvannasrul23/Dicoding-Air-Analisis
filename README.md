# Air Quality Analysis and Dashboard Project

This project aims to analyze air quality data from multiple stations and visualize the results on a Streamlit dashboard.

## Project Setup

### Step 1: Environment Setup
Open your Anaconda PowerShell prompt and activate your environment by typing:  
conda activate main-ds

### Step 2: Create Project Directory
Create a directory for your project:  
mkdir air_analisis  
cd air_analisis

### Step 3: Install Required Libraries
Install the necessary libraries for data analysis and visualization:  
pip install numpy pandas scipy matplotlib seaborn jupyter

### Step 4: Install Streamlit
Install Streamlit for the dashboard application:  
pip install streamlit

### Step 5: Data Analysis with Jupyter Notebook
Run Jupyter Notebook:  

jupyter-notebook .  
Create a new notebook called notebook.ipynb and perform the data analysis using the PRSA datasets found in the Data folder. The datasets are:  
PRSA_Data_Guanyuan_20130301-20170228.csv  
PRSA_Data_Aotizhongxin_20130301-20170228.csv  
PRSA_Data_Tiantan_20130301-20170228.csv  

In the notebook.ipynb, clean the data by removing missing values and correcting date formats, etc. In the last cell, it will save the datasets and change that into the Dashboard folder as:  
Guanyuan_Cleaned.csv    
Aotizhongxin_Cleaned.csv    
Tiantan_Cleaned.csv    
These cleaned datasets will be used in the dashboard.    

### Step 6: Project Folder Structure  
Your project directory should have the following structure:  

air_analisis/  
│  
├── Data/  
│   ├── PRSA_Data_Guanyuan_20130301-20170228.csv  
│   ├── PRSA_Data_Aotizhongxin_20130301-20170228.csv  
│   ├── PRSA_Data_Tiantan_20130301-20170228.csv  
│  
├── Dashboard/  
│   ├── Guanyuan_cleaned.csv  
│   ├── Aotizhongxin_cleaned.csv  
│   ├── Tiantan_cleaned.csv  
│   ├── dashboard.py  
│   └── Air Quality.png  
│  
└── notebook.ipynb  

### Step 7: Running the Dashboard  
Once the analysis is done and the cleaned datasets are saved in the Dashboard folder, you can run the Streamlit dashboard.  

Navigate to the Dashboard folder and execute the following command:  

cd Dashboard   
streamlit run dashboard.py  

### Step 8: Viewing the Dashboard  
Once the above command is run, Streamlit will provide a local URL in the terminal. Open that URL in your web browser to access the interactive dashboard.  

Notes:  
The dashboard will display trends, correlations, and statistical analysis based on PM2.5 air quality data from three stations.  
The image Air Quality.png is required in the Dashboard folder for the sidebar in the Streamlit dashboard.  
