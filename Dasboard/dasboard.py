import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from datetime import datetime

# Load datasets
df1_cleaned = pd.read_csv('Guanyuan_cleaned.csv')
df2_cleaned = pd.read_csv('Aotizhongxin_cleaned.csv')
df3_cleaned = pd.read_csv('Tiantan_cleaned.csv')

# Convert date columns
for df_cleaned in [df1_cleaned, df2_cleaned, df3_cleaned]:
    df_cleaned['year'] = df_cleaned['year'].astype(int)
    df_cleaned['month'] = df_cleaned['month'].astype(int)
    df_cleaned['day'] = df_cleaned['day'].astype(int)
    df_cleaned['hour'] = df_cleaned['hour'].astype(int)
    df_cleaned['date'] = pd.to_datetime(df_cleaned['year'].astype(str) + '-' +
                                        df_cleaned['month'].astype(str) + '-' +
                                        df_cleaned['day'].astype(str))

# PM2.5 trends
pm25_trend_guanyuan = df1_cleaned.groupby('date')['PM2.5'].mean().reset_index()
pm25_trend_aotizhongxin = df2_cleaned.groupby('date')['PM2.5'].mean().reset_index()
pm25_trend_tiantan = df3_cleaned.groupby('date')['PM2.5'].mean().reset_index()

# Streamlit sidebar
st.sidebar.header('Air Quality Dashboard')
st.sidebar.image("Air Quality.png")  

# Date input
min_date = df1_cleaned['date'].min()
max_date = df1_cleaned['date'].max()
date_input = st.sidebar.date_input(
    label='Select Date Range',
    min_value=min_date,
    max_value=max_date,
    value=(min_date, max_date)  # Default to the full range
)

# Check if a single date is selected
if len(date_input) == 1:
    start_date = end_date = date_input[0]
else:
    start_date, end_date = date_input

# Filter data based on the selected date range
filtered_guanyuan = pm25_trend_guanyuan[(pm25_trend_guanyuan['date'] >= pd.Timestamp(start_date)) & 
                                        (pm25_trend_guanyuan['date'] <= pd.Timestamp(end_date))]
filtered_aotizhongxin = pm25_trend_aotizhongxin[(pm25_trend_aotizhongxin['date'] >= pd.Timestamp(start_date)) & 
                                                (pm25_trend_aotizhongxin['date'] <= pd.Timestamp(end_date))]
filtered_tiantan = pm25_trend_tiantan[(pm25_trend_tiantan['date'] >= pd.Timestamp(start_date)) & 
                                        (pm25_trend_tiantan['date'] <= pd.Timestamp(end_date))]

# PM2.5 Trend Over Time
st.title('Air Quality Dashboard :sparkles:')
st.subheader('PM2.5 Trend Over Time')
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(filtered_guanyuan['date'], filtered_guanyuan['PM2.5'], marker='o', color='b', label='Guanyuan')
ax.plot(filtered_aotizhongxin['date'], filtered_aotizhongxin['PM2.5'], marker='o', color='g', label='Aotizhongxin')
ax.plot(filtered_tiantan['date'], filtered_tiantan['PM2.5'], marker='o', color='r', label='Tiantan')
ax.set_title("Tren PM2.5 dari 2013 hingga 2017 untuk Setiap Stasiun", fontsize=16)
ax.set_xlabel("Tanggal")
ax.set_ylabel("Rata-rata PM2.5")
plt.xticks(rotation=45)
plt.grid(True)
ax.legend()
st.pyplot(fig)

