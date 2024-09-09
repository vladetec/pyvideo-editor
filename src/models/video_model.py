from moviepy.editor import VideoFileClip
from pathlib import Path

class VideoModel:
    def __init__(self, file_path: Path, start_time: int, end_time: int):
        self.file_path = file_path
        self.start_time = start_time
        self.end_time = end_time

    def edit_video(self) -> Path:
        clip = VideoFileClip(str(self.file_path))
        edited_clip = clip.subclip(self.start_time, self.end_time)
        output_path = self.file_path.parent / f"edited_{self.file_path.name}"
        edited_clip.write_videofile(str(output_path))
        return output_path
