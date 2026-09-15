def create_embeddings(chunks):
    embeddings = []

    for chunk in chunks:
        embeddings.append([float(len(chunk))])

    return embeddings