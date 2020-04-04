import click

from messages.Messages import Messages

messagesFactory = Messages()


class Generator:
    def __init__(self):
        self.allowedFilters = [
            "link",
            "h1",
            "href",

            # to continue . . .
        ]

        self.allowedFileFormat = [
            "excel",
            "csv"
        ]

    '''
    :param allElements: All DOM elements found on URL given
    :param filters: correspond to --element options (DOM elements expected)
    :param formatTarget: correspond to the file generated format wanted (default string empty, that means NO file should be generated by default)
    '''

    def applyFilter(self, allElements, filters, formatTarget=""):
        if formatTarget == "":
            click.echo(messagesFactory.makeInfoMessage("No generation file format specified"))
        else:
            if not self.checkFileFormat(formatTarget):
                click.echo(messagesFactory.makeErrorMessage("Invalid format given : {}, allowed format list : {}".format(formatTarget, self.allowedFileFormat)))
                return
            else:
                click.echo(messagesFactory.makeInfoMessage("Ouput format : {}".format(formatTarget)))

        error_flag = False
        if filters == "all":
            # If not params --elements, default we choose all
            click.echo(messagesFactory.makeInfoMessage("--elements : all (default)"))
            error_flag = True
            return

        # if --elements given, we split the string with white space then we remove duplicate
        DOM_elements_list = list(dict.fromkeys(filters.split("_")))

        for element in DOM_elements_list:
            if not self.checkFilter(element):
                error_flag = True
                click.echo(messagesFactory.makeErrorMessage(
                    "--elements: Not allowed DOM elements given {} ".format(element)))
                return  # end the loop when one element given in option is not valid

        if not error_flag:
            click.echo(messagesFactory.makeInfoMessage(
                "--elements: {} ".format(DOM_elements_list)))

            # TODO: call generate file method
            # check format is given,

    def checkFilter(self, filterGiven):
        if filterGiven in self.allowedFilters:
            return True
        else:
            return False

    # Dans la condition du all il faut faire un generate
    # dans l'autre condition aussi (mais ca va se dupliquer un peu
    def generateFile(self, formatTarget):
        print("go to generate  {} ".format(formatTarget))
        return "ok"

    def checkFileFormat(self, formatName):
         if formatName in self.allowedFileFormat:
             return True
         else:
             return False
