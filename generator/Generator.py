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

    def applyFilter(self, allElements, filters, formatTarget):
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


    def checkFilter(self, filterGiven):
        if filterGiven in self.allowedFilters:
            return True
        else:
            return False

    # dANS la condition du all il faut faire un generate
     # dans l'autre condition aussi (mais ca va se dupliquer un peu
    def generateFile(self, formatTarget):
        print("go to generate  {} ".format(formatTarget))
        return "ok"