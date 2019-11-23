' Not print in console 
' The result will store in C:\Windows\Temp\Result.txt
' Change the scanning range by strSubNet
strSubNet = "172.20.10."
Set objFSO= CreateObject("Scripting.FileSystemObject")
Set objTS = objfso.CreateTextFile("C:\Windows\Temp\Result.txt")
For i = 1 To 254
strComputer = strSubNet & i
blnResult = Ping(strComputer)
If blnResult = True Then
objTS.WriteLine strComputer & " is alived ! :) "
End If
    Next

objTS.Close
WScript.Echo "All Ping Scan , All Done ! :) "
Function Ping(strComputer)
Set objWMIService = GetObject("winmgmts:\\.\root\cimv2")
Set colItems = objWMIService.ExecQuery("Select * From Win32_PingStatus Where Address='" & strComputer & "'")
For Each objItem In colItems
Select case objItem.StatusCode
Case 0
Ping = True
Case Else
Ping = False
End select
Exit For
Next
End Function