# Correlation Analysis
st.subheader('Korelasi antara PM2.5 dan Faktor Lingkungan')
correlation_df_guanyuan = df1_cleaned[['PM2.5', 'TEMP', 'DEWP', 'WSPM']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_df_guanyuan, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Korelasi di Guanyuan', fontsize=16)
st.pyplot(fig)

correlation_df_aotizhongxin = df2_cleaned[['PM2.5', 'TEMP', 'DEWP', 'WSPM']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_df_aotizhongxin, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Korelasi di Aotizhongxin', fontsize=16)
st.pyplot(fig)

correlation_df_tiantan = df3_cleaned[['PM2.5', 'TEMP', 'DEWP', 'WSPM']].corr()
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(correlation_df_tiantan, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
ax.set_title('Korelasi di Tiantan', fontsize=16)
st.pyplot(fig)

# Mean PM2.5 by station
mean_pm25_by_station = pd.DataFrame({
    'Station': ['Guanyuan', 'Aotizhongxin', 'Tiantan'],
    'Mean PM2.5': [
        df1_cleaned['PM2.5'].mean(),
        df2_cleaned['PM2.5'].mean(),
        df3_cleaned['PM2.5'].mean()
    ]
})

st.subheader('Rata-rata PM2.5 Berdasarkan Stasiun')
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(data=mean_pm25_by_station, x='Station', y='Mean PM2.5', palette='Blues')
plt.title('Rata-rata PM2.5 Berdasarkan Stasiun', fontsize=16)
plt.xlabel('Stasiun')
plt.ylabel('Rata-rata PM2.5')
st.pyplot(fig)

# Season categorization
def get_season(month):
    if month in [12, 1, 2]:
        return 'Winter'
    elif month in [3, 4, 5]:
        return 'Spring'
    elif month in [6, 7, 8]:
        return 'Summer'
    else:
        return 'Fall'

for df_cleaned in [df1_cleaned, df2_cleaned, df3_cleaned]:
    df_cleaned['season'] = df_cleaned['month'].apply(get_season)

seasonal_pm25_guanyuan = df1_cleaned.groupby('season')['PM2.5'].mean().reset_index()
seasonal_pm25_aotizhongxin = df2_cleaned.groupby('season')['PM2.5'].mean().reset_index()
seasonal_pm25_tiantan = df3_cleaned.groupby('season')['PM2.5'].mean().reset_index()

seasonal_pm25_combined = pd.DataFrame({
    'Season': seasonal_pm25_guanyuan['season'],
    'Guanyuan': seasonal_pm25_guanyuan['PM2.5'],
    'Aotizhongxin': seasonal_pm25_aotizhongxin['PM2.5'],
    'Tiantan': seasonal_pm25_tiantan['PM2.5']
})

seasonal_pm25_melted = seasonal_pm25_combined.melt(id_vars='Season', var_name='Station', value_name='PM2.5')

st.subheader('Rata-rata PM2.5 Berdasarkan Musim')
fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=seasonal_pm25_melted, x='Season', y='PM2.5', hue='Station', palette='Set2')
plt.title('Rata-rata PM2.5 Berdasarkan Musim untuk Setiap Stasiun', fontsize=16)
plt.xlabel('Musim')
plt.ylabel('Rata-rata PM2.5')
plt.legend(title='Stasiun')
st.pyplot(fig)

# PM2.5 Categories
bins = [0, 50, 100, df1_cleaned['PM2.5'].max()]
labels = ['Low', 'Medium', 'High']

for df_cleaned in [df1_cleaned, df2_cleaned, df3_cleaned]:
    df_cleaned['pm25_category'] = pd.cut(df_cleaned['PM2.5'], bins=bins, labels=labels)

# Combine categories from all stations
air_df_cleaned = pd.concat([df1_cleaned[['pm25_category']], 
                             df2_cleaned[['pm25_category']], 
                             df3_cleaned[['pm25_category']]], 
                            axis=0)

custom_palette = ["#FFCC99","#FF9999", "#99FF99"] 

st.subheader('Distribusi Kategori PM2.5')
fig, ax = plt.subplots(figsize=(8, 5))
air_df_cleaned['pm25_category'].value_counts().plot(kind='bar', ax=ax, color=custom_palette)
plt.title('Distribusi Kategori PM2.5', fontsize=16)
plt.xlabel('Kategori PM2.5')
plt.ylabel('Frekuensi')
st.pyplot(fig)

st.caption('Copyright (c) Elvan 2024')