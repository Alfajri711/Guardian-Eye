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
    # Model yang digunakan
    st.markdown(
        """
            ### 🆕 Model Yolo Versi 8
            Menggunakan model Yolo versi 8 yang merupakan model terbaru yang dikembangkan oleh ultralytics. Diharapkan dengan model terbaru ini dapat memberikan hasil yang maksimal dalam pendeteksian objek. Selain itu, kami melakukan modifikasi layer pada konfigurasi training model.
        """
    )
    model_file = open('assets/model_before.jpeg', 'rb')
    model1_file = open('assets/model_after.jpeg', 'rb')
    model_byte = model_file.read()
    model1_byte = model1_file.read()
    left_co, cent_co = st.columns(2)
    with left_co:
        st.image(model_byte, caption='Model Sebelum Dimodifikasi')
    with cent_co:
        st.image(model1_byte, caption='Model Setelah Dimodifikasi')

    
    # Objek apa saja yang dideteksi
    st.markdown(
        """
            ### 🔪 Objek Yang Dapat Dideteksi
            Kami telah melakukan klasifikasi untuk objek apa saja yang bisa dideteksi pada projek kami. Didapat 6 objek yang bisa dideteksi yaitu, Pisau, Pistol, Kapak, Linggis, Palu, dan Gunting.
        """
    )
    object_file = open('assets/pisau.jpg', 'rb')
    object_byte = object_file.read()
    object1_file = open('assets/pistol.jpg', 'rb')
    object1_byte = object1_file.read()
    object2_file = open('assets/axe.jpg', 'rb')
    object2_byte = object2_file.read()
    left_co_object, cent_co_object,last_co_object = st.columns(3)
    with left_co_object:
        st.image(object_byte)
    with cent_co_object:
        st.image(object1_byte)
    with last_co_object:
        st.image(object2_byte)

    
    object3_file = open('assets/crowbar1.jpg', 'rb')
    object3_byte = object3_file.read()
    object4_file = open('assets/hammer.jpg', 'rb')
    object4_byte = object4_file.read()
    object5_file = open('assets/scissor.jpg', 'rb')
    object5_byte = object5_file.read()
    left_co_object_1, cent_co_object_1,last_co_object_1 = st.columns(3)
    with left_co_object_1:
        st.image(object3_byte)
    with cent_co_object_1:
        st.image(object4_byte)
    with last_co_object_1:
        st.image(object5_byte)

    # Limitasi objek
    st.markdown(
        """
            ### 🔴 Limitasi Objek
            Terlepas dari hasil terbaik yang telah kami usahakan, terdapat limitasi objek yang menyebabkan objek tidak terdeteksi.
        """
    )
    limit_file = open('assets/limit1.jpeg', 'rb')
    limit_byte = limit_file.read()
    limit2_file = open('assets/limit2.jpeg', 'rb')
    limit2_byte = limit2_file.read()
    limit3_file = open('assets/limit3.jpeg', 'rb')
    limit3_byte = limit3_file.read()
    left_co_limit_1, cent_co_limit_1, last_co_limit_1 = st.columns(3)
    with left_co_limit_1:
        st.image(limit_byte, caption="Target terhalang objek lain, sehingga salah terdeteksi bahkan tidak terdeteksi.")
    with cent_co_limit_1:
        st.image(limit2_byte, caption="Posisi target terlalu miring dan terhalang objek lain, sehingga salah terdeteksi.")
    with last_co_limit_1:
        st.image(limit3_byte, caption="Posisi target terlalu miring, sehingga tidak terdeteksi.")


if __name__ == "__main__":
    main()