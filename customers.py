import csv

def get_page(url):
    return requests.get(url, auth=('user','pass')).json()

#API endpoint is paginated, but don't know in advance how many pages there are
#use pull_again to determine if there's another page to pull
pull_again = True
page = 1

customers = {}

while pull_again == True:
    url = 'xxxx.xxxxxx.com/api/customer?page={}&per_page=25'.format(page)
    r = get_page(url)
    
    #some guests don't have a restaurant field - use dict.get
    for guest in r['results']:
        customers[guest['email']] = guest['history'][0]['data'].get('restaurants',"")       
        
    if r['next'] == None:
        pull_again = False
    
    page += 1


with open('customers.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in customers.items():
       writer.writerow([key, value])
