import os
import requests
from time import sleep
from bs4 import BeautifulSoup
import json

states = [
    "Abia State",
    "Adamawa State",
    "Akwa Ibom State",
    "Anambra State",
    "Bauchi State",
    "Bayelsa State",
    "Benue State",
    "Borno State",
    "Cross River State",
    "Delta State",
    "Ebonyi State",
    "Edo State",
    "Ekiti State",
    "Enugu State",
    "Gombe State",
    "Imo State",
    "Jigawa State",
    "Kaduna State",
    "Kano State",
    "Katsina State",
    "Kebbi State",
    "Kogi State",
    "Kwara State",
    "Lagos State",
    "Nasarawa State",
    "Niger State",
    "Ogun State",
    "Ondo State",
    "Osun State",
    "Oyo State",
    "Plateau State",
    "Rivers State",
    "Sokoto State",
    "Taraba State",
    "Yobe State",
    "Zamfara State",
    "Federal_Capital_Territory_(Nigeria)",
]

def scrape_wiki():
    for state in states:
        state = state.replace(' ', '_')
        print("state: ",state)
        # the URL of the web page that we want to get transaction data
        api_url = "https://en.wikipedia.org/wiki/"+state
        # HTTP headers used to send a HTTP request
        headers = {
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0'
        }
        # Pauses for 0.5 seconds before sending the next request
        sleep(0.5)
        # send the request to get data in the webpage

        response = requests.get(api_url, headers=headers)
        for row in BeautifulSoup(response.content, 'html.parser').select(('table tbody tr td div div div')):
            images = row.select('a img')
           
            if len(images) and images[0]['alt'].startswith("Seal"):
                # print("image len: ", images[0]['alt'])
                url = "https:" + images[0]['src']
                print(url)
            # get image data and write to disk
                if len(url):
                    img_data = requests.get(url).content
                    dir_path = os.path.dirname(os.path.realpath(__file__))
                    with open(dir_path + "\\data\\" "seal_of_"+ state.lower() + '.png',
                            'wb') as handler:
                        handler.write(img_data)
                        sleep(0.5)
                    print("Downloaded: ", state)
    


if __name__ == "__main__":  # entrance to the main function
    scrape_wiki()
   
