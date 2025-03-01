import networkx as nx
import heapq

# Create a graph
kerala_graph = nx.Graph()

# Define places with categories and budgets
places = {
    "Munnar": {"type": "Hill Station", "budget": "Mid"},
    "Wayanad": {"type": "Hill Station", "budget": "Mid"},
    "Thekkady": {"type": "Hill Station", "budget": "Mid"},
    "Vagamon": {"type": "Hill Station", "budget": "Low"},
    "Alappuzha": {"type": "Backwaters", "budget": "High"},
    "Kumarakom": {"type": "Backwaters", "budget": "High"},
    "Ashtamudi Lake": {"type": "Backwaters", "budget": "Mid"},
    "Munroe Island": {"type": "Backwaters", "budget": "Low"},
    "Kuttanad": {"type": "Backwaters", "budget": "Mid"},
    "Kochi": {"type": "City Heritage", "budget": "Mid"},
    "Trivandrum": {"type": "City Heritage", "budget": "Mid"},
    "Athirapally Waterfalls": {"type": "Waterfalls", "budget": "Low"},
    "Varkala": {"type": "Beach", "budget": "Mid"},
    "Kovalam": {"type": "Beach", "budget": "High"},
    "Ponmudi": {"type": "Hill Station", "budget": "Low"},
    "Bekal": {"type": "City Heritage", "budget": "Mid"},
    "Marari Beach": {"type": "Beach", "budget": "Low"},
    "Silent Valley": {"type": "Hill Station", "budget": "Mid"},
    "Nelliampathy": {"type": "Hill Station", "budget": "Mid"},
    "Idukki": {"type": "Hill Station", "budget": "Mid"},
    "Pathiramanal Island": {"type": "Backwaters", "budget": "Low"},
    "Vembanad Lake": {"type": "Backwaters", "budget": "Mid"},
    "Punnamada Lake": {"type": "Backwaters", "budget": "Mid"},
    "Payyambalam Beach": {"type": "Beach", "budget": "Mid"},
    "Bekal Beach": {"type": "Beach", "budget": "Mid"},
    "Cherai Beach": {"type": "Beach", "budget": "Low"},
    "Kappad Beach": {"type": "Beach", "budget": "Mid"},
    "Muzhappilangad Drive-in Beach": {"type": "Beach", "budget": "Mid"},
    "Thrissur": {"type": "City", "budget": "Mid"},
    "Kannur": {"type": "City", "budget": "Mid"},
    "Kozhikode": {"type": "City", "budget": "Mid"},
    "Palakkad": {"type": "City", "budget": "Low"},
    "Malappuram": {"type": "City", "budget": "Low"},
    "Kollam": {"type": "City", "budget": "Mid"},
    "Kottayam": {"type": "City", "budget": "Mid"},
    "Meenmutty Waterfalls": {"type": "Waterfalls", "budget": "Low"},
    "Soochipara Waterfalls": {"type": "Waterfalls", "budget": "Low"},
    "Thusharagiri Waterfalls": {"type": "Waterfalls", "budget": "Low"},
    "Palaruvi Waterfalls": {"type": "Waterfalls", "budget": "Low"},
    "Vazhachal Waterfalls": {"type": "Waterfalls", "budget": "Low"},
    "Periyar Wildlife Sanctuary": {"type": "Wildlife", "budget": "Mid"},
    "Wayanad Wildlife Sanctuary": {"type": "Wildlife", "budget": "Mid"},
    "Parambikulam Tiger Reserve": {"type": "Wildlife", "budget": "High"},
    "Chinnar Wildlife Sanctuary": {"type": "Wildlife", "budget": "Low"},
    "Thattekad Bird Sanctuary": {"type": "Wildlife", "budget": "Low"},
    "Neyyar Wildlife Sanctuary": {"type": "Wildlife", "budget": "Mid"},
    
}

# Add places as nodes
for place, attributes in places.items():
    kerala_graph.add_node(place, **attributes)

