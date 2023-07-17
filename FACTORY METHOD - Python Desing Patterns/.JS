class WindowsDialog extends Dialog is
    method createButton():Button is
            return new WindowsButton()

class WebDialog extends Dialog is
    method createButton():Button is
        return new HTMLButton()