
restaurant_ids = [1, 2, 3, 4, 5]
restaurant_names = ["Vikings Luxury Buffet", "Antonio's Restaurant", "Mesa Filipino Moderne", "Manam Comfort Filipino", "Ramen Nagi"]
restaurant_locations = ["Pasay City", "Tagaytay", "Makati City", "Quezon City", "Various Locations"]
restaurant_cuisine_types = ["Buffet", "Fine Dining", "Filipino", "Filipino", "Japanese"]
restaurant_established_years = [2011, 2002, 2009, 2013, 2013]
restaurant_websites_or_contacts = ["www.vikings.ph", "www.antoniosrestaurant.ph", "www.mesa.ph", "www.manam.ph", "www.ramennagi.com.ph"]


print("Restaurant Data:")
for i in range(len(restaurant_ids)):
    print(f"Restaurant ID: {restaurant_ids[i]}, Name: {restaurant_names[i]}, Location: {restaurant_locations[i]}, Cuisine Type: {restaurant_cuisine_types[i]}, Established Year: {restaurant_established_years[i]}, Website/Contact: {restaurant_websites_or_contacts[i]}")
