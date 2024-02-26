import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Streamlit UI
st.title("Train Track Simulation")

# Canvas for drawing or displaying results
canvas_result = st_canvas(
    stroke_width=2,
    stroke_color="#000000",
    background_color="#FFFFFF",
    height=150,
    drawing_mode="freedraw",
    key="canvas",
)

# Display the drawing
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
