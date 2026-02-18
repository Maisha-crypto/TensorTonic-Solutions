def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    step_distances = []
    results = []

    # loop through each of the points
    for p in points:
        
        step_distances.clear()
        
        
        for c in centroids:
          
          # distance to center 
          step_distance = (p[0]-c[0])**2 + (p[1]-c[1])**2
          step_distances.append(step_distance)
        # get the min diatnce
        min_distance = min(step_distances)
        print(min_distance)
        
        #results.append(f"{p} distance to {c} is {step_distance}")
        
    #print(results)  
    
    # for each point, compute the distance from the centroid
    # asign the point to the nearest centroid
      
points = [[1,1],[1,2],[10,10],[10,11]]
centroids = [[0,0],[11,11]]

k_means_assignment(points, centroids)
