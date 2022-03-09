import urllib.request, talk1.talk1, json, requests

number_facts_url = "http://numbersapi.com/random/math"
cat_facts_url = "https://catfact.ninja/fact"


def facts_about_numbers(order = None):
    result = urllib.request.urlopen(number_facts_url).read()
    print("The facts is: ", result.decode("utf-8"))
    talk1.talk1.talk(result.decode("utf-8"))


def facts_about_cats(afterword = None):
    result = json.load(urllib.request.urlopen(cat_facts_url))['fact']
    print("The facts is: ", result)
    talk1.talk1.talk(result)


plugin_loader = (('numberfacts', facts_about_numbers), ('catfacts', facts_about_cats),
                 ('numberfact', facts_about_numbers), ('catfact', facts_about_cats),)
if __name__ == "__main__":
    # facts_about_numbers("")
    facts_about_cats("")
