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

===
