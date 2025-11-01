from collections import defaultdict


graph = defaultdict(list)
graph["E"]  = [["T", "E'"]]
graph["E'"] = [["+", "T", "E'"], ["ε"]]
graph["T"]  = [["F", "T'"]]
graph["T'"] = [["*", "F", "T'"], ["ε"]]
graph["F"]  = [["(", "E", ")"], ["id"]]

target_symbol = ["(" ,"id","+","id","*","id" , ")"]
non_terminals = set(graph.keys())

def TopDownParsing(curr_symbol, target_index):
    
    if curr_symbol == "ε":
        return True, target_index

   
    if curr_symbol not in non_terminals:
        if target_index < len(target_symbol) and curr_symbol == target_symbol[target_index]:
            return True, target_index + 1
        return False, target_index

   
    for production in graph[curr_symbol]:
        temp_index = target_index
        success = True
        for symb in production:
            ok, temp_index = TopDownParsing(symb, temp_index)
            if not ok:
                success = False
                break
        if success:
            return True, temp_index

    return False, target_index


result, final_index = TopDownParsing("E", 0)

if result and final_index == len(target_symbol):
    print(f"Accepted: The input {target_symbol} is syntactically correct!")
else:
    print(f"Rejected: The input  {target_symbol} is NOT syntactically correct.")
