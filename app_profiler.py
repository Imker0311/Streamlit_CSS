import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page — Imker Hoogenhout")

# Collect basic information
name = "Mr. JI Hoogenhout"
field = "Chemical Engineering"
institution = "University of Stellenbosch"
company = "Sappi"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")
st.write(f"**Company / Industry Collaboration:** {company}")

st.image(
    "https://images.ctfassets.net/mrbo2ykgx5lt/31352/612d7a43dcca06b795970c28aa2d4f04/chemical-engineer-chemistry-industry-zeolite-ionic-polymer-e1567409711514.jpg?&w=912&fm=webp&q=80",
    caption="Guy making a bomb or meth or something chemical engineers do"
)

# ===== Thesis 1: Predictive Modelling of Chemical Recovery =====
st.header("Masters Thesis: Predictive Modelling of Chemical Recovery in a Pulp Mill")
st.write(
    """
This research will focus on predicting chemical recovery efficiency in pulp mills using advanced data-driven models. The goal will be to optimize recovery rates, reduce waste, and improve energy efficiency. I will analyze historical mill data, apply predictive modelling techniques, and validate models against real plant data. Additionally, I will be developing first-principle models of the process to better understand the underlying chemical and physical phenomena. This work will be carried out in collaboration with Sappi, aiming to provide actionable insights for industrial operations.
"""
)

# Placeholder images for thesis 1
st.subheader("Figures / Diagrams")
col1, col2 = st.columns(2)
with col1:
    st.image("https://cisp.cachefly.net/assets/articles/images/resized/0001023333_resized_enonlinesappisaicor0920221022.jpg", caption="Pulp and Paper Mill (Sappi)")
with col2:
    st.image("https://paperpulpingmachine.com/wp-content/uploads/2018/10/black-liquor.jpg", caption="Black Liquor Used for Energy Recovery")


# ===== Thesis 2: Fault Detection and Diagnosis =====
st.header("Undergrad Thesis: Comparison of Autoencoders and UMAP for Fault Detection and Diagnosis")
st.write(
    """
This research compared **autoencoders** and **UMAP (Uniform Manifold Approximation and Projection)** techniques for fault detection in industrial chemical processes.
The goal was to automatically detect anomalies, identify potential faults, and improve plant reliability.
The study included data preprocessing, model training, and evaluation against real operational datasets.
The research was conducted with a focus on industrial applicability for chemical recovery processes at **Sappi**.
"""
)

# Placeholder images for thesis 2 (2x2 grid)
st.subheader("Figures / Diagrams")
col1, col2 = st.columns(2)
with col1:
    st.image("UMAP_3d_poster_v3.png", caption="Uniform Manifold Approximation and Projection")
    
with col2:
    st.image("PCA_visual.png", caption="Principle Component Analysis")
    st.image("Fully Connected AE.jpg", caption="Fully Connected Autoencoder")


# ===== Contact Section =====
st.header("Contact Information")
email = "imker0311@gmail.com"
st.write(f"You can reach {name} at {email}.")

# ===== GitHub / Projects Section =====
st.header("Projects / GitHub")
github_link = "https://github.com/Imker0311/FYP478"
st.markdown(f"[View my project on GitHub]({github_link})")


