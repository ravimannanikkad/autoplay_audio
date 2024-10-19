import vlc
import time
import schedule
import argparse
from datetime import datetime

# Function to play the audio for a specified duration
def play_audio(duration):
    print(f"Playing audio at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} for {duration} seconds.")
    player = vlc.MediaPlayer(audio_file)
    player.play()

    # Wait for the specified duration or until the audio finishes playing
    time.sleep(duration)
    player.stop()
    print(f"Stopped playing audio at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Set up argument parsing
parser = argparse.ArgumentParser(description="Play an audio file at a specific time for a set duration.")
parser.add_argument('play_time', type=str, help='The time to play the audio (HH:MM format)')
parser.add_argument('duration', type=int, help='The duration in seconds to play the audio')

args = parser.parse_args()
play_time = args.play_time
duration = args.duration

# Path to the audio file you want to play
audio_file = "./devi.mp3"  # Replace with the path to your audio file

# Schedule the job with the provided duration
schedule.every().day.at(play_time).do(play_audio, duration)

print(f"Scheduled to play audio every day at {play_time} for {duration} seconds.")

# Run the scheduler
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped.")
