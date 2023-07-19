
import PIL.Image as Image
import zipfile
from pathlib import Path

import streamlit as st
import pandas as pdx
import natsort
import json
import cv2
import os



# wide하게 설정
st.set_page_config(layout="wide")

# 메인 페이지 인터페이스
st.write('# I ♥ Waffle 🧇')
st.write('***🧇Waffle flamework🧇* 와 관련된 데이터 기능들을 제공합니다.**')
st.write('---')
st.write('## Get Start!  ')
st.write('  ')

def img_view_page():
    # 압축한 이미지를 받는다.
    image_col, json_col = st.columns(2)

# Visualize Function
def visualize(json_path):

    label_list = []

    with open(json_path) as f:
        contents = json.load(f)

        # Put label names in label_list
        for label_mark in contents["categories"]:
            label_list.append(label_mark["name"])  # label list (['cls1', 'cls2', ...])

        # Process each image
        for img_contents in contents["images"]:
            img_id = img_contents["id"]
            img_path =  "images/" + img_contents["file_name"]  # Load image path (coco/images/1.png)
            image_original = cv2.imread(img_path)  # Save original image
            image_result = image_original.copy()  # Output image

            # Process annotations for the current image
            for annotation_contents in contents["annotations"]:
                if img_id == annotation_contents["image_id"]:
                    cls_index = annotation_contents["category_id"] - 1
                    xy_point = annotation_contents["bbox"]  # x, y, width, height

                    # Draw line
                    cv2.rectangle(image_result, (xy_point[0], xy_point[1]), (xy_point[0] + xy_point[2], xy_point[1] + xy_point[3]), (0, 0, 255), 2)

                    # Write Class name
                    text = label_list[cls_index]
                    text_position = (xy_point[0] - 5, xy_point[1] - 5)  # Fix locate
                    cv2.putText(image_result, text, text_position, cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2)

            # Combine Original and Edited Image
            combined_image = cv2.hconcat([image_original, image_result])

            # Make Result folder as output
            result_folder = "result"
            if not os.path.exists(result_folder):
                os.makedirs(result_folder)
            result_image_path = os.path.join(result_folder, os.path.basename(img_path))
            cv2.imwrite(result_image_path, combined_image)  # Save output image
            




# 이미지 압축파일 및 coco annotation form labeled data(coco.json) 을 받는다.
image_col, json_col = st.columns(2)

with image_col:
    st.write("### IMAGE")
    img_zip_file = st.file_uploader(" 이미지를 압축한 파일을 올려주세요.", type=["zip"])
    print(img_zip_file)
    
with json_col:
    st.write("### LABEL")
    coco_file = st.file_uploader("coco 라벨링 파일을 올려주세요.", type=["json"])

# 이미지와 라벨이 모두 업로드 된 경우 진행
if img_zip_file and coco_file :
    st.write("업로드 완료!")

    # 압축 해제 해보자.
    if img_zip_file is not None :
        with open(img_zip_file.name, "wb") as img_file:
            img_file.write(img_zip_file.getbuffer())
        
        with zipfile.ZipFile(img_zip_file.name, "r") as zip_ref:
            zip_ref.extractall("images")        #images폴더 안에 압축해제된 이미지들이 존재

    # Json을 받아보자.
    if coco_file is not None :
        with open(coco_file.name, "wb") as coco_json:
            coco_json.write(coco_file.getbuffer())  #라벨 json파일 저장

    visualize(coco_file.name)







# 서브 페이지 만들 계획이였으나 없어도 될 듯
# # 이미지와 정보를 볼 수 있다. 기본적으로 보여줄 수 있어야함.
# def img_view_page():
#     # 압축한 이미지를 받는다.
#     image_col, json_col = st.columns(2)


# # 이미지를 Curation하는 페이지
# def img_cur_page():
#     # 압축한 이미지를 받는다.
#     image_col_cur, json_col_cur = st.columns(2)








#st.write('### 이미지 분석')




# view = [100,150,30]
# view

# st.write('# Hello')
# st.write('## hi')
# st.write('### bar chart')


# st.bar_chart(view)
# sview = pd.Series(view)
# sview