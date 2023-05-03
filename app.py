import graphviz

with open("list.txt", 'r') as file:
    graph_data = graphviz.Graph()
    graph = []
    const =0
    while (const == 0):
        tops = file.readline()
        top = tops.split()
        if len(top) == 2:
            graph_data.edge(top[0],top[1])
            graph.append(top)
        elif len(top) == 1:
            graph_data.node(top[0])
            graph.append(top)
        else:
            print("You should enter 1 or 2 tops in every line")
            const = 1
            
    print(graph)
graph_data.view()
