# importing the libraries
import os
import pandas as pd
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Get the directory of the current script
current_directory = os.path.dirname(__file__)

# loading the models
diabetes_model_path = os.path.join(current_directory, "diabetes_model.pkl")
diabetes = pickle.load(open(diabetes_model_path, "rb"))

heart_disease_model_path = os.path.join(current_directory, "heart_disease_model.pkl")
heart_disease = pickle.load(open(heart_disease_model_path, "rb"))

parkinsons_model_path = os.path.join(current_directory, "parkinsons_model.pkl")
parkinsons_disease = pickle.load(open(parkinsons_model_path, "rb"))

breast_cancer_model_path = os.path.join(current_directory, "breast_cancer_model.pkl")
breast_cancer = pickle.load(open(breast_cancer_model_path, "rb"))

lung_cancer_model_path = os.path.join(current_directory, "lung_cancer_model.pkl")
lung_cancer = pickle.load(open(lung_cancer_model_path, "rb"))
