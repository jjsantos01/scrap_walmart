# Scrap Walmart

This script retrieve the information about the departments, categories and subcategories from the grocery store [Walmart Mexico](https://super.walmart.com.mx/). The output is a json file which contains the name and URL to access to all the departments, categories and subcategories.

To run this script, clone this repo in your computer:
```bash
git clone git@github.com:jjsantos01/scrap_walmart.git
cd scrap_walmart
```

You need to have installed and running Docker in your system. Then, run in the terminal the next command to build the image:
```bash
docker build -t walmart-scraper .
```
And then you run the command to execute the script:
```bash
docker run -v $(pwd)/data:/app/data walmart-scraper
```
A new file `data/menu_despensa.json` will be created with the information. The file looks like this:

```json
[
    {
        "department": "Temporadas",
        "url": "https://super.walmart.com.mx/content/temporadas/dia-de-las-madres/1940018_2500034",
        "categories": [
            []
        ]
    },
    {
        "department": "Lo m\u00e1s nuevo",
        "url": "https://super.walmart.com.mx/content/lo-mas-nuevo/3710103",
        "categories": [
            [
                {
                    "name": "Todo para tu despensa",
                    "url": "https://super.walmart.com.mx/content/lo-mas-nuevo/todo-para-tu-despensa/3710103_3880040",
                    "subcategories": [
                        {
                            "name": "Alimentos y bebidas",
                            "url": "https://super.walmart.com.mx/browse/lo-mas-nuevo/todo-para-tu-despensa/alimentos-y-bebidas/3710103_3880040_3880041"
                        },
                        {
                            "name": "Cuidado del hogar y de la ropa",
                            "url": "https://super.walmart.com.mx/browse/lo-mas-nuevo/todo-para-tu-despensa/cuidado-del-hogar-y-de-la-ropa/3710103_3880040_3880043"
                        }
                    ]
                },
                {
                    "name": "Lacteos, congelados, botanas y m\u00e1s",
                    "url": "https://super.walmart.com.mx/content/lo-mas-nuevo/lacteos-congelados-botanas-y-mas/3710103_3880032",
                    "subcategories": [
                        {
                            "name": "Bebidas y botanas",
                            "url": "https://super.walmart.com.mx/browse/lo-mas-nuevo/lacteos-congelados-botanas-y-mas/bebidas-y-botanas/3710103_3880032_3880033"
                        },
                        {
                            "name": "Congelados, l\u00e1cteos y Salchichoner\u00eda",
                            "url": "https://super.walmart.com.mx/browse/lo-mas-nuevo/lacteos-congelados-botanas-y-mas/congelados-lacteos-y-salchichoneria/3710103_3880032_3880034"
                        },
                        {
                            "name": "Vinos y licores",
                            "url": "https://super.walmart.com.mx/browse/lo-mas-nuevo/lacteos-congelados-botanas-y-mas/vinos-y-licores/3710103_3880032_3880035"
                        }
                    ]
                },

      ...
]
```
