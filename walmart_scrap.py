import requests
import json

base_url = "https://super.walmart.com.mx"
url = f"{base_url}/orchestra/graphql/header"
payload = json.dumps({
  "query": "query Header( $globalHeaderTempoParams:JSON $tenant:String! $pageType:String! ){contentLayout( channel:\"WWW\" pageType:$pageType tenant:$tenant version:\"v1\" ){modules(p13n:{}tempo:$globalHeaderTempoParams){name type moduleId matchedTrigger{zone}configs{...on EnricherModuleConfigsV1{zoneV1}...GlobalAlertBar...GlobalHeaderHamburgerNav...GlobalHeaderMenu}}}}fragment GlobalHeaderHamburgerNav on TempoWM_GLASSWWWGlobalHamburgerNavConfigs{subCategory{subLinks{link{linkText title clickThrough{value}uid}icon}}}fragment GlobalHeaderMenu on TempoWM_GLASSWWWGlobalHeaderMenuConfigs{allCategoriesLink{linkText title clickThrough{value}uid}departments{name cta{linkText title clickThrough{value}uid}heading description image{alt assetId assetName clickThrough{value}height src title width size contentType uid}subCategoryGroup{subCategoryHeading subCategoryLinksGroup{subCategoryLink{linkText title clickThrough{value}uid}openInNewTab}}}}fragment GlobalAlertBar on TempoWM_GLASSWWWGlobalAlertBarConfigsV1{athenaEnabled alertBarV1{iconName text link{linkText title clickThrough{value}uid}backgroundColor messageColor showCloseButton}}",
  "variables": {
    "globalHeaderTempoParams": {
      "params": [
        {
          "key": "zone",
          "value": "alertBar"
        },
        {
          "key": "zone",
          "value": "hamburgerNav"
        },
        {
          "key": "zone",
          "value": "departmentsMenu"
        },
        {
          "key": "zone",
          "value": "servicesMenu"
        }
      ]
    },
    "tenant": "MX_GLASS",
    "pageType": "global_header"
  }
})
headers = {
  'accept': 'application/json',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
  'cache-control': 'no-cache',
  'content-length': '1391',
  'content-type': 'application/json',
  'origin': 'https://super.walmart.com.mx',
  'pragma': 'no-cache',
  'referer': 'https://super.walmart.com.mx/',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'wm_consumer.banner': 'GR',
  'wm_mp': 'true',
  'wm_page_url': 'https://super.walmart.com.mx/',
  'x-apollo-operation-name': 'Header',
  'x-enable-server-timing': '1',
  'x-latency-trace': '1',
  'x-o-bu': 'WALMART-MX',
  'x-o-ccm': 'server',
  'x-o-correlation-id': '2jxL2g5T7U3im64hCw2dV-tWO9Rtqupf4JG4',
  'x-o-gql-query': 'query Header',
  'x-o-mart': 'B2C',
  'x-o-platform': 'rweb',
  'x-o-platform-version': 'main-1.62.2-75bf5d-0505T0900',
  'x-o-segment': 'oaoh',
  'x-o-vertical': 'OD',
}

def get_menu_despensa():
    response = requests.post(url, headers=headers, data=payload)
    data = response.json()
    all_departments = data["data"]["contentLayout"]["modules"][0]["configs"]["departments"]
    menu = []

    for department in all_departments:
        categories = department["subCategoryGroup"]
        department_info = {
            "department": department["name"],
            "url": f'{base_url}{categories[0]["subCategoryLinksGroup"][0]["subCategoryLink"]["clickThrough"]["value"]}',
            "categories": []
        }
        categories_data = []

        for category in categories[1:]:
            subcategories = category["subCategoryLinksGroup"]
            categorie_info = {
                "name": category["subCategoryHeading"],
                "url": f'{base_url}{subcategories[0]["subCategoryLink"]["clickThrough"]["value"]}',
                "subcategories": []
            }

            for subcategory in subcategories[1:]:
                subcategory_info = {
                    "name": subcategory["subCategoryLink"]["linkText"],
                    "url": f'{base_url}{subcategory["subCategoryLink"]["clickThrough"]["value"]}'
                }
                categorie_info["subcategories"].append(subcategory_info)

            categories_data.append(categorie_info)

        department_info["categories"].append(categories_data)
        menu.append(department_info)
    return menu

menu_despensa = get_menu_despensa()
with open('data/menu_despensa.json', 'w') as file:
    json.dump(menu_despensa, file, indent=4)
print("Task finished!")
