import click
import requests
from pprint import pprint  # pretty print
from bs4 import BeautifulSoup
import validators
from tqdm import tqdm

from messages.Messages import Messages

messagesFactory = Messages()


@click.command()
@click.option('--url', default="", help='URL target')
@click.option('--elements', default="all", help='Indicate elements HTML you need')
def pull(url, elements):
    if not url:
        click.echo(
            messagesFactory.makeErrorMessage("no URL given. Provide correct URL such as, --url=https://your_url.com"))
        return

    if not validators.url(url):
        click.echo(messagesFactory.makeErrorMessage("Wrong URL format given"))
        return

    if validators.url(url):
        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.content, 'html.parser')
            all_elements = soup.find_all()

            click.echo(messagesFactory.makeInfoMessage("Target URL => {}".format(url)))
            # Progress bar display CLI
            for i in tqdm(range(len(all_elements)), 'Page analysis'):
                pass

            click.echo(messagesFactory.makeSuccessMessage("{} elements found".format(len(all_elements))))

        except requests.exceptions.RequestException as e:
            click.echo(messagesFactory.makeErrorMessage(e))

        #
        # soup = BeautifulSoup(res.content, 'html.parser')
        # click.echo(pprint(soup))
