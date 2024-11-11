# 치지직 인증 정보 얻기

1. Microsoft Edge, Google Chrome, Mozilla Firefox와 같은 데스크톱 웹 브라우저에서 [치지직](https://chzzk.naver.com/)에 접속합니다.
2. NAVER 아이디로 로그인합니다.
3. **Ctrl+Shift+I**를 눌러 개발자 도구를 엽니다.
4. **Application** 탭으로 이동합니다.
5. 카테고리에서 **Cookies** 항목 아래의 https://chzzk.naver.com을 선택합니다.
6. **NID_AUT**와 **NID_SES** 값을 복사합니다.
7. 필요할 때 해당 항목에 해당 값을 붙여넣습니다.

<div style='text-align: center'>
<img src='../../img/screenshots/dev_tools.png' />
<p><i>(이 이미지는 최신 정보와 다를 수 있습니다.)</i></p>
</div>

**[알림]**
`NID_SES` 값은 치지직에 로그인할 때마다 변경됩니다. 그러나 `NID_AUT` 값이 유효한 한 `NID_SES` 값을 매번 재설정할 필요는 없습니다.
