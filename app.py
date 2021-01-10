import os
import streamlit as st 
# EDA Pkgs
import pandas as pd 
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
# Viz Pkgs
import matplotlib
matplotlib.use('Agg')
from PIL import Image


image_DVJ = Image.open('diveera.jpg')
image_JR = Image.open('jeevanraksha.jpg')
image_UM= Image.open('urjitam.jpg')
image_HT = Image.open('harbal tea.jpg')
image_NU = Image.open('nariurja.jpg')
    
#restults_df = restults_df.sort_values(by='RMSE', ascending=False).reset_index()

def main():
	""" UNICARE ML Dataset Explorer """
	st.title("UNICARE PRODUCT DETAILS")
	st.subheader("Unicare treatment with Medicine")

	html_temp = """
	<div style="background-color:tomato;"><p style="color:white;font-size:30px;padding:10px">Unicare Total Health Solution</p></div>
	"""
	st.markdown(html_temp,unsafe_allow_html=True)


    # Read Data
	df = pd.read_csv('product_details.csv')
	
	
	
	# Show Dataset

	if st.checkbox("Show Dataset"):
		
		st.dataframe(df)

	# S
	
	st.subheader("DETAIS OF UNICARE PRODUCT")
	#all_columns_names = df_data.columns.tolist()
	type_of_model = st.selectbox("Select Type of model",["DIVEERA JUICE","JEEVANRAKSHA SYRUP","HARBAL TEA","NARI URJA"])

	if st.button("Unicare product list"):
		#st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

		# Plot By Streamlit
		if type_of_model == 'DIVEERA JUICE':
			#cust_data = df[selected_columns_names]
			#st.write(results_lin)
			st.image(image_DVJ)

		elif type_of_model == 'HARBAL TEA':
			#cust_data = df[selected_columns_names]
			#st.write(results_ran)
			st.image(image_HT)
			
		elif type_of_model == 'JEEVANRAKSHA SYRUP':
			#cust_data = df[selected_columns_names]
			#st.write(results_XG)
			st.image(image_JR)
			
        
		# Custom Plot 
		elif type_of_model:
			#cust_model= df_data[selected_columns_names].plot(kind=type_of_model)
			#st.write(results_)
			st.image(image_NU)
			#st.pyplot()

	if st.button("CHILD PRODUCT:URJITTAM"):
		#st.write(results)
		st.image(image_UM)
		
	
	st.header("CONTACT US:NITIN SIR-9220914632/ 7400364712")	
    
	
	st.sidebar.header("About App")
	st.sidebar.info("A Simple EDA App for Exploring Common ML Dataset")

	st.sidebar.header("Get Datasets")
	st.sidebar.markdown("[Common ML Dataset Repo]("")")

	st.sidebar.header("About")
	st.sidebar.info("nitin faye@uttakarsh")
	st.sidebar.text("CONTACT:9220914632/ 7400364712")
	st.sidebar.text("Maintained by Nitin Faye")


if __name__ == '__main__':
	main()

