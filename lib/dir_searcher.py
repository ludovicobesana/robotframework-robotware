import requests

def dir_searcher(host, dictionary): 
    
    url = 'https://' + host + '/'   

    ok_status = [] 
    
    for i in range(len(dictionary)): 

        response = requests.get(url + dictionary[i]) 
        if response.status_code == 200:
            
            ok_status.append(dictionary[i]) 
        else:
                        
            print("Error 404: " + url + dictionary[i] + " does not exist") 
    return ok_status

dict = ["skdjfhiksudhfoiusd", "robot"]

print("Found: " + str(dir_searcher("it.wikipedia.org/wiki", dict)))
