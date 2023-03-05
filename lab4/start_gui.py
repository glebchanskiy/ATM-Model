from lab4.core.controller import Controller

from lab4.gui.application_gui import ApplicationGUI


def gui():
    app = ApplicationGUI(Controller())
    app.run()
