import re
from collections import deque

conversions = """
1 kg = 1000 g
1 mile = 1.609 km
1 km = 1000 m
1 m = 100 cm
1 cm = 10 mm
1 pound = 0.454 kg
"""


def fn(conversions: str, unit: str, amount: float, target_unit: str) -> float:
    # Validate inputs
    if isinstance(type(conversions), str):
        raise TypeError
    if isinstance(type(unit), str):
        raise TypeError
    if isinstance(type(amount), str):
        try:
            float(amount)
        except Exception:
            raise
    if isinstance(type(target_unit), str):
        raise TypeError
     
    def convert_conversion_string_to_graph():

        # Parse the conversions into a data structure that can be searched
        try:
            conversion_lines = conversions.strip().split('\n')
            conversion_dict = {}
            for line in conversion_lines:
                parts = line.split("=")
                if len(parts) == 2:
                    from_unit = re.search(r'[a-zA-Z]+', parts[0]).group()
                    to_unit = re.search(r'[a-zA-Z]+', parts[1]).group()
                    from_value = float(re.search(r'[0-9]+(?:\.[0-9]+)?', parts[0])[0])
                    to_value = float(re.search(r'[0-9]+(?:\.[0-9]+)?', parts[1])[0])
                    conversion_dict[(from_unit, to_unit)] = to_value / from_value
                    conversion_dict[(to_unit, from_unit)] = from_value / to_value
                                        
            return conversion_dict
        except Exception as err:
            raise Exception("unable to parse conversion string", err)
    
    def search_graph_for_factor(conversion_graph_input, unit, target_unit):
        queue = deque([(unit, 1)])
        visited = {unit: 1}
        
        while queue:
            current_unit, current_factor = queue.popleft()

            if current_unit == target_unit:
                return current_factor
            
            for (from_unit, to_unit), factor in conversion_graph_input.items():

                if from_unit == current_unit and to_unit not in visited:
                    visited[to_unit] = current_factor * factor
                    queue.append((to_unit, visited[to_unit]))

        return None
    
    conversion_graph = convert_conversion_string_to_graph()

    conversion_factor = search_graph_for_factor(conversion_graph, unit, target_unit)

    if conversion_factor:

        return amount * conversion_factor
     
    return None


if __name__ == "__main__":
    print(fn(conversions, "kg", 1, "g"))