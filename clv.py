from flask import Flask
from flask import render_template
from sklearn.cluster import KMeans
from io import BytesIO
import base64 

import matplotlib.pyplot as plt
import json
import pandas as pd
import numpy as np
import datetime

#匯入模型
from lifetimes import GammaGammaFitter
from lifetimes import BetaGeoFitter

#分店A
def getRFMA():
    # read RFM csv
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSRJAYjbzy0TdmOKPD6Q_ubs9gn1W2iGgSUeyhi81FlBNtyaJvrSIwapi1sxOAb-GCCuvXoElDXzQ70/pub?output=csv')
    # convert Timestamp type to Datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # RFM table
    df['days'] = (datetime.datetime.strptime('2023-12-29', '%Y-%m-%d') - df['Date']).dt.days
    rfm = df.groupby(by=['C_ID']).agg(
        recency=('days', min),
        frequency=('C_ID', 'size'),
        monetary=('SalesAmount', 'mean'),
        senior=('days', max),
        since=('Date', min)
    )
    rfm['log_monetary'] = np.log(rfm['monetary'])
    # print(rfm)
    return rfm


def visualize_rfmA(rfm):
    # 選擇 'frequency'、'log_monetary' 作為特徵
    X = rfm[['frequency', 'log_monetary']]

    # K-means 分群，設定群數為 5
    kmeans = KMeans(n_clusters=5, random_state=2023)
    rfm['cluster'] = kmeans.fit_predict(X)

    # 計算每個群的平均營收貢獻
    rfm['revenue_contribution'] = rfm['frequency'] * rfm['monetary']

    # 繪製泡泡圖
    plt.figure(figsize=(10, 6))
    plt.scatter(
        rfm['frequency'],  # X軸：購買頻率
        rfm['log_monetary'],  # Y軸：平均交易金額（使用對數）
        s=rfm['revenue_contribution'],  # 泡泡大小：營收貢獻
        c=rfm['recency'],  # 泡泡顏色：Recency（越紅代表越久沒來買）
        cmap='RdPu',  # 顏色映射設定為紅色調
        alpha=0.6  # 設定透明度
    )

    plt.xlabel('Frequency(log)')
    plt.ylabel('Average Transaction Amount (log)')
    plt.title('Customer Segmentation')

    plt.colorbar(label='Recency')  # 顏色欄位標籤

    plt.show()

# 假設 rfm 是你之前計算好的 RFM 資料集
     # 保存圖片到 BytesIO
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # 將 BytesIO 轉換成 base64 字串
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

    return img_base64

def getCLVA():
    rfm = getRFMA()
    # 我們定義的平均顧客壽命是6個月
    retain = rfm[rfm['frequency'] > 1]  # 我們只取出購買頻率>1的(不是短期單次的顧客)
    ggf = GammaGammaFitter(penalizer_coef=0.001)
    ggf.fit(retain['frequency'], retain['monetary'])
    conditional_avg_profit = ggf.conditional_expected_average_profit(rfm['frequency'], rfm['recency'])

    bgf = BetaGeoFitter(penalizer_coef=0.1).fit(rfm['frequency'], rfm['recency'], rfm['senior'])

    clv = ggf.customer_lifetime_value(
        bgf,
        rfm['frequency'],
        rfm['recency'],
        rfm['senior'],
        rfm['monetary'],
        time=12,
        discount_rate=0.01
    )

    clv_list = clv.tolist()
    table = []

    for i in range(len(clv)):
        table.append([rfm.index[i], round(clv_list[i], 2)])  # 将 C_ID 加入到结果表格中

    clv_df = pd.DataFrame(table, columns=['C_ID', 'CLV Value'])  # 修改列名为 C_ID
     # 排序CLV表格
    clv_df = clv_df.sort_values(by='CLV Value', ascending=False)


    return clv_df

#分店B
def getRFMB():
    # read RFM csv
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vT6Ym-aRhDhofx9qPDW9LOC-0fVfWUUZ9ObZsCjW675k2C6iJdAHe3uPdsHiFtn7k36xuRx5vRCOX9J/pub?output=csv')
    # convert Timestamp type to Datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # RFM table
    df['days'] = (datetime.datetime.strptime('2023-12-29', '%Y-%m-%d') - df['Date']).dt.days
    rfm = df.groupby(by=['C_ID']).agg(
        recency=('days', min),
        frequency=('C_ID', 'size'),
        monetary=('SalesAmount', 'mean'),
        senior=('days', max),
        since=('Date', min)
    )
    rfm['log_monetary'] = np.log(rfm['monetary'])
    # print(rfm)
    return rfm


def visualize_rfmB(rfm):
    # 選擇 'frequency'、'log_monetary' 作為特徵
    X = rfm[['frequency', 'log_monetary']]

    # K-means 分群，設定群數為 5
    kmeans = KMeans(n_clusters=5, random_state=2023)
    rfm['cluster'] = kmeans.fit_predict(X)

    # 計算每個群的平均營收貢獻
    rfm['revenue_contribution'] = rfm['frequency'] * rfm['monetary']

    # 繪製泡泡圖
    plt.figure(figsize=(10, 6))
    plt.scatter(
        rfm['frequency'],  # X軸：購買頻率
        rfm['log_monetary'],  # Y軸：平均交易金額（使用對數）
        s=rfm['revenue_contribution'],  # 泡泡大小：營收貢獻
        c=rfm['recency'],  # 泡泡顏色：Recency（越紅代表越久沒來買）
        cmap='RdPu',  # 顏色映射設定為紅色調
        alpha=0.6  # 設定透明度
    )

    plt.xlabel('Frequency(log)')
    plt.ylabel('Average Transaction Amount (log)')
    plt.title('Customer Segmentation')

    plt.colorbar(label='Recency')  # 顏色欄位標籤

    plt.show()

