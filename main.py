import argparse
import pandas
import requests
from bs4 import BeautifulSoup
import random


class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    END = "\033[0m"


class art:

    orge = (
        Colors.RED
        + """
    
    ___              _               
   /   \\ ___   _ __ | | __ ___  _ __ 
  / /\\ // _ \\ | '__|| |/ // _ \\| '__|
 / /_//| (_) || |   |   <|  __/| |   
/___,'  \\___/ |_|   |_|\\_\\___||_|  
                                     

    """
        + Colors.END
    )

    train = (
        Colors.GREEN
        + """

   ___                     _                     
  |   \\    ___      _ _   | |__    ___      _ _  
  | |) |  / _ \\    | '_|  | / /   / -_)    | '_| 
  |___/   \\___/   _|_|_   |_\\_\\   \\___|   _|_|_  
_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"|_|\"\"\"\"\"| 
\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-'\"`-0-0-' 

    """
        + Colors.END
    )

    fancy = (
        Colors.PURPLE
        + """
    

╔╦╗┌─┐┬─┐┬┌─┌─┐┬─┐
 ║║│ │├┬┘├┴┐├┤ ├┬┘
═╩╝└─┘┴└─┴ ┴└─┘┴└─

                                    
    """
        + Colors.END
    )

    orge = (
        Colors.RED
        + """
    

                                     

    """
        + Colors.END
    )

    bumpy = (
        Colors.BLUE
        + """
    

 ___                 _                  
(  _`\\              ( )                 
| | ) |   _    _ __ | |/')    __   _ __ 
| | | ) /'_`\\ ( '__)| , <   /'__`\\( '__)
| |_) |( (_) )| |   | |\\`\\ (  ___/| |   
(____/'`\\___/'(_)   (_) (_)`\\____)(_)   
                                        
                                        

                                     

    """
        + Colors.END
    )

    big = (
        Colors.YELLOW
        + """

                                                              
                                                              
    ,---,                             ,-.                     
  .'  .' `\\                       ,--/ /|                     
,---.'     \\    ,---.    __  ,-.,--. :/ |             __  ,-. 
|   |  .`\\  |  '   ,'\\ ,' ,'/ /|:  : ' /            ,' ,'/ /| 
:   : |  '  | /   /   |'  | |' ||  '  /      ,---.  '  | |' | 
|   ' '  ;  :.   ; ,. :|  |   ,''  |  :     /     \\ |  |   ,' 
'   | ;  .  |'   | |: :'  :  /  |  |   \\   /    /  |'  :  /   
|   | :  |  ''   | .; :|  | '   '  : |. \\ .    ' / ||  | '    
'   : | /  ; |   :    |;  : |   |  | ' \\ \'   ;   /|;  : |    
|   | '` ,/   \\   \\  / |  , ;   '  : |--' '   |  / ||  , ;    
;   :  .'      `----'   ---'    ;  |,'    |   :    | ---'     
|   ,.'                         '--'       \\   \\  /           
'---'                                       `----'            
                                                                                                   

    """
        + Colors.END
    )

    help = """
    hi, welcome to dorker. this is a in progress
    dorking tool that uses 12 seach operators to help
    you find what you want. 
    
    some things you should know. 
    
    when a paramater requires a site, enter site.com. do
    not use http(s):// because it defaults to https for security
    
    you cannot save the output to a file currently. 
    
    if your argument has whitespace, encapsulate it with ""
    
    this is my first shot at a osint tool, and its early in devolpment.
    
    most of the help is in the argument description, so look there if confused
    
    to see it just run the script with no arguments
    
    have fun and use nicely!
    
    """


class Dork:
    def __init__(self):

        self.parser = argparse.ArgumentParser(
            description="Python script for Google dorking using a specific website"
        )

        self.parser.add_argument(
            "-s", "--site", help="Specify the site to dork", type=str, required=True
        )

        self.parser.add_argument(
            "-q",
            "--query",
            help="Specify search query encapsulated with double quotes.",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-p",
            "--page",
            help="Specify page number or maximum number of pages to search",
            type=int,
            required=True,
            default=0,
        )

        self.parser.add_argument(
            "-inurl",
            "--inurl",
            help="Specify url to search for in a website",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-intext",
            "--intext",
            help="Search for specified text within the body of a website.",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-related",
            "--related",
            help="Find websites related to the specified website",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-intitle",
            "--intitle",
            help="Search for specified text within title of a website",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-info",
            "--info",
            help="Find information about a website",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-date",
            "--date",
            help="Search for websites published before or after a specific date (YYYY/MM/DD)",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-location",
            "--location",
            help="Search for websites in a specific location or language",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-anchortext",
            "--anchortext",
            help="Search for websites with a specific anchor text",
            type=str,
            required=False,
            default="",
        )

        self.parser.add_argument(
            "-o",
            "--output_file",
            help="Specify the name of a .txt file to save output to",
            type=str,
            required=False,
            default="results",
        )

    def check_convert_date(self):

        args = self.parser.parse_args()

        date = args.date

        date = str(args.date)

        date = date.split("/")

        year = int(date[0])

        if year > 2025 or year < 1900:
            raise ValueError("Year is less than 1900 or greater than 2025")
        month = int(date[1])
        if month > 12 or month < 1:
            raise ValueError("Month is less than 1 or greater than 12")
        day = int(date[2])
        if day > 30 or day < 1:
            raise ValueError("Day is less than 30 or greater than 12")

        timestamp = pandas.Timestamp(
            year=year, month=month, day=day, hour=12, second=30, tz="US/Central"
        )

        date = str(timestamp.to_julian_date())

        print(date)

        return date

    def dork_by_max_page(self):

        args = self.parser.parse_args()

        page_number = args.page

        if page_number < 1:

            raise ValueError("Page number should be greater than 0")

        site = f"site:https://{args.site}"

        inurl = f"inurl:{args.inurl}"

        intitle = f'intitle:"{args.intitle}"'

        intext = f"intext:{args.intext}"

        location = f"loc:{args.location}"

        anchortext = f"anchortext:{args.anchortext}"

        related = f"https://{args.related}"

        query = args.query

        # Build the search query

        operators = site

        if args.location:

            operators += f" {location}"

        if args.intext:

            operators += f" {intext}"

        if args.intitle:

            operators += f" {intitle}"

        if args.inurl:

            operators += f" {inurl}"

        if args.anchortext:

            operators += f" {anchortext}"

        if args.related:

            operators += f" {related}"

        if args.query:

            operators = f"{query} {site}"

        # Get the search results

        result = []

        url = "https://www.google.com/search"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
        }

        for i in range(page_number):

            params = {"q": operators, "start": i * 10}

            response = requests.get(url, params=params, headers=headers)

            soup = BeautifulSoup(response.text, "html.parser")

            links = soup.findAll("div", {"class": "yuRUbf"})

            for j, link in enumerate(links):

                result.append(f"{i*10+j+1}" +" | " +  link.find("a").get("href"))

        return "\n".join(result)


if __name__ == "__main__":

    dork = Dork()

    artlist = [art.big, art.bumpy, art.fancy, art.orge, art.train]

    print(random.choice(artlist))

    print(art.help)

    print(dork.dork_by_max_page())
