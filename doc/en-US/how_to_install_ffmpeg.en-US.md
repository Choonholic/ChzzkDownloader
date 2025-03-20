# How to install ffmpeg on Windows

## Notices

* The minimum supported version of FFmpeg is 7.0.
* If FFmpeg is already installed, you can skip the following steps and simply add the path to the FFmpeg installation directory to the Path system environment variable.

## Installing Using the Installer

* Note: The binary installed using this method may not immediately reflect the latest version.

1. Open [https://getffmpeg.org/](https://getffmpeg.org/).
2. Click **Download ffmpeg-setup.exe Installer** button to download `ffmpeg-setup.exe` file.
3. Run `ffmpeg-setup.exe` file and follow the instructions to complete the installation.

## Installing the Latest Version Using Winget

1. Open `PowerShell`.
2. Run the following command.

```powershell
winget install --id gyan.FFmpeg --source winget
```

3. After installation has finished, Restart your computer to apply configurations and system environments.
