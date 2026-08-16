# How to install FFmpeg on Windows

## Notices

- Chzzk Downloader Suite only supports the official major versions of FFmpeg and does not support test builds or any other unofficial releases.
- The minimum supported version of FFmpeg is 7.0.
- If FFmpeg is already installed, you can skip the following steps and simply add the directory containing `ffmpeg.exe` to the `PATH` system environment variable.

## Installing Using the Installer

- Note: The binary installed using this method may not immediately reflect the latest version.

1. Open [https://getffmpeg.org/](https://getffmpeg.org/).
2. Click **Download ffmpeg-setup.exe Installer** button to download `ffmpeg-setup.exe` file.
3. Run `ffmpeg-setup.exe` file and follow the instructions to complete the installation.

## Installing the Latest Version Using Winget

1. Open `PowerShell`.
2. Run the following command.

   ```powershell
   winget install --id Gyan.FFmpeg --source winget
   ```

3. After installation has finished, restart your computer to apply configurations and system environments.

## Installing an Official Build Manually

1. Open [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/).
2. Under **release builds**, download one of the following files from the **latest release** section.

   * `ffmpeg-release-essentials.7z`
   * `ffmpeg-release-essentials.zip`
   * `ffmpeg-release-full.7z`
   * `ffmpeg-release-full-shared.7z`

3. Extract the downloaded archive to a directory of your choice.
4. Add the `bin` directory inside the extracted FFmpeg directory to the `PATH` system environment variable.

   For instructions on adding a directory to the `PATH` environment variable, see `how_to_add_path_environment.en-US.pdf`.
