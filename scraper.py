from recipe_scrapers import scrape_me
import recipe_loader
a = 'Y'
while (a == 'Y'):
    link = str(input("Enter a recipe link please: "))
    scraper = scrape_me(f'{link}')

    title = scraper.title()
    time = scraper.total_time()
    yields = scraper.yields()
    ingredients = scraper.ingredients()
    instructions = scraper.instructions()
    image = scraper.image()
    host = scraper.host()
    links = scraper.links()
    nutrients = scraper.nutrients()

    json_data = {
        'Title': title,
        'Ingredients': ingredients,
        'Quantity': yields,
        'Instructions': instructions,
        'Image Link': image
    }

    recipe_loader.loader(json_data)
    a = str(input("Do you want to add another one? [Y or N]: "))
    if a == 'N':
        print("Thank you for using Luigi's Software...")
        break
