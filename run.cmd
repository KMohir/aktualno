set /a Flag=1
:do
 python Script.py
:while
 if %Flag% NEQ 0 (goto do) else (goto exit)
:next

pause&exit /b

