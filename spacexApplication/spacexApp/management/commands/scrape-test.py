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
        html = urlopen(req)

        #convert to soup 
        soup = BeautifulSoup(html, 'html.parser')

        # grab all postings
        main_data = soup.find_all("div", class_="mh-content")

        for data in main_data:
            title =       data.find_all('span', class_='mission')
            launch_date = data.find_all('span', class_='launchdate')
            launch_info = data.find_all('div', class_='missiondata')
            description = data.find_all('div', class_='missdescrip')

            for t in title: 
                t.find('span', class_='mission')
                futureLaunch.objects.create(title=t.text)
                
            for launch in launch_date:
                launch.find('span', class_="launchdate")
                futureLaunch.objects.create(launch_date=launch.text)
            
             