import streamlit as st
import time
import numpy as np

def main():
    st.set_page_config(page_title="About Us", page_icon="📈")

    # Logo
    logo_file = open('assets/Logo.jpeg', 'rb')
    logo_byte = logo_file.read()
    left_co, cent_co,last_co = st.columns(3)
    with cent_co:
        st.image(logo_byte)

    # Nama Tim
    st.markdown("<h1 style='text-align: center;'>The Explorers</h1>", unsafe_allow_html=True)

    # Deskripsi projek
    st.markdown("<p style='text-align: center;'><b>Guardian Eyes: Automatic Detection of Dangerous Objects in Public Spaces</b> merupakan projek yang dibuat oleh tim <b>The Explorers</b> dalam rangka menyelesaikan tugas akhir dari studi independen kami di Startup Campus. Projek ini terinspirasi dari maraknya tindak kejahatan menggunakan senjata tajam bahkan senjata api, maka kami mendapatkan ide membuat object detection untuk mendeteksi benda-benda berbahaya tersebut.</p>", unsafe_allow_html=True)

    # Siapa Kami
    st.markdown("<h3 style='text-align: center;'>Anggota Tim</h3>", unsafe_allow_html=True)

    # Foto nama asal univ
    left_co_row1, cent_co_row1, last_co_row1 = st.columns(3)
    left_co_row2, cent_co_row2, last_co_row2 = st.columns(3)
    with left_co_row1:
        photo_file = open('assets/alfajri_square.png', 'rb')
        photo_byte = photo_file.read()
        st.image(photo_byte)
        st.markdown("<h5 style='text-align: center;'>Muhammad Asri Alfajri</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Politeknik Negeri Batam</p>", unsafe_allow_html=True)
    with cent_co_row1:
        photo_file = open('assets/nanda_square.jpg', 'rb')
        photo_byte = photo_file.read()
        st.image(photo_byte)
        st.markdown("<h5 style='text-align: center;'>Nanda Eka Suci Ramadan</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Universitas Negeri Jakarta</p>", unsafe_allow_html=True)
    with last_co_row1:
        photo_file = open('assets/ismail_square.jpg', 'rb')
        photo_byte = photo_file.read()
        st.image(photo_byte)
        st.markdown("<h5 style='text-align: center;'>Iis Ismail</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Politeknik Negeri Jakarta</p>", unsafe_allow_html=True)

    with left_co_row2:
        photo_file = open('assets/rifan_square.jpg', 'rb')
        photo_byte = photo_file.read()
        st.image(photo_byte)
        st.markdown("<h5 style='text-align: center;'>Rifan Ahmad R</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Universitas Perjuangan Tasikmalaya</p>", unsafe_allow_html=True)
    with cent_co_row2:
        photo_file = open('assets/elfiede_square.jpg', 'rb')
        photo_byte = photo_file.read()
        st.image(photo_byte)
        st.markdown("<h5 style='text-align: center;'>Elfiede Nirwana S</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Universitas Sumatera Utara</p>", unsafe_allow_html=True)
    with last_co_row2:
        photo_file = open('assets/elsa_square.jpg', 'rb')
        photo_byte = photo_file.read()
        st.image(photo_byte)
        st.markdown("<h5 style='text-align: center;'>Elsa Indriani</h5>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'>Universitas Amikom Purwokerto</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()


