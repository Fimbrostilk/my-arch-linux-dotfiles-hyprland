import subprocess
import time
import json
import sys

GLYPHS = {
    "paused": "",
    "playing": "",
    "stopped": ""
}
DEFAULT_GLYPH = ""  # Glyph when status is unknown or default
TEXT_WHEN_STOPPED = "..."  # Text to display when nothing is playing
SCROLL_TEXT_LENGTH = 50 # Length of the song title part (excludes glyph and space)
REFRESH_INTERVAL = 0.4  # How often the script updates (in seconds)
PLAYERCTL_PATH = "/usr/bin/playerctl" # Path to playerctl, use which playerctl to find yours.

# Function to get player status using playerctl
def get_player_status():
    try:
        result = subprocess.run([PLAYERCTL_PATH, 'status'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        status = result.stdout.decode('utf-8').strip().lower()
        if result.returncode != 0 or not status:
            return "stopped"  # Default to stopped if no status
        return status
    except Exception as e:
        return "stopped"

# Function to get currently playing song using playerctl
def get_current_song():
    try:
        result = subprocess.run([PLAYERCTL_PATH, 'metadata', 'title'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        song_title = result.stdout.decode('utf-8').strip()
        if result.returncode != 0 or not song_title:
            return [TEXT_WHEN_STOPPED, 0]  # Return None if no song is playing or an error occurred
        return [song_title + '      ', 1] if len(song_title) > SCROLL_TEXT_LENGTH else [song_title, 0]
    except Exception as e:
        return None

# Function to generate scrolling text with fixed length
def scroll_text(text, length=SCROLL_TEXT_LENGTH):
    text = text.ljust(length)  # Ensure the text is padded to the desired length
    scrolling_text = text + ' ' + text[:length]  # Add space and repeat start for scrolling effect

    for i in range(len(scrolling_text) - length):
        yield scrolling_text[i:i + length]  # Use a generator to yield scrolling parts

if __name__ == "__main__":
    scroll_generator = None
    salir = 0

    while True:
        output = {}

        try:
            # Get the player status and song title
            status = get_player_status()
            song, scroll = get_current_song()

            # Get the glyph based on player status
            glyph = GLYPHS.get(status, DEFAULT_GLYPH)

            if scroll:
                if song:
                    if len(song) > SCROLL_TEXT_LENGTH:  # Adjusted for fixed glyph space
                        if scroll_generator is None:
                            scroll_generator = scroll_text(song)  # Initialize the generator
                        try:
                            song_text = next(scroll_generator)
                        except StopIteration:
                            scroll_generator = scroll_text(song)
                            song_text = next(scroll_generator)
                    else:
                        song_text = song.ljust(SCROLL_TEXT_LENGTH)  # Ensure the song title is padded
                        scroll_generator = None

                # Combine glyph and song text with a fixed space
                output['text'] = f"{glyph} {song_text}"

            else:
                output['text'] = f"{glyph} {song}"

        except Exception as e:
            output['text'] = f" Error: {str(e)}".ljust(SCROLL_TEXT_LENGTH + 2)  # Show error with stop symbol

        # Print the JSON-like output
        print(json.dumps(output), end='\n')

        time.sleep(REFRESH_INTERVAL)
