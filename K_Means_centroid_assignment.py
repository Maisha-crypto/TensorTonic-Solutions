
# Online Python - IDE, Editor, Compiler, Interpreter
# Online Python compiler (interpreter) to run Python online.
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    step_distances = {}
    min_distances = []
    centroid_index = []

    # loop through each of the points
    for p in points:
        step_distances.clear()
        
        for index, c in enumerate(centroids):
          # distance to center 
            step_distance = (p[0]-c[0])**2 + (p[1]-c[1])**2
            
            #print(f"Eucledead distance between {c} and {p} = {step_distance}")
            step_distances.update({index: step_distance})
    
        # get the min diatnce
        min_distances.append(min(step_distances.values()))
        print(min_distances)
        for d in min_distances:
            
            for k,v in step_distances.items():
                print(k, v, d)
                if d == v:
                    centroid_index.append(k)
                   
        
        return centroid_index
    # for each point, compute the distance from the centroid
    # asign the point to the nearest centroid
      
points = [[1,1],[1,2],[10,10],[10,11]]
centroids = [[0,0],[11,11]]

print(k_means_assignment(points, centroids))
