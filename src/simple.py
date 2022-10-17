"""Web Scrappper with Simple Approach"""


from utils import  get_response, parse_countries_urls, get_country_detail


def simple_countries_detail(start_url):
    """This method is used to get information of all countries"""

    response = get_response(start_url)
    if response:
        country_url = parse_countries_urls(response.content)
    for url in country_url:
        get_country_detail(url)
