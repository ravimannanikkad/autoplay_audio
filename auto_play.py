import vlc
import time
import schedule
import argparse
from datetime import datetime, timedelta

# Function to play the audio

def play_audio(duration_minutes):
    try:
        print(f"Playing audio at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        player = vlc.MediaPlayer(audio_file)

        #player = vlc.MediaPlayer(audio_file)
        #player.set_mrl(audio_file)
        player.get_media().add_option('verbose=2')
        player.play()

        # Calculate the end time based on the specified duration
        end_time = datetime.now() + timedelta(minutes=duration_minutes)

        # Wait until the duration is over or until the audio finishes
        while datetime.now() < end_time and player.is_playing():
            time.sleep(1)

        print("Playback stopped.")
        player.stop()
    except Exception as e:
        print(f"An error occurred during playback: {e}")



# Set up argument parsing
parser = argparse.ArgumentParser(description="Play an audio file at a specific time for a given duration.")
parser.add_argument('play_time', type=str, help='The time to play the audio (HH:MM format)')
parser.add_argument('duration', type=int, help='The duration to play the audio (in minutes)')

args = parser.parse_args()
play_time = args.play_time
duration = args.duration

# Path to the audio file you want to play
audio_file = "/home/ravi/playlist/devi.mp3"  # Replace with the path to your audio file

# Schedule the job
schedule.every().day.at(play_time).do(play_audio, duration)

print(f"Scheduled to play audio every day at {play_time} for {duration} minutes.")

# Run the scheduler
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped.")