# 假設 rfm 是你之前計算好的 RFM 資料集
     # 保存圖片到 BytesIO
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # 將 BytesIO 轉換成 base64 字串
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

    return img_base64

def getCLVB():
    rfm = getRFMB()
    # 我們定義的平均顧客壽命是6個月
    retain = rfm[rfm['frequency'] > 1]  # 我們只取出購買頻率>1的(不是短期單次的顧客)
    ggf = GammaGammaFitter(penalizer_coef=0.001)
    ggf.fit(retain['frequency'], retain['monetary'])
    conditional_avg_profit = ggf.conditional_expected_average_profit(rfm['frequency'], rfm['recency'])

    bgf = BetaGeoFitter(penalizer_coef=0.1).fit(rfm['frequency'], rfm['recency'], rfm['senior'])

    clv = ggf.customer_lifetime_value(
        bgf,
        rfm['frequency'],
        rfm['recency'],
        rfm['senior'],
        rfm['monetary'],
        time=12,
        discount_rate=0.01
    )

    clv_list = clv.tolist()
    table = []

    for i in range(len(clv)):
        table.append([rfm.index[i], round(clv_list[i], 2)])  # 将 C_ID 加入到结果表格中

    clv_df = pd.DataFrame(table, columns=['C_ID', 'CLV Value'])  # 修改列名为 C_ID
     # 排序CLV表格
    clv_df = clv_df.sort_values(by='CLV Value', ascending=False)


    return clv_df

#分店C
def getRFMC():
    # read RFM csv
    df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vRhlswRtM56BMVFrp11ogd1x02wgXO-oFVWp_bdmUyto1u27pTM757L8SNKT1PR0_ES_zh1Tc-XsE5x/pub?output=csv')
    # convert Timestamp type to Datetime
    df['Date'] = pd.to_datetime(df['Date'])
    # RFM table
    df['days'] = (datetime.datetime.strptime('2023-12-29', '%Y-%m-%d') - df['Date']).dt.days
    rfm = df.groupby(by=['C_ID']).agg(
        recency=('days', min),
        frequency=('C_ID', 'size'),
        monetary=('SalesAmount', 'mean'),
        senior=('days', max),
        since=('Date', min)
    )
    rfm['log_monetary'] = np.log(rfm['monetary'])
    # print(rfm)
    return rfm


def visualize_rfmC(rfm):
    # 選擇 'frequency'、'log_monetary' 作為特徵
    X = rfm[['frequency', 'log_monetary']]

    # K-means 分群，設定群數為 5
    kmeans = KMeans(n_clusters=5, random_state=2023)
    rfm['cluster'] = kmeans.fit_predict(X)

    # 計算每個群的平均營收貢獻
    rfm['revenue_contribution'] = rfm['frequency'] * rfm['monetary']

    # 繪製泡泡圖
    plt.figure(figsize=(10, 6))
    plt.scatter(
        rfm['frequency'],  # X軸：購買頻率
        rfm['log_monetary'],  # Y軸：平均交易金額（使用對數）
        s=rfm['revenue_contribution'],  # 泡泡大小：營收貢獻
        c=rfm['recency'],  # 泡泡顏色：Recency（越紅代表越久沒來買）
        cmap='RdPu',  # 顏色映射設定為紅色調
        alpha=0.6  # 設定透明度
    )

    plt.xlabel('Frequency(log)')
    plt.ylabel('Average Transaction Amount (log)')
    plt.title('Customer Segmentation')

    plt.colorbar(label='Recency')  # 顏色欄位標籤

    plt.show()

# 假設 rfm 是你之前計算好的 RFM 資料集
     # 保存圖片到 BytesIO
    img_buf = BytesIO()
    plt.savefig(img_buf, format='png')
    img_buf.seek(0)

    # 將 BytesIO 轉換成 base64 字串
    img_base64 = base64.b64encode(img_buf.read()).decode('utf-8')

    return img_base64

def getCLVC():
    rfm = getRFMC()
    # 我們定義的平均顧客壽命是6個月
    retain = rfm[rfm['frequency'] > 1]  # 我們只取出購買頻率>1的(不是短期單次的顧客)
    ggf = GammaGammaFitter(penalizer_coef=0.01)
    ggf.fit(retain['frequency'], retain['monetary'])
    conditional_avg_profit = ggf.conditional_expected_average_profit(rfm['frequency'], rfm['recency'])

    bgf = BetaGeoFitter(penalizer_coef=0.1).fit(rfm['frequency'], rfm['recency'], rfm['senior'])

    clv = ggf.customer_lifetime_value(
        bgf,
        rfm['frequency'],
        rfm['recency'],
        rfm['senior'],
        rfm['monetary'],
        time=12,
        discount_rate=0.01
    )

    clv_list = clv.tolist()
    table = []

    for i in range(len(clv)):
        table.append([rfm.index[i], round(clv_list[i], 2)])  # 将 C_ID 加入到结果表格中

    clv_df = pd.DataFrame(table, columns=['C_ID', 'CLV Value'])  # 修改列名为 C_ID
     # 排序CLV表格
    clv_df = clv_df.sort_values(by='CLV Value', ascending=False)


    return clv_df