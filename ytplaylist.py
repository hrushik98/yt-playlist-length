import streamlit as st
from pytube import Playlist
import math
import streamlit.components.v1 as components
st.title("YouTube Playlist Time Calculator")
st.write(
    "Enter the URL of any YT playlist and find out the time it takes for for you to watch it at 1x, 1.5x and 2x speeds!"
    
    )
st.text("Created by @hrushik98 (github) / @hrush1k (insta) / Phani Hrushik Reddy (LinkedIN)")

st.text("")
url = st.text_input("Enter the URL of the YouTube playlist:")



if st.button("Go"):
    try:

        playlist = Playlist(url)
        playlist_id = playlist.playlist_id
        total_duration = sum(video.length for video in playlist.videos)
        def seconds_to_time(total_duration):
            hours = total_duration// 3600
            minutes = (total_duration % 3600) // 60
            remaining_seconds = total_duration % 60
            hours = round(hours,1)
            minutes = round(minutes,2)
            remaining_seconds = round(remaining_seconds,2)
            return f"{hours} hours, {minutes} minutes, {remaining_seconds} seconds"
        
        
        st.write("Total duration of playlist if played at 1x speed: ")
        st.markdown(f'<span style="background-color: orange; padding: 10px; font-size: 20px; color: white;"> <b><i> {seconds_to_time(total_duration)} </i></b> </span>', unsafe_allow_html=True)
        st.write("Total duration of playlist if played at 1.5x speed: ")
        st.markdown(f'<span style="background-color: teal ; padding: 10px; font-size: 20px; color: white;"> <b><i> {seconds_to_time(total_duration/1.5)} </i></b> </span>', unsafe_allow_html=True)
        st.write("Total duration of playlist if played at 2x speed: ")
        st.markdown(f'<span style="background-color: green; padding: 10px; font-size: 20px; color: white;"> <b><i> {seconds_to_time(total_duration/2)} </i></b> </span>', unsafe_allow_html=True)
        st.text("")
        import streamlit as st

        st.title("YouTube Video Player")

        video_url = f"https://www.youtube.com/embed/videoseries?list={playlist_id}"
        # embed streamlit docs in a streamlit app
        components.iframe(video_url, width=640, height=360)


    except Exception as e:
        st.write("Error: ", e)

