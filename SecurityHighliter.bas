Attribute VB_Name = "NewMacros"
Sub SecurityHighliter()
Attribute SecurityHighliter.VB_Description = "Searches AIC Reports and Highlights Specific strings that require additional attention.  "
Attribute SecurityHighliter.VB_ProcData.VB_Invoke_Func = "Normal.NewMacros.SecurityHighliter"

Dim range As range
Dim i As Long
Dim TargetList

TargetList = Array("VULNERABLE", "writable", "open", "CVE-", "administrator", "admin", "vulnerable", "anonymous", "OSVDB-", "Interesting", "found") ' put list of terms to find here
IPList = Array("192.168.0.117")

For i = 0 To UBound(TargetList)

Set range = ActiveDocument.range

With range.Find
.Text = TargetList(i)
.Format = True
.MatchCase = True
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False

Do While .Execute(Forward:=True) = True
'range.HighlightColorIndex = wdRed
range.Font.ColorIndex = wdRed

Loop

End With
Next

For i = 0 To UBound(IPList)

With range.Find
.Text = IPList(i)
.Format = True
.MatchCase = True
.Replacement.Font.Bold = True
.MatchWholeWord = False
.MatchWildcards = False
.MatchSoundsLike = False
.MatchAllWordForms = False

End With
range.Find.Execute Replace:=wdReplaceAll
Next

End Sub
