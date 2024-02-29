import win32com.client

import pythoncom

def protected_view_excel(path,sheets):  #opensheetsofexcelinprotectedview
    pythoncom.CoInitialize()
    xl = win32com.client.Dispatch("Excel.Application")
    xl.Visible = True
    xl.DisplayAlerts = False
    workbook = xl.Workbooks.Open(path)
    active_sheet = workbook.Worksheets(sheets)
    active_sheet.Activate()
    for sheet in workbook.Worksheets:
        if sheet.Name != sheets:
            sheet.Visible = 0
    workbook.Unprotect(Password="password")
    workbook.Protect(Password="password", Structure=True, Windows=True, Readonly=True)
    xl.ActiveWindow.Activate()
    workbook.Close(False)
    xl.Quit()
    pythoncom.CoUninitialize()
