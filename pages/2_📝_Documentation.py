import streamlit as st
import time
import numpy as np

st.set_page_config(page_title="Documentation", page_icon="📈")

st.markdown("# Documentation Of Code")
st.caption("Pada bagian ini berisi kode dan fungsi yang kami gunakan untuk melalukan deployment projek.")

# deteksi foto
st.markdown("<h3>Kode Untuk Deteksi Foto</h3>", unsafe_allow_html=True)

# input foto
st.markdown("<h5>Upload Foto</h5>", unsafe_allow_html=True)
code_image_upload = '''
source_img = st.file_uploader(
        "Upload an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
'''
st.code(code_image_upload, language='python')
# input nilai confidence
st.markdown("<h5>Input Nilai Confidence</h5>", unsafe_allow_html=True)
code_image_confidence = '''
confidence = float(st.slider(key="image_confidence",
        label="Select Model Confidence", min_value=25, max_value=100, value=40)) / 100
'''
st.code(code_image_confidence, language='python')
# cek model
st.markdown("<h5>Cek Ketersediaan Model</h5>", unsafe_allow_html=True)
code_image_model = '''
try:
    model_image = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model for images. Check the specified path: {model_path}")
    st.error(ex)

'''
st.code(code_image_model, language='python')

# Untuk fungsi deteksi
st.markdown("<h5>Fungsi Deteksi Foto</h5>", unsafe_allow_html=True)
code_image_detection = '''
if st.button('Detect Objects in Image'):
    if source_img:
        # Process the image and get detection results
        res_image = model_image.predict(uploaded_image, conf=confidence)
        boxes_image = res_image[0].boxes
        res_plotted_image = res_image[0].plot()[:, :, ::-1]
        with col2:
            st.image(res_plotted_image,
                    caption='Detected Image',
                    use_column_width=True
                    )
            try:
                with st.expander("Detection Results for Image"):
                    for box_image in boxes_image:
                        st.write(box_image.xywh)
            except Exception as ex:
                st.write("No image is uploaded yet!")
'''
st.code(code_image_detection, language='python')

st.markdown("""---""")

# deteksi video
st.markdown("<h3>Kode Untuk Deteksi Video</h3>", unsafe_allow_html=True)

# input video
st.markdown("<h5>Upload Video</h5>", unsafe_allow_html=True)
code_video_upload = '''
source_video = st.file_uploader(
        "Upload a video...", type=("mp4", "avi", "mov", "mkv"))
'''
st.code(code_video_upload, language='python')
# input nilai confidence
st.markdown("<h5>Input Nilai Confidence</h5>", unsafe_allow_html=True)
code_video_confidence = '''
confidence_video = float(st.slider(key="video_confidence",
        label="Select Model Confidence", min_value=25, max_value=100, value=40)) / 100
'''
st.code(code_video_confidence, language='python')
# cek model
st.markdown("<h5>Cek Ketersediaan Model</h5>", unsafe_allow_html=True)
code_video_model = '''
try:
    model_video = YOLO(model_path)
except Exception as ex:
    st.error(f"Unable to load model for videos. Check the specified path: {model_path}")
    st.error(ex)

'''
st.code(code_video_model, language='python')

# Untuk fungsi deteksi
st.markdown("<h5>Fungsi Deteksi Video</h5>", unsafe_allow_html=True)
code_video_detection = '''
if st.button('Detect Objects in Video'):
    if source_video:
        with col4:
            try:
                with tempfile.NamedTemporaryFile() as f:
                    f.write(source_video.read())
                    f.flush()
                    vid_cap = cv2.VideoCapture(f.name)

                if not vid_cap.isOpened():
                    print("Could not open video file")
                    return

                st_frame = st.empty()
                while (vid_cap.isOpened()):
                    success, image = vid_cap.read()
                    if success:
                        _display_detected_frames(confidence_video,
                                                model_video,
                                                st_frame,
                                                image,
                                                )
                    else:
                        vid_cap.release()
                        break
            except Exception as e:
                st.sidebar.error("Error loading video: " + str(e))
'''
st.code(code_video_detection, language='python')

st.markdown("""---""")

# fungsi menampilkan frame video
st.markdown("<h3>Fungsi Tambahan</h3>", unsafe_allow_html=True)
st.markdown("<h5>Fungsi Untuk Menampilkan Frame Hasil Deteksi Video</h5>", unsafe_allow_html=True)
st.markdown(
    """
    Kode ini menggunakan referensi dari sebuah repositry github berikut. [CodingMantras/yolov8-streamlit-detection-tracking](https://github.com/CodingMantras/yolov8-streamlit-detection-tracking/blob/master/helper.py)
"""
)
code_video_detection = '''
def _display_detected_frames(conf, model, st_frame, image, is_display_tracking=None, tracker=None):
    """
    Display the detected objects on a video frame using the YOLOv8 model.

    Args:
    - conf (float): Confidence threshold for object detection.
    - model (YoloV8): A YOLOv8 object detection model.
    - st_frame (Streamlit object): A Streamlit object to display the detected video.
    - image (numpy array): A numpy array representing the video frame.
    - is_display_tracking (bool): A flag indicating whether to display object tracking (default=None).

    Returns:
    None
    """

    # Resize the image to a standard size
    image = cv2.resize(image, (720, int(720*(9/16))))

    # Display object tracking, if specified
    if is_display_tracking:
        res = model.track(image, conf=conf, persist=True, tracker=tracker)
    else:
        # Predict the objects in the image using the YOLOv8 model
        res = model.predict(image, conf=conf)

    # # Plot the detected objects on the video frame
    res_plotted = res[0].plot()
    st_frame.image(res_plotted,
                   caption='Detected Video',
                   channels="BGR",
                   use_column_width=True
                   )
'''
st.code(code_video_detection, language='python')