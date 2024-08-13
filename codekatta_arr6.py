from collections import Counter

def find_non_unique_ids():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    # Reading the number of prisoners (not actually used)
    n = int(data[0])
    
    # Reading the prisoner IDs
    ids = list(map(int, data[1:]))
    
    # Count occurrences of each ID
    id_count = Counter(ids)
    
    # Find non-unique IDs
    non_unique_ids = [id for id, count in id_count.items() if count > 1]
    
    if non_unique_ids:
        # Print non-unique IDs, space-separated
        print(" ".join(map(str, sorted(non_unique_ids))))
    else:
        # Print -1 if all IDs are unique
        print(-1)


#exaple
find_non_unique_ids()
