from covid import Covid
from matplotlib import pyplot as py


covid = Covid()
countries_list = covid.list_countries()
countries = set([key['name'] for key in countries_list])
countries = sorted(countries)

def start():
    print("Want data of specific country (press: 1)")
    print("World data (press: 2)")
    choice = int(input("Enter your choice: "))


def result():
    key = list(report.keys())
    value = list(report.values())

    py.title(f"{country.capitalize()}'s Corona Virus Tracker")
    py.bar(range(len(report)), value, tick_label=key)
    py.show()

    print("Showing report for", country.capitalize(),":",report)


print("Want data of specific country (press: 1)")
print("World data (press: 2)")

check = False
while not check:

    try:

        choice = int(input("Enter your choice: "))

        restart = False
        while not restart:

            if choice == 1:

                check = True
                country = input("Enter your country to check Covid-19 status: ")
                print("Country is", country.capitalize())

                status = covid.get_status_by_country_name(country)
                # total national COVID-19 cases by extracting specifix keys from dictionary using dictionary comprehension + items()
                report = {key: status[key] for key in status.keys() & {'confirmed', 'active', 'deaths', 'recovered'}}
                key = list(report.keys())
                value = list(report.values())
                result()
                break

            elif choice == 2:

                check = True
                country = "worldwide"
                # total Worldwide COVID-19 cases
                report = {
                    "confirmed": covid.get_total_confirmed_cases(),
                    "active": covid.get_total_active_cases(),
                    "deaths": covid.get_total_deaths(),
                    "recovered": covid.get_total_recovered(),
                }
                result()
                break

            else:
                restart = False
                print("Invalid selection! Please try again ...")
                start()
                choice = int(input("Enter your choice: "))


    except (ValueError, TypeError):
        check = False
        print("Invalid input! Please try again ...")
        start()
        choice = int(input("Enter your choice: "))


