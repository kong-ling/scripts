from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()

poem=[
    '锄禾日当午，',
    '汗滴禾下土。',
    '谁知盘中餐，',
    '粒粒皆辛苦。',
    '\n',
    '千山鸟飞绝，',
    '万径人踪灭。',
    '孤舟蓑笠翁，',
    '独钓寒江雪。',
]


for sentence in poem:
    app.UntitledNotepad.Edit.type_keys("%s" % sentence, with_spaces = True)
    app.UntitledNotepad.Edit.type_keys("{ENTER}", with_spaces = True)

app.UntitledNotepad.menu_select("File->Save")
app['Save As'].Edit.type_keys('test.txt')
app['Save As']['Save'].click()
app['Confirm Save As']['Yes'].click()

save_dlg=app.window(title_re='Notepad')
save_dlg.child_window(title_re='OK').click()
