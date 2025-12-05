"""
Kivy Music Player Application

A simple music player GUI built with Kivy framework.

Features:
- Play/Pause/Stop controls
- Volume control
- Song selection from directory
- Display current playing song
- Duration tracking
- Playlist support

Requirements:
    pip install kivy playsound

Note: For audio playback, you may need to install additional dependencies
based on your OS. Kivy core provides built-in audio support via kivy.core.audio
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.uix.filechooser import FileChooserListView

import os
import logging
import subprocess

# Suppress Kivy audio errors (WSL has no audio device)
logging.getLogger("kivy.core.audio").setLevel(logging.ERROR)

# Note: Removed ANGLE backend as it's Windows-only
# On Linux, Kivy will use default OpenGL backend
os.environ["KIVY_AUDIO"] = "sdl2"

# Try to import alternative audio players
try:
    import vlc  # noqa: F401

    HAS_VLC = True
except ImportError:
    HAS_VLC = False

try:
    import pygame  # noqa: F401

    HAS_PYGAME = False  # Don't use pygame as it has issues with Kivy
except ImportError:
    HAS_PYGAME = False


class MusicPlayerApp(App):
    """
    A Kivy-based music player application with play, pause, and volume controls.
    """

    def __init__(self, **kwargs):
        """Initialize the music player with default values."""
        super().__init__(**kwargs)
        self.current_song = None
        self.sound = None
        self.is_playing = False
        self.playlist = []
        self.current_index = 0
        self.music_directory = os.path.expanduser("~/Music")
        self.default_audio = os.path.join(os.path.dirname(__file__), "audio.mp3")
        self.vlc_instance = None
        self.vlc_player = None
        self.ffplay_process = None

    def build(self):
        """
        Build the UI layout for the music player.

        Returns:
            BoxLayout: The root widget containing all UI elements
        """
        # Main vertical layout
        self.root = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # ===== Display Section =====
        display_layout = BoxLayout(orientation="vertical", size_hint_y=0.3, spacing=5)

        # Title label
        title_layout = BoxLayout(size_hint_y=0.4)
        self.title_label = Label(
            text="Music Player", font_size="24sp", bold=True, color=(1, 1, 1, 1)
        )
        title_layout.add_widget(self.title_label)
        display_layout.add_widget(title_layout)

        # Current song label
        song_layout = BoxLayout(size_hint_y=0.3)
        self.song_label = Label(
            text="Now Playing: None", font_size="14sp", color=(0.8, 0.8, 0.8, 1)
        )
        song_layout.add_widget(self.song_label)
        display_layout.add_widget(song_layout)

        # Time label
        time_layout = BoxLayout(size_hint_y=0.3)
        self.time_label = Label(
            text="00:00 / 00:00", font_size="12sp", color=(0.6, 0.6, 0.6, 1)
        )
        time_layout.add_widget(self.time_label)
        display_layout.add_widget(time_layout)

        self.root.add_widget(display_layout)

        # ===== Progress Bar =====
        self.progress_slider = Slider(min=0, max=100, value=0, size_hint_y=0.1)
        self.root.add_widget(self.progress_slider)

        # ===== Control Buttons Section =====
        controls_layout = GridLayout(cols=5, size_hint_y=0.25, spacing=5)

        # Previous button
        prev_button = Button(
            text="⏮ Prev", background_color=(0.2, 0.2, 0.2, 1), font_size="12sp"
        )
        prev_button.bind(on_release=self.previous_song)
        controls_layout.add_widget(prev_button)

        # Play button
        self.play_button = Button(
            text="▶ Play", background_color=(0.2, 0.6, 0.2, 1), font_size="12sp"
        )
        self.play_button.bind(on_release=self.play_music)
        controls_layout.add_widget(self.play_button)

        # Pause button
        self.pause_button = Button(
            text="⏸ Pause", background_color=(0.6, 0.6, 0.2, 1), font_size="12sp"
        )
        self.pause_button.bind(on_release=self.pause_music)
        controls_layout.add_widget(self.pause_button)

        # Stop button
        self.stop_button = Button(
            text="⏹ Stop", background_color=(0.6, 0.2, 0.2, 1), font_size="12sp"
        )
        self.stop_button.bind(on_release=self.stop_music)
        controls_layout.add_widget(self.stop_button)

        # Next button
        next_button = Button(
            text="Next ⏭", background_color=(0.2, 0.2, 0.2, 1), font_size="12sp"
        )
        next_button.bind(on_release=self.next_song)
        controls_layout.add_widget(next_button)

        self.root.add_widget(controls_layout)

        # ===== Volume Control Section =====
        volume_layout = BoxLayout(size_hint_y=0.15, spacing=10)

        volume_label = Label(text="Volume:", size_hint_x=0.2, font_size="12sp")
        volume_layout.add_widget(volume_label)

        self.volume_slider = Slider(min=0, max=1, value=0.5, size_hint_x=0.8)
        self.volume_slider.bind(value=self.set_volume)
        volume_layout.add_widget(self.volume_slider)

        self.root.add_widget(volume_layout)

        # ===== Playlist Section =====
        playlist_button = Button(
            text="📁 Load Playlist",
            size_hint_y=0.1,
            background_color=(0.3, 0.3, 0.5, 1),
            font_size="12sp",
        )
        playlist_button.bind(on_release=self.load_playlist)
        self.root.add_widget(playlist_button)

        # Status label
        self.status_label = Label(
            text="Status: Ready",
            size_hint_y=0.1,
            font_size="11sp",
            color=(0.5, 1, 0.5, 1),
        )
        self.root.add_widget(self.status_label)

        # Schedule updates
        Clock.schedule_interval(self.update_progress, 0.1)

        # Load default audio file if it exists
        if os.path.exists(self.default_audio):
            self.current_song = self.default_audio
            self.song_label.text = f"Selected: {os.path.basename(self.current_song)}"
            self.status_label.text = "Status: Ready to play"

        return self.root

    def play_music(self, instance):
        """
        Play the current song using ffplay (best WSL compatibility).

        Args:
            instance: Button instance that triggered the event
        """
        if self.current_song is None:
            self.status_label.text = "Status: No song selected"
            return

        if self.is_playing:
            return

        try:
            # Stop any existing playback
            if self.ffplay_process:
                self.ffplay_process.terminate()

            # Start ffplay in background
            self.ffplay_process = subprocess.Popen(
                ["ffplay", "-nodisp", "-autoexit", "-v", "error", self.current_song],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            self.is_playing = True
            self.play_button.text = "▶ Playing"
            self.play_button.background_color = (0.2, 0.8, 0.2, 1)
            self.status_label.text = (
                f"Status: Playing {os.path.basename(self.current_song)}"
            )
        except FileNotFoundError:
            self.status_label.text = "Status: ffplay not installed (install ffmpeg)"
        except Exception as e:
            self.status_label.text = f"Status: Error - {str(e)}"

    def pause_music(self, instance):
        """
        Pause the current song.

        Args:
            instance: Button instance that triggered the event
        """
        if self.is_playing:
            if self.vlc_player:
                self.vlc_player.pause()
            elif self.ffplay_process:
                self.ffplay_process.terminate()
                self.ffplay_process = None
            elif self.sound:
                self.sound.stop()

            self.is_playing = False
            self.play_button.text = "▶ Play"
            self.play_button.background_color = (0.2, 0.6, 0.2, 1)
            self.status_label.text = "Status: Paused"

    def stop_music(self, instance):
        """
        Stop the current song and reset playback.

        Args:
            instance: Button instance that triggered the event
        """
        if self.is_playing:
            if self.vlc_player:
                self.vlc_player.stop()
            elif self.ffplay_process:
                self.ffplay_process.terminate()
                self.ffplay_process = None
            elif self.sound:
                self.sound.stop()

        self.sound = None
        self.is_playing = False
        self.play_button.text = "▶ Play"
        self.play_button.background_color = (0.2, 0.6, 0.2, 1)
        self.progress_slider.value = 0
        self.time_label.text = "00:00 / 00:00"
        self.status_label.text = "Status: Stopped"

    def set_volume(self, instance, value):
        """
        Set the volume level for playback.

        Args:
            instance: Slider instance
            value: Volume level (0.0 to 1.0)
        """
        if self.sound:
            self.sound.volume = value

    def update_progress(self, dt):
        """
        Update the progress bar and time display.

        Args:
            dt: Delta time since last call (used by Clock scheduler)
        """
        if self.sound and self.is_playing:
            try:
                # Update progress slider
                if self.sound.length > 0:
                    progress = (self.sound.get_pos() / self.sound.length) * 100
                    self.progress_slider.value = progress

                    # Update time label
                    current_time = self.sound.get_pos()
                    total_time = self.sound.length
                    self.time_label.text = (
                        self.format_time(current_time)
                        + " / "
                        + self.format_time(total_time)
                    )

                # Check if song finished
                if self.sound.get_pos() >= self.sound.length:
                    self.next_song(None)
            except Exception:
                pass  # Silently handle audio property errors

    def format_time(self, seconds):
        """
        Format seconds into MM:SS format.

        Args:
            seconds: Time in seconds

        Returns:
            str: Formatted time string (MM:SS)
        """
        mins = int(seconds) // 60
        secs = int(seconds) % 60
        return f"{mins:02d}:{secs:02d}"

    def load_playlist(self, instance):
        """
        Open a file browser to load music files.

        Args:
            instance: Button instance that triggered the event
        """
        content = BoxLayout(orientation="vertical")

        # File chooser with filters
        filechooser = FileChooserListView(filters=["*.mp3", "*.wav", "*.ogg", "*.flac"])
        content.add_widget(filechooser)

        # Buttons layout
        btn_layout = BoxLayout(size_hint_y=0.1, spacing=5)

        def load_file(instance):
            if filechooser.selection:
                self.current_song = filechooser.selection[0]
                self.song_label.text = (
                    f"Selected: {os.path.basename(self.current_song)}"
                )
                self.status_label.text = "Status: Ready to play"
                popup.dismiss()

        load_btn = Button(text="Load")
        load_btn.bind(on_release=load_file)
        btn_layout.add_widget(load_btn)

        cancel_btn = Button(text="Cancel")
        cancel_btn.bind(on_release=lambda x: popup.dismiss())
        btn_layout.add_widget(cancel_btn)

        content.add_widget(btn_layout)

        popup = Popup(title="Select Music File", content=content, size_hint=(0.9, 0.9))
        popup.open()

    def next_song(self, instance):
        """
        Play the next song in the playlist.

        Args:
            instance: Button instance or None
        """
        if self.playlist and self.current_index < len(self.playlist) - 1:
            self.current_index += 1
            self.current_song = self.playlist[self.current_index]
            self.sound = None
            self.play_music(None)
        else:
            self.status_label.text = "Status: End of playlist"

    def previous_song(self, instance):
        """
        Play the previous song in the playlist.

        Args:
            instance: Button instance
        """
        if self.playlist and self.current_index > 0:
            self.current_index -= 1
            self.current_song = self.playlist[self.current_index]
            self.sound = None
            self.play_music(None)
        else:
            self.status_label.text = "Status: Already at first song"


if __name__ == "__main__":
    MusicPlayerApp().run()
