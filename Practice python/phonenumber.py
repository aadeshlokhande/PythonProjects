# pip install phonenumbers
import phonenumbers
from phonenumbers import geocoder, carrier, timezone
# TECH_IN_SECONDS

phone_number = phonenumbers.parse( "+"+ input("Enter a country code = ") + input("mobile number = "))

# this will print the country name
country = geocoder.description_for_number(phone_number, 'en')
print(f"Country = {country}")

# this will print the service provider
service_pro = carrier.name_for_number(phone_number,'en')
print(f"your first Service Provider = {service_pro}")

# this will print the timezone
time_zone = timezone.time_zones_for_number(phone_number)
print(f"Timezone = {time_zone[0]}")



# Enter a country code = 91  
# mobile number = 70XXXXXX26
# Country = India
# your first Service Provider = Airtel
# Timezone = Asia/Calcutta