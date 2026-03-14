from sklearn.tree import DecisionTreeClassifier

print("Play Outside Prediction System")
print("-------------------------------")

# Training dataset
weather_data = [
    ["Sunny", "Hot"],
    ["Sunny", "Cool"],
    ["Rainy", "Mild"],
    ["Overcast", "Cool"],
    ["Rainy", "Cool"]
]

play = ["No", "Yes", "Yes", "Yes", "Yes"]

# Encode values
encoding = {"Sunny":0, "Rainy":1, "Overcast":2,
            "Hot":0, "Mild":1, "Cool":2}

X = [[encoding[w], encoding[t]] for w,t in weather_data]

model = DecisionTreeClassifier()
model.fit(X, play)

weather = input("Enter weather (Sunny/Rainy/Overcast): ").capitalize()
temperature = input("Enter temperature (Hot/Mild/Cool): ").capitalize()

prediction = model.predict([[encoding[weather], encoding[temperature]]])

print("-------------------------------")
print("Prediction:", prediction[0])
print("-------------------------------")