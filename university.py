
university_ids = [1, 2, 3, 4, 5]
university_names = ["University of the Philippines", "Ateneo de Manila University", "De La Salle University", "University of Santo Tomas", "Polytechnic University of the Philippines"]
university_locations = ["Quezon City", "Quezon City", "Manila", "Manila", "Manila"]
university_established_years = [1908, 1859, 1911, 1611, 1904]
university_types = ["Public", "Private", "Private", "Private", "Public"]
university_websites = ["www.up.edu.ph", "www.ateneo.edu", "www.dlsu.edu.ph", "www.ust.edu.ph", "www.pup.edu.ph"]


print("University Data:")
for i in range(len(university_ids)):
    print(f"University ID: {university_ids[i]}, Name: {university_names[i]}, Location: {university_locations[i]}, Established Year: {university_established_years[i]}, Type: {university_types[i]}, Website: {university_websites[i]}")
