import PIL
import streamlit as st
from ultralytics import YOLO
import cv2
import tempfile

def main():
    st.set_page_config(page_title="Project", page_icon="📈")
    model_path = 'models/best-1.pt'

    st.markdown("# Demonstrasi Projek Guardian Eye")

    st.markdown("## 📷 Image Detection")
    st.caption('Pada bagian ini berfungsi untuk demonstrasi mendeteksi objek dari sebuah gambar. Pengguna dapat mengunggah gambar untuk dideteksi apakah terdapat barang yang mengancam.')

    st.markdown("### Upload Image Here")    # Adding header to sidebar
    # Adding file uploader to sidebar for selecting images
    source_img = st.file_uploader(
        "Upload an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))

    # Model Options for Image
    confidence = float(st.slider(key="image_confidence",
        label="Select Model Confidence", min_value=25, max_value=100, value=40)) / 100

    # Creating two columns on the main page
    col1, col2 = st.columns(2)

    # Adding image to the first column if image is uploaded
    with col1:
        if source_img:
            # Opening the uploaded image
            uploaded_image = PIL.Image.open(source_img)
            # Adding the uploaded image to the page with a caption
            st.image(source_img,
                    caption="Uploaded Image",
                    use_column_width=True
                    )

    try:
        model_image = YOLO(model_path)
    except Exception as ex:
        st.error(
            f"Unable to load model for images. Check the specified path: {model_path}")
        st.error(ex)

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

    st.markdown("""---""")

    st.markdown("## 📹 Video Detection")
    st.caption('Pada bagian ini berfungsi untuk demonstrasi mendeteksi objek dari sebuah video. Pengguna dapat mengunggah video untuk dideteksi apakah terdapat barang yang mengancam.')

    st.markdown("### Upload Video Here") 
    # Adding file uploader to sidebar for selecting video
    source_video = st.file_uploader(
        "Upload a video...", type=("mp4", "avi", "mov", "mkv"))

    # Model Options for Video
    confidence_video = float(st.slider(key="video_confidence",
        label="Select Model Confidence", min_value=25, max_value=100, value=40)) / 100

    # Creating two columns on the main page
    col3, col4 = st.columns(2)

    # Adding video to the first column if video is uploaded
    with col3:
        if source_video:
            # Display the uploaded video
            st.video(source_video)

    try:
        model_video = YOLO(model_path)  # Ganti dengan path model yang sesuai
    except Exception as ex:
        st.error(f"Unable to load model for videos. Check the specified path: {model_path}")
        st.error(ex)

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

if __name__ == "__main__":
    main()