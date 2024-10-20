import requests
from bs4 import BeautifulSoup

def fill_fbar_form(data):
    """
    Automate the completion of the FBAR form with the provided data.
    
    Args:
    data (dict): A dictionary containing the necessary information to fill out the FBAR form.
    """
    # URL for the FBAR form submission page
    url = "https://bsaefiling.fincen.gov/lc/content/xfaforms/profiles/htmldefault.html"
    
    # Start a session
    session = requests.Session()
    
    # Get the form page
    response = session.get(url)
    response.raise_for_status()  # Check for HTTP issues
    
    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the form
    form = soup.find('form')
    if not form:
        raise Exception("Could not find the form on the page.")
    
    # Prepare the form data
    form_data = {}
    for input_tag in form.find_all('input'):
        input_name = input_tag.get('name')
        if input_name:
            form_data[input_name] = data.get(input_name, '')
    
    # Submit the form
    response = session.post(url, data=form_data)
    response.raise_for_status()  # Check for HTTP issues
    
    if "Thank you for filing" in response.text:
        print("FBAR form submitted successfully.")
    else:
        print("Failed to submit FBAR form.")

# Example data to fill the FBAR form
data = {
    'name': 'John Doe',
    'address': '123 Elm Street',
    'account_number': '987654321',
    'country': 'USA',
    'max_value': '15000'
}

fill_fbar_form(data)
