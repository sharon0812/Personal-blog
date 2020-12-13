import requests

# from .models import Quote
base_url = None



def configure_requests(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

    # return requests.get(url).json()
    
def get_quotes():
    '''
    Function that gets the json response to our url request
    '''
    get_quote_response = requests.get('http://quotes.stormconsultancy.co.uk/quotes/42').json()
    print(get_quote_response)
    return get_quote_response