import json


def open_json():
    return [json.loads(line) for line in open('world_bank.json', 'r')]


def get_list_of_countries():
    data_list = []
    for data in open_json():
        data_list.append(data['countryname'])
    return data_list


def count_projects_per_country_amount(countries):
    countries_and_projects_amount = {}
    for country in countries:
        if country in countries_and_projects_amount:
            countries_and_projects_amount[country] = countries_and_projects_amount[country] + 1
        else:
            countries_and_projects_amount[country] = 1
    return countries_and_projects_amount


def get_money(country):
    total_money_for_country = 0
    for data in open_json():
        if country in data['countryname']:
            total_money_for_country += data['totalamt']
    return total_money_for_country


def money_invested_per_country(list_of_countries):
    countries_and_projects_amount = {}
    for country in set(list_of_countries):
        countries_and_projects_amount[country] = get_money(country)
    return countries_and_projects_amount


def get_regions_with_top_project_amount(regions, amount=10):
    print("Regions with highest project amount...")
    for region_name, number_of_projects in sorted(regions.items(), key=lambda x: x[1],
                                                  reverse=True)[:amount]:
        print(f"Region name: {region_name}, number of projects: {number_of_projects}")


def get_regions_with_top_money_invested_amount(regions, amount=10):
    print("Regions with highest money invested amount...")
    for region_name, money_invested in sorted(regions.items(), key=lambda x: x[1],
                                                  reverse=True)[:amount]:
        print(f"Region name: {region_name}, money invested: {money_invested}")


def main():
    get_regions_with_top_project_amount(regions=count_projects_per_country_amount(get_list_of_countries()))
    print("")
    get_regions_with_top_money_invested_amount(regions=money_invested_per_country(get_list_of_countries()))


main()
