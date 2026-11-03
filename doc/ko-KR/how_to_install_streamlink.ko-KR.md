# Windows 버전 Streamlink 설치하기

Streamlink는 전역에서 사용할 수 있는 Python 환경의 설치 여부에 따라 두 가지 방법으로 설치할 수 있습니다.

## 1. pip를 사용한 설치 (Python 환경이 있는 경우)

**최소 지원 버전: 8.6.1**

전역에서 사용할 수 있는 Python 환경이 설치되어 있다면 `pip`를 사용해 Streamlink를 설치하거나 업데이트할 수 있습니다.

```powershell
python -m pip install --upgrade streamlink
```

Python 개발자, 이른바 파이써니스타(Pythonista)라면 평소 사용하는 Python 환경을 이용해도 됩니다.

## 2. Python 없이 설치하기

**최소 지원 버전: 8.3.0**

Python이 설치되어 있지 않다면 Python 런타임이 포함된 Windows용 설치 파일을 사용할 수 있습니다.

1. [streamlink-8.6.3-1-py315-x86_64.exe](https://github.com/streamlink/windows-builds/releases/download/8.6.3-1/streamlink-8.6.3-1-py315-x86_64.exe)를 다운로드합니다.
2. 다운로드한 설치 파일을 실행합니다.
3. 설치 대상을 선택하는 화면에서 **Install for anyone using this computer**를 선택합니다.
4. 설치가 완료되면 시스템 환경 설정 변경 사항을 확실히 적용하기 위해 컴퓨터를 다시 시작합니다.

## 보안 관련 권장 사항

**설치 방법과 관계없이 잠재적인 보안 위험을 최소화하고 호환성과 안정성을 확보하기 위해 Streamlink를 항상 사용 가능한 최신 버전으로 업데이트할 것을 강력히 권장합니다.**
