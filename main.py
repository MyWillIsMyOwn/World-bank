import json


def open_json():
    return [json.loads(line) for line in open('world_bank.json', 'r')]


def get_list_of_values(key):
    data_list = []
    for data in open_json():
        data_list.append(data[f'{key}'])
    return data_list


def count_values_appearance(values):
    number_of_values_appearance = {}
    for value in values:
        if value in number_of_values_appearance:
            number_of_values_appearance[value] = number_of_values_appearance[value] + 1
        else:
            number_of_values_appearance[value] = 1
    return number_of_values_appearance


def get_regions_with_top_project_amount(regions, amount=10):
    print("Regions with highest project amount...")
    for region_name, number_of_projects in sorted(regions.items(), key=lambda x: x[1],
                                                  reverse=True)[:amount]:
        print(f"Region name: {region_name}, number of projects: {number_of_projects}")


get_regions_with_top_project_amount(regions=count_values_appearance(get_list_of_values('countryname')))