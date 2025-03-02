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


def heuristic(node1, node2, graph):
    """Improved heuristic estimating travel time between nodes."""
    if graph.has_edge(node1, node2):
        return graph[node1][node2]['travel_time']
    return 10  # Default heuristic for distant nodes


def a_star_search(graph, start, goal):
    """A* algorithm to find the shortest path based on travel time."""
    pq = []
    heapq.heappush(pq, (0, start))  # (cost, node)
    came_from = {start: None}
    g_score = {node: float('inf') for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph.nodes}
    f_score[start] = heuristic(start, goal, graph)

    while pq:
        _, current = heapq.heappop(pq)
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]  # Return reversed path

        for neighbor in graph.neighbors(current):
            weight = graph[current][neighbor]['travel_time']
            tentative_g_score = g_score[current] + weight

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal, graph)
                heapq.heappush(pq, (f_score[neighbor], neighbor))

    return None  # No path found


def generate_plan(start, place_type, max_travel_hours, budget, num_days, return_to_start=False):
    filtered_places = [place for place in kerala_graph.nodes if kerala_graph.nodes[place]["type"] == place_type]
    alternative_budgets = {"Low": ["Mid"], "Mid": ["Low", "High"], "High": ["Mid"]}
    possible_places = [
        place for place in filtered_places
        if
        kerala_graph.nodes[place]["budget"] == budget or kerala_graph.nodes[place]["budget"] in alternative_budgets.get(
            budget, [])
    ]

    if not possible_places:
        return "No matching destinations found!"

    visited_places = set()
    daily_plan = {}
    current_location = start

    for day in range(1, num_days + 1):
        # Sort by heuristic + user preferences (e.g., rating, popularity)
        sorted_places = sorted(possible_places, key=lambda x: (
        heuristic(current_location, x, kerala_graph), -kerala_graph.nodes[x].get("rating", 0)))

        day_plan = []
        total_time_spent = 0

        for place in sorted_places:
            if place in visited_places:
                continue

            path = a_star_search(kerala_graph, current_location, place)
            if not path:
                continue  # Skip unreachable places

            travel_time = sum(kerala_graph[u][v]['travel_time'] for u, v in zip(path[:-1], path[1:]))
            if total_time_spent + travel_time <= max_travel_hours:
                day_plan.append({"route": path, "travel_time": travel_time})
                total_time_spent += travel_time
                visited_places.add(place)
                current_location = place

            if total_time_spent >= max_travel_hours:
                break

        if day_plan:
            daily_plan[f"Day {day}"] = day_plan
        if not set(possible_places) - visited_places:
            break

    if return_to_start and current_location != start:
        return_path = a_star_search(kerala_graph, current_location, start)
        if return_path:
            return_time = sum(kerala_graph[u][v]['travel_time'] for u, v in zip(return_path[:-1], return_path[1:]))
            daily_plan[f"Return to {start}"] = [{"route": return_path, "travel_time": return_time}]

    return daily_plan


# New user preferences
# New user preferences
user_input = {
    "start": "Wayanad",
    "place_type": "Waterfalls",  # Changed from "type" to "place_type"
    "max_travel_hours": 6,
    "budget": "Low",
    "num_days": 1,
    "return_to_start": True
}

# Update function to use "place_type" instead of "type"
plan = generate_plan(**user_input)
print("Recommended travel plan:", plan)