# Define connections (edges) with travel times in hours
edges = [
    ("Munnar", "Thekkady", 3.5),
    ("Munnar", "Kochi", 4.0),
    ("Thekkady", "Alappuzha", 4.5),
    ("Alappuzha", "Kumarakom", 1.0),
    ("Kumarakom", "Kochi", 1.5),
    ("Kochi", "Athirapally Waterfalls", 2.0),
    ("Kochi", "Trivandrum", 5.0),
    ("Trivandrum", "Kumarakom", 4.5),
    ("Alappuzha", "Kuttanad", 1.0),
    ("Ashtamudi Lake", "Munroe Island", 0.5),
    ("Kochi", "Varkala", 3.5),
    ("Varkala", "Kovalam", 2.0),
    ("Kovalam", "Trivandrum", 1.5),
    ("Munnar", "Ponmudi", 5.0),
    ("Bekal", "Kochi", 6.0),
    ("Marari Beach", "Alappuzha", 0.5),
    ("Silent Valley", "Wayanad", 3.5),
    ("Munnar", "Idukki", 2.0),
    ("Idukki", "Thekkady", 2.5),
    ("Nelliampathy", "Silent Valley", 3.0),
    ("Kumarakom", "Vembanad Lake", 0.5),
    ("Vembanad Lake", "Punnamada Lake", 1.0),
    ("Punnamada Lake", "Pathiramanal Island", 0.5),
    ("Ashtamudi Lake", "Kollam", 1.0),
    ("Munroe Island", "Ashtamudi Lake", 0.5),
    ("Kochi", "Cherai Beach", 1.0),
    ("Kochi", "Varkala", 3.5),
    ("Varkala", "Kovalam", 2.0),
    ("Kovalam", "Trivandrum", 1.5),
    ("Marari Beach", "Alappuzha", 0.5),
    ("Bekal Beach", "Kannur", 1.5),
    ("Payyambalam Beach", "Kannur", 1.0),
    ("Kozhikode", "Kappad Beach", 0.5),
    ("Kozhikode", "Muzhappilangad Drive-in Beach", 1.5),
    ("Bekal", "Kozhikode", 4.0),
    ("Thrissur", "Kochi", 1.5),
    ("Kannur", "Thrissur", 4.0),
    ("Kozhikode", "Thrissur", 3.0),
    ("Palakkad", "Thrissur", 1.5),
    ("Kottayam", "Kumarakom", 0.5),
    ("Athirapally Waterfalls", "Vazhachal Waterfalls", 0.5),
    ("Meenmutty Waterfalls", "Wayanad", 1.5),
    ("Soochipara Waterfalls", "Wayanad", 2.0),
    ("Thusharagiri Waterfalls", "Wayanad", 2.0),
    ("Palaruvi Waterfalls", "Kollam", 1.5),
    ("Periyar Wildlife Sanctuary", "Thekkady", 1.0),
    ("Wayanad Wildlife Sanctuary", "Wayanad", 1.5),
    ("Parambikulam Tiger Reserve", "Palakkad", 4.0),
    ("Chinnar Wildlife Sanctuary", "Munnar", 2.5),
    ("Thattekad Bird Sanctuary", "Kochi", 1.5),
    ("Neyyar Wildlife Sanctuary", "Trivandrum", 2.0),
]

# Add edges to graph
for src, dest, time in edges:
    kerala_graph.add_edge(src, dest, travel_time=time)

# Dijkstra's algorithm for shortest paths
def shortest_path(graph, start):
    pq = []
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]["travel_time"]
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Travel Plan Generator
def generate_plan(start, place_type, max_travel_hours, budget, num_days, return_to_start=False):
    filtered_places = [
        place for place in kerala_graph.nodes if kerala_graph.nodes[place]["type"] == place_type
    ]

    alternative_budgets = {"Low": ["Mid"], "Mid": ["Low", "High"], "High": ["Mid"]}
    possible_places = [
        place for place in filtered_places
        if kerala_graph.nodes[place]["budget"] == budget or
        kerala_graph.nodes[place]["budget"] in alternative_budgets.get(budget, [])
    ]

    if not possible_places:
        return "No matching destinations found!"

    visited_places = set()
    daily_plan = {}
    current_location = start

    for day in range(1, num_days + 1):
        distances = shortest_path(kerala_graph, current_location)
        sorted_places = sorted(possible_places, key=lambda x: distances.get(x, float('inf')))

        day_plan = []
        total_time_spent = 0

        for place in sorted_places:
            if place in visited_places:
                continue

            if place not in distances or distances[place] == float('inf'):
                continue  # Skip unreachable places

            travel_time = distances[place]

            if total_time_spent + travel_time <= max_travel_hours:
                path = nx.shortest_path(kerala_graph, current_location, place, weight="travel_time")
                day_plan.append({"route": path, "travel_time": travel_time})
                total_time_spent += travel_time
                visited_places.add(place)
                current_location = place

            if total_time_spent >= max_travel_hours:
                break

        if day_plan:
            daily_plan[f"Day {day}"] = day_plan

            # Ensure possible_places is a set before subtracting visited_places
        if not set(possible_places) - visited_places:

            break  # If all places are visited, stop

    # Return to start at the end
    if return_to_start and current_location != start:
        if nx.has_path(kerala_graph, current_location, start):
            return_path = nx.shortest_path(kerala_graph, current_location, start, weight="travel_time")
            return_time = sum(kerala_graph[u][v]['travel_time'] for u, v in zip(return_path[:-1], return_path[1:]))
            daily_plan[f"Return to {start}"] = [{"route": return_path, "travel_time": return_time}]

    return daily_plan

# New user preferences
# New user preferences
user_input = {
    "start": "Alappuzha",
    "place_type": "Hill Station",  # Changed from "type" to "place_type"
    "max_travel_hours": 6,
    "budget": "Low",
    "num_days": 3,
    "return_to_start": True
}

# Update function to use "place_type" instead of "type"
plan = generate_plan(**user_input)
print("Recommended travel plan:", plan)


