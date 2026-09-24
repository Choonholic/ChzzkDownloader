# fMP4 Recover

fMP4 Recover is an experimental recovery tool for downloaded Fragmented MP4 (fMP4) files containing damaged segments.

It analyzes the segments in the file, recovers as much valid media data as possible, and creates a new MP4 file.

## Usage

Run `fMP4Recover.exe` with the file to recover:

```
.\fMP4Recover.exe "video.ts"
```

You can also drag and drop the file onto `fMP4Recover.exe`.

When recovery is complete, a new file with `_fixed` appended to the original filename will be created in the same directory.

For example:

```
video.ts
video_fixed.mp4
```

The original file is not modified.

## Limitations

fMP4 Recover is designed to recover specific types of damaged Fragmented MP4 files. It is not a general-purpose video repair tool and cannot recover every damaged file.

Damaged segments that cannot be recovered may be removed from the resulting file. Therefore, some portions of the video or audio may be missing.

Recovery is only possible when enough valid media data remains in the original file. Keep the original file until you have verified the recovered MP4 file.
