import click
import requests
from pprint import pprint  # pretty print
from bs4 import BeautifulSoup
import validators
from tqdm import tqdm

from generator.Generator import Generator
from messages.Messages import Messages

messagesFactory = Messages()
generatorService = Generator()


@click.command()
@click.option('--url', default="", help='URL target')
@click.option('--elements', default="all", help='Indicate elements HTML you need such as : link_h1_article_<your_element...>')
@click.option('--format', default="", help='Choose your format (supported : excel)')
def pull(url, elements, format):
    if not url:
        click.echo(
            messagesFactory.makeErrorMessage("no URL given. Provide correct URL such as, --url=https://your_url.com"))
        return

    if not validators.url(url):
        click.echo(messagesFactory.makeErrorMessage("Wrong URL format given"))
        return

    if validators.url(url):
        try:
            # Get HTML content from page
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            all_elements = soup.find_all()

            # Prepare data to retrieve into the file
            print("\n ------------ Parameters ------------")
            generatorService.applyFilter(all_elements, elements, format)
            click.echo(messagesFactory.makeInfoMessage("Target URL => {}".format(url)))
            print(" -----------------------------------")

            print("\n")

            # Progress bar display CLI
            for i in tqdm(range(len(all_elements)), 'Page analysis'):
                pass

            click.echo(messagesFactory.makeSuccessMessage("{} elements found".format(len(all_elements))))

        except requests.exceptions.RequestException as e:
            click.echo(messagesFactory.makeErrorMessage(e))