travel_log = {
    "France": ["Paris", "Lille","Dijon"],
    "Germany": ["Berlin", "Stuttgart"]
}
print(travel_log["France"][1])




nested_list = ["A", "B", ["C", "D"]]
print(f"Printing C: {nested_list[2][0]}")

travel_log_2 = {
    "France": { 
        "num_times_visited": 8,
        "cities_visited": ["Paris", "Lille","Dijon"]
    },
    "Germany": { 
        "num_times_visited": 3,
        "cities_visited": ["Berlin", "Stuttgart"]     
    }
}

print(f"City: {travel_log_2['Germany']['cities_visited'][1]}, number of times visited: {travel_log_2['Germany']['num_times_visited']}")
