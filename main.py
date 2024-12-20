from scraper import Scraper

class Main(Scraper):
    def __init__(self):
        super().__init__()

    def run(self):
        print(self.scrape('https://finance.yahoo.com/'))

if __name__ == '__main__':
    main = Main()
    main.run()

