from django.core.management.base import BaseCommand
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json

from spacexApp.models import futureLaunch

class Command(BaseCommand):
    help = "Collect Data"

    # defin logic of command
    def handle(self, *args, **options):

        # Collect html
        req = Request("https://spaceflightnow.com/launch-schedule/", headers={'User-Agent': 'Mozilla/5.0'})
        html = urlopen(req).read()

        #convert to soup 
        soup = BeautifulSoup(html, 'html.parser')

        # grab all postings
        main_data = soup.find_all("div", class_="mh-content")

        for data in main_data:
            title =       data.find_all('span', class_='mission')
            launch_date = data.find_all('span', class_='launchdate')
            launch_info = data.find_all('div', class_='missiondata')
            description = data.find_all('div', class_='missdescrip')

           # save in db
            for (t, date, info, desc) in zip(title, launch_date, launch_info, description):
                t.find('span', class_='mission')
                date.find('span', class_="launchdate")
                info.find('div', class_="missondata")
                desc.find('div', class_='missdescrip')

                futureLaunch.objects.get_or_create(
                    title=t.text,
                    launch_date=date.text,
                    launch_info=info.text,
                    description=desc.text
                )
                #print(t.text, date.text, info.text, desc.text)
                
        self.stdout.write( 'Job complete')

