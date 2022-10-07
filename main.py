import json


def open_json():
    return [json.loads(line) for line in open('world_bank.json', 'r')]


def get_regions_and_project_amount():
    regions = []
    regions_with_amount_of_projects = {}
    for region in open_json():
        regions.append(region['countryname'])

    for region in regions:
        if region in regions_with_amount_of_projects:
            regions_with_amount_of_projects[region] = regions_with_amount_of_projects[region] + 1
        else:
            regions_with_amount_of_projects[region] = 1
    return regions_with_amount_of_projects


def print_regions_with_top_project_amount(regions):
    print("Regions with highest project amount...")
    for region_name, number_of_projects in sorted(regions.items(), key=lambda x: x[1],
                                                  reverse=True)[:10]:
        print(f"Region name: {region_name}, number of projects: {number_of_projects}")


print_regions_with_top_project_amount(get_regions_and_project_amount())
