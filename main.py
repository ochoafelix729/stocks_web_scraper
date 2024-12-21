from scraper import Scraper

class Main(Scraper):
    def __init__(self):
        super().__init__()

    def run(self):
        print(self.scrape('https://www.google.com/finance/markets/most-active'))

if __name__ == '__main__':
    main = Main()
    # print(main.create_database())
    # print(main.insert_to_database('https://www.google.com/finance/markets/most-active'))
    # print(main.run())
    print(main.pages_to_scrape('https://www.google.com/finance/markets/most-active'))


