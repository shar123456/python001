import webbrowser
SetBrowserPath=r"C:\Users\king\AppData\Local\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(SetBrowserPath))  
webbrowser.get('chrome').open("http://www.baidu.com",new=2,autoraise=True)