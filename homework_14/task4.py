def chunk_data(data, chunk_size):
    chunks = ()
    i = 0
    while i < len(data):
        chunks += (tuple(data[i:i + chunk_size]),)
        i += chunk_size
    
    print("Chunks:")
    for chunk in chunks:
        print(chunk)
    
    return chunk

chunk_data([1, 2, 3, 4, 5, 6, 7, 8], 3)
chunk_data([1, 2, 3, 4, 5, 6, 7, 8], 2)