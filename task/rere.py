import json
#
#
def open_json():
    return [json.loads(line) for line in open('task/world_bank.json', 'r')]
#
#
def get_list_of_countries():
    data_list = []
    for data in open_json():
        data_list.append(data['project_name'])
    return set(data_list)

print(get_list_of_countries())
print(len(get_list_of_countries()))
# # x = "People's Republic of China"
# #
# #
# def get_money(country):
#     total_money_for_country = 0
#     for data in open_json():
#         if country in data['countryname']:
#             total_money_for_country += data['totalamt']
#     return total_money_for_country
# # def get_money(country):
# #     total_money_for_country = 0
# #     for data in open_json():
# #         if country in data['countryname']:
# #             total_money_for_country += 1
# #     return total_money_for_country
# #
# #
# # get_money(x)
#
# def caa(list_of_countries):
#     countries_and_projects_amount = {}
#     list_of_countries = set(list_of_countries)
#     for country in list_of_countries:
#         countries_and_projects_amount[country] = get_money(country)
#     return countries_and_projects_amount
#
# def get_regions_with_top_project_amount(regions, amount=10):
#     print("Regions with highest project amount...")
#     for region_name, number_of_projects in sorted(regions.items(), key=lambda x: x[1],
#                                                   reverse=True)[:amount]:
#         print(f"Region name: {region_name}, number of projects: {number_of_projects}")
#
# get_regions_with_top_project_amount(caa(get_list_of_countries()))