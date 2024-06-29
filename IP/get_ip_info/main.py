import requests

def get_ip_info(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    ip = input("Enter IP address: ")
    ip_info = get_ip_info(ip)
    if ip_info['status'] == 'success':
        print("Country:", ip_info["country"])
        print("Country Code:", ip_info['countryCode'])
        print('Region:', ip_info['regionName'])
        print('City:', ip_info['city'])
        print('Postal Code:', ip_info['zip'])
        print('Latitude:', ip_info['lat'])
        print('Longitude:', ip_info['lon'])
        print('Timezone:', ip_info['timezone'])
        print('ISP:', ip_info['isp'])
    else:
        print("ERROR")

if __name__ == "__main__":
    main()
