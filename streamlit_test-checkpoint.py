import pandas as pd
import streamlit as st
from io import BytesIO
from PIL import Image
import os

import numpy as np


st.title("Welcome to Biophilic Art style Selection!")

instructions = """Upload your own Biophilic Art. 
                  The image you upload will be fed through the Deep Neural Network in real-time
                  and the output will be displayed to the screen.
                  """
st.write(instructions)
file = st.file_uploader('Upload An Image')

st.title("Here is the image you've selected")
if file:# if user uploaded file
        img = Image.open(file)
        resized_image = img.resize((336, 336))
        st.image(resized_image)
st.title("Here is the Biophilic Art Style for the uploaded Image")
df = pd.DataFrame(data=np.zeros((5, 2)),
                  columns=['Biophilic Art Style', 'Confidence Level'],
                  index=np.linspace(1, 5, 5, dtype=int))

