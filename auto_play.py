import vlc
import time
import schedule
import argparse
from datetime import datetime

# Function to play the audio playlist for a specified duration
def play_audio_playlist(duration):
    print(f"Playing audio playlist at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} for {duration} seconds.")

    # Create a VLC instance and media list player
    instance = vlc.Instance()
    media_list = instance.media_list_new()
    player = instance.media_list_player_new()

    # Add each audio file to the media list
    for audio_file in playlist_files:
        media = instance.media_new(audio_file)
        media_list.add_media(media)

    # Set the media list to the player and start playback
    player.set_media_list(media_list)
    player.play()

    # Wait for the specified duration before stopping
    time.sleep(duration)
    player.stop()
    print(f"Stopped playing audio at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Set up argument parsing
parser = argparse.ArgumentParser(description="Play a playlist of audio files at a specific time for a set duration.")
parser.add_argument('play_time', type=str, help='The time to play the audio (HH:MM format)')
parser.add_argument('duration', type=int, help='The duration in seconds to play the audio')
parser.add_argument('playlist', nargs='+', help='List of audio file paths for the playlist')

args = parser.parse_args()
play_time = args.play_time
duration = args.duration
playlist_files = args.playlist

# Schedule the job with the provided duration
schedule.every().day.at(play_time).do(play_audio_playlist, duration)

print(f"Scheduled to play audio playlist every day at {play_time} for {duration} seconds.")
print(f"Playlist contains {len(playlist_files)} files.")

# Run the scheduler
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped.")
