
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('성적 데이터 시각화 앱')  # 앱 제목
st.write('CSV 파일을 업로드하고 다양한 그래프를 그릴 수 있습니다.')

# 1. CSV 파일 업로드
uploaded_file = st.file_uploader('성적 데이터 CSV 파일 업로드', type=['csv'])
df = None
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write('데이터 미리보기:')
    st.dataframe(df)

# 2. 그래프 옵션 선택
st.header('그래프 옵션 선택')
graph_type = st.radio('그래프 종류를 선택하세요', ['히스토그램', '막대그래프', '산점도', '상자그림'])

# 3. 변수 선택 및 그래프 그리기
if df is not None:
    if graph_type == '히스토그램':
        num_cols = df.select_dtypes(include='number').columns.tolist()
        col = st.selectbox('히스토그램을 그릴 변수 선택', num_cols)
        if col:
            fig, ax = plt.subplots()
            sns.histplot(df[col], kde=True, ax=ax)
            ax.set_title(f'{col} 히스토그램')
            st.pyplot(fig)
    elif graph_type == '막대그래프':
        cat_cols = df.select_dtypes(include='object').columns.tolist()
        num_cols = df.select_dtypes(include='number').columns.tolist()
        cat_col = st.selectbox('막대그래프의 범주형 변수 선택', cat_cols)
        num_col = st.selectbox('막대그래프의 수치형 변수 선택', num_cols)
        if cat_col and num_col:
            fig, ax = plt.subplots()
            sns.barplot(x=cat_col, y=num_col, data=df, ax=ax)
            ax.set_title(f'{cat_col}별 {num_col} 막대그래프')
            st.pyplot(fig)
    elif graph_type == '산점도':
        num_cols = df.select_dtypes(include='number').columns.tolist()
        x_col = st.selectbox('X축 변수 선택', num_cols)
        y_col = st.selectbox('Y축 변수 선택', num_cols, index=1 if len(num_cols)>1 else 0)
        if x_col and y_col:
            fig, ax = plt.subplots()
            sns.scatterplot(x=x_col, y=y_col, data=df, ax=ax)
            ax.set_title(f'{x_col} vs {y_col} 산점도')
            st.pyplot(fig)
    elif graph_type == '상자그림':
        num_cols = df.select_dtypes(include='number').columns.tolist()
        cat_cols = df.select_dtypes(include='object').columns.tolist()
        num_col = st.selectbox('상자그림의 수치형 변수 선택', num_cols)
        cat_col = st.selectbox('상자그림의 범주형 변수 선택', cat_cols)
        if num_col and cat_col:
            fig, ax = plt.subplots()
            sns.boxplot(x=cat_col, y=num_col, data=df, ax=ax)
            ax.set_title(f'{cat_col}별 {num_col} 상자그림')
            st.pyplot(fig)
