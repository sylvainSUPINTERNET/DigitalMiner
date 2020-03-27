# Create generic message for every CLI commands


class Messages:
    def __init__(self):
        self.errorMessageIcon = " ✕ "
        self.successMessageIcon = " ✔ "
        self.infoMessageIcon = " ◌ "

    def makeErrorMessage(self, errMsg="unexpected error is occured, try again"):
        return "{} {}".format(self.errorMessageIcon, errMsg)

    def makeSuccessMessage(self, successMsg="operation executed with success !"):
        return "{} {}".format(self.successMessageIcon, successMsg)

    def makeInfoMessage(self, infoMsg=""):
        return "{} {}".format(self.infoMessageIcon, infoMsg)