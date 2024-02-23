from pywinauto.application import Application

app = Application(backend='uia').connect(best_match="Surfshark")
app.Surfshark.print_control_identifiers()

