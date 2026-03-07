import tensorflow as tf
import streamlit as st
import os


path = os.path.join(os.getcwd(), "01 Neural network regression with TensorFlow", "model_2.keras")
print(path)
model = tf.keras.models.load_model(path)

st.title("House Price Predictor")

sq_meters = st.text_input("Metrekare girin", 80)

n_of_room = st.text_input("oda sayısı girin", 3)

if sq_meters and n_of_room:
    if not sq_meters.isdigit() or not n_of_room.isdigit():
        st.error("What the hell did you give me?")

    sq_meters = float(sq_meters)
    n_of_room = float(n_of_room)
    pred = tf.constant([[sq_meters, n_of_room]])
    st.markdown("---")
    st.markdown("**Price:**")
    st.text(f"$ {model.predict(pred)[0][0]:,.0f}")

