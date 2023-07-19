import streamlit as st
import pandas as pd
import zipfile
import PIL.Image as Image

#st.set_page_config(layout="wide")

# 큰 제목
st.write('# I ♥ Waffle 🧇')
st.write('**Waffle flamework와 관련된 데이터 기능들을 제공합니다.**')
st.write('---')

# 메인 페이지 Display
def main_page():
    st.write("### ① 이미지 정보보기")
    
    # 서브 페이지로 이동하는 버튼
    if st.button("Viewer"):
        img_view_page()

    st.write("### ② 라벨 정리")
    if st.button("Curation"):
        img_cur_page()

# 이미지와 정보를 볼 수 있는 페이지
def img_view_page():
    # 압축한 이미지를 받는다.
    image_col, json_col = st.columns(2)
    
    with image_col:
        st.header("IMAGE")
        file = st.file_uploader(" 이미지를 압축한 파일을 올려주세요.", type=["zip"])
        
    with json_col:
        st.header("LABEL")
        coco_file = st.file_uploader("coco 라벨링 파일을 올려주세요.", type=["json"])
    
    
    # 메인 페이지로 돌아가는 버튼
    if st.button("메인 페이지로 돌아가기"):
        main_page()

# 이미지를 Curation하는 페이지
def img_cur_page():
    # 압축한 이미지를 받는다.
    image_col_cur, json_col_cur = st.columns(2)
    
    with image_col_cur:
        st.header("IMAGE")
        file = st.file_uploader(" 이미지를 압축한 파일을 올려주세요.", type=["zip"])
        
    with json_col_cur:
        st.header("LABEL")
        coco_file = st.file_uploader("coco 라벨링 파일을 올려주세요.", type=["json"])


    # 메인 페이지로 돌아가는 버튼
    if st.button("메인 페이지로 돌아가기"):
        main_page()
main_page()
        





#st.write('### 이미지 분석')




# view = [100,150,30]
# view

# st.write('# Hello')
# st.write('## hi')
# st.write('### bar chart')


# st.bar_chart(view)
# sview = pd.Series(view)
# sview