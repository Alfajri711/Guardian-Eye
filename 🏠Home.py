import streamlit as st
from PIL import Image

def main():
    st.set_page_config(
        page_title="Home",
        page_icon="👋",
    )

    st.write("# Guardian Eyes: Automatic Detection of Dangerous Objects in Public Spaces")
    video_file = open('assets/VideoTheExplorers.mp4', 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

    st.markdown(
        """
        Dengan meningkatnya kasus kejahatan yang melibatkan senjata tajam di tempat umum hingga tahun 2022 mencapai 36,6%, keamanan publik menjadi priotitas utama. Untuk mengatasi tantangan ini, kami memperkenalkan proyek Guardian Eyes. Proyek ini menggunakan teknologi YOLO (You Only Look Once) versi 8, sebuah pendekatan terkini dalam deteksi objek dalam citra dan video secara real-time. Dengan memanfaatkan kecerdasan buatan dan deep learning, Guardian Eyes akan memonitor ruang publik secara real-time dan memberikan peringatan dini kepada pihak berwenang ketika mendeteksi keberadaan benda tajam yang mencurigakan. Dengan demikian, proyek ini diharapkan dapat berkontribusi secara signifikan dalam meningkatkan keamanan dan kenyamanan di lingkungan publik.

        ### Benefit
        - Efektifitas dan efisiensi keamanan
        - Pengurangan atau pencegahan tindak kriminal lebih awal
        - Optimalisasi dan solusi keamanan tambahan
    """
    )

if __name__ == "__main__":
    main()