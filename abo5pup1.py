import streamlit as st
import logging
import os
from PIL import Image as PILImage
from pupdatabase import update_product
from abo5s3 import *
import time
import datetime
if 'session' not in st.session_state:
    st.session_state['session'] = 'New Session'

url="https://abo5.s3.eu-central-1.amazonaws.com/"


#Header
st.title('Abo5 Product Collection Portal')

#initiating a form
productform=st.form("product", clear_on_submit=True)

#container

Productnameen = productform.container()
productnamear = productform.container()
Tags = productform.container()
category = productform.container()
subcategory = productform.container()
Retail_outlet = productform.container()
price = productform.container()
Upload = productform.container()

#Image Upload

urllist=[]
uploaded_files = Upload.file_uploader("Take Pictures or browse", type=["png","jpg","jpeg"], accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     #st.write("filename:", uploaded_file.name)
     #st.write(uploaded_file.name)
     save_uploadedfile(uploaded_file)
     s3.Bucket('abo5').upload_file(Filename=uploaded_file.name, Key=uploaded_file.name)
     urllist.append(url+uploaded_file.name)
links = ", ".join(urllist)

#Select Category
Pro_category = category.selectbox(
    'Select Product Category',
    ('Occasions & Holidays', 'Household Gears', 'Antiques & Gifts','Cleaning & Plastics','Personal Care','Stationery & School Supplies','Accessories','MISCELLANEOUS','CLOTHES','FOOD'))

#Pro_subcategory = subcategory.selectbox(
#    'Select Product Sub-Category',
#    ('Utensils', 'Food', 'kitchenware'))

Pro_price = price.text_input('Product-Price', '')

Pro_Retail= Retail_outlet.selectbox('Select Retail Outlet',
                                    ('Store1', 'Store2', 'Store3','Store4'))


#Product Name textbox    
Pro_nameen = Productnameen. text_input('Product Name English', '')
Pro_namear = productnamear.text_input('Product Name Arabic', '')
Pro_Tags = Tags.text_input('Tags', '')


#submit button
if productform.form_submit_button("upload"):
    update_product(Product_Entry_Timestamp=datetime.datetime.now(), Product_Name_en=Pro_nameen, 
                    Product_Name_ar=Pro_namear, Product_Category=Pro_category, 
                    Tags=Pro_Tags,Retail_outlet=Pro_Retail,
                    Product_price=0.00, Product_image_R_url=links)
    st.success("Updated")
    st.balloons()
    #   status=False

