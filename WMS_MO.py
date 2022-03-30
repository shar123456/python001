import webbrowser
SetBrowserPath=r"C:\Users\zhangxq\AppData\Local\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(SetBrowserPath))  
webbrowser.get('chrome').open("http://172.16.100.200//Account//Login",new=2,autoraise=True)