from sklearn.neighbors import NearestNeighbors
import numpy as np

# Movie dataset (features: Action, Romance, SciFi)
movies = [
    "Avengers",
    "Titanic",
    "Interstellar",
    "Fast & Furious",
    "Notebook"
]

features = np.array([
    [1,0,1],  # Avengers
    [0,1,0],  # Titanic
    [1,0,1],  # Interstellar
    [1,0,0],  # Fast & Furious
    [0,1,0]   # Notebook
])

# Train KNN model
model = NearestNeighbors(n_neighbors=2)
model.fit(features)

# User preference (Action + SciFi)
user_preference = np.array([[1,0,1]])

distances, indices = model.kneighbors(user_preference)

print("\nRecommended Movies:")

for i in indices[0]:
    print(movies[i])

