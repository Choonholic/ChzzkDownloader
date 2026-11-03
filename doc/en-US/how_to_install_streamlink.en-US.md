# How to Install Streamlink on Windows

There are two ways to install Streamlink, depending on whether you have a globally accessible Python environment.

## 1. Installing Streamlink with pip (Python environment available)

**Minimum supported version: 8.6.1**

If you have a globally accessible Python environment, you can install or upgrade Streamlink using `pip`.

```powershell
python -m pip install --upgrade streamlink
```

If you are a Python developer (a.k.a. Pythonista), you can use your preferred Python environment.

## 2. Installing Streamlink without Python

**Minimum supported version: 8.3.0**

If you do not have Python installed, you can use the standalone Windows installer, which includes its own Python runtime.

1. Download [streamlink-8.6.3-1-py315-x86_64.exe](https://github.com/streamlink/windows-builds/releases/download/8.6.3-1/streamlink-8.6.3-1-py315-x86_64.exe).
2. Run the downloaded installer.
3. When prompted to select which users to install for, choose **Install for anyone using this computer**.
4. After installation is complete, restart your computer to ensure that the updated system environment settings take effect.

## Security Recommendation

**Regardless of the installation method, we strongly recommend keeping Streamlink updated to the latest available version to minimize potential security risks and ensure compatibility and stability.**
