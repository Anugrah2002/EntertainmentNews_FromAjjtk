Current issue:

===1
Traceback (most recent call last):
  File "C:\Users\Abhay\Desktop\seleniumfile.py", line 20, in <module>
    upload_result = youtube.upload('path_to_video', 'title', 'description', ['tag1', 'tag2'])
  File "C:\Users\Abhay\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\selenium_youtube\youtube.py", line 213, in upload
    res = self.__upload(
  File "C:\Users\Abhay\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\kstopit\kstopit.py", line 34, in wrapper
    return __run_with_timeout(
  File "C:\Users\Abhay\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\kstopit\kstopit.py", line 100, in __run_with_timeout
    with timeout_class(timeout, swallow_exc=False):
  File "C:\Users\Abhay\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\stopit\utils.py", line 73, in __enter__
    self.setup_interrupt()
  File "C:\Users\Abhay\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0\LocalCache\local-packages\Python310\site-packages\stopit\signalstop.py", line 33, in setup_interrupt
    signal.signal(signal.SIGALRM, self.handle_timeout)
AttributeError: module 'signal' has no attribute 'SIGALRM'. Did you mean: 'SIGABRT'?

=============================================================
  
   Could not install packages due to an EnvironmentError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/62/d5/5f610ebe421e85889f2e55e33b7f9a6795bd982198517d912eb1c76e1a53/pycparser-2.21-py2.py3-none-any.whl (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f9ddeadd3a0>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
