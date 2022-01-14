# from curses import use_default_colors
# from email.mime import image
# import imghdr
# from turtle import width, window_width
import streamlit as st
# import pandas as pd
# import numpy as np

import time
latest_iteration = st.empty()
bar = st.progress(0)

for percent_complete in range(100):
    time.sleep(0.1)
    bar.progress(percent_complete + 1)

st.balloons()

"""
読み込み完了

"""

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.46, 139.62],
#     columns=['lat', 'lon']
# )
# df

# st.write("Display Image")

from PIL import Image
image = Image.open('sample.jpg')



if st.button('click me!'):
     st.balloons()
# # col1.map(df)

st.image(image, caption='稲村ヶ崎', use_column_width=True)



audio_file = open('20220112.ogg', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')

aaa = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("たまプラーザ", "あざみ野駅前", "フレル鷺沼")
) 

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたが好きな数字は',option,'です'
if(option  == 10):
    st.balloons()

option2 = st.text_input(
    "あなたの趣味を教えてください",
)
# if option2:


# # condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)
# # "コンディション：",condition

col1, col2 = st.columns(2)
button = col1.button("文字を表示")
if button:
    col2.write(
        """
        おりゃ文字だぞこら \n
        見てんのかおい
        """)

expander = st.expander("疲れた方へ...")
expander.write(
    """
    うぇいっ！\n
    ばーかばーか
    """
)
