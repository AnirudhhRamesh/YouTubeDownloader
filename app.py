import streamlit as st
from youtube_downloader import YoutubeDownloader

def main():
    st.title("YouTube Video Downloader")

    # Input field for YouTube URL
    url = st.text_input("Enter YouTube URL:")

    # Input fields for start and end times
    col1, col2 = st.columns(2)
    with col1:
        start_time = st.text_input("Start time (optional, format: HH:MM:SS)")
    with col2:
        end_time = st.text_input("End time (optional, format: HH:MM:SS)")

    if st.button("Download"):
        if url:
            with st.spinner("Downloading..."):
                yt_downloader = YoutubeDownloader()
                output_file = yt_downloader.download(url, start_time=start_time or None, end_time=end_time or None)
                
                if output_file:
                    st.success("Download completed!")
                    
                    # Provide download link
                    with open(output_file, "rb") as file:
                        st.download_button(
                            label="Download Video",
                            data=file,
                            file_name=output_file,
                            mime="video/mp4"
                        )
                else:
                    st.error("Download failed. Please check the URL and try again.")
        else:
            st.warning("Please enter a YouTube URL.")

if __name__ == "__main__":
    main()
