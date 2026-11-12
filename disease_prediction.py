import pandas as pd

data =pd.read_csv("Disease_symptom_and_patient_profile_dataset.csv")

print("Dataset loaded successfully!")
print(data.head( ))

print("\nColumns in dataset:")
print(data.columns.tolist( ))

print("\nDisease distribution:")
print(data["Disease"].value_counts( ))

print("\nDisease with very few records:")
print(data["Disease"].value_counts( )[data["Disease"].value_counts( ) <= 2])

print("\nNumber of diseases with 2 oe fewer records:")
print((data["Disease"].value_counts( ) <=2).sum( ))

x =  data.drop("Disease", axis=1)
y= data["Disease"]

print("\nInput features:")
print(x.columns.tolist( ))

print("\nTarget:")
print(y.name)

from sklearn.preprocessing import LabelEncoder

encoder = LabelEncoder()

for column in x.columns:

      x[column] = encoder.fit_transform(x[column].astype(str))

print("\nEncoded data:")
print(x.head( ))

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

print("\nTraining data:", x_train.shape)
print("Testing data:", x_test.shape)

from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
         random_state=42
)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

while True:

    print("\nEnter patient details:")
    print("----------------")

    fever = input("Enter Fever (Yes/No): ")
    cough = input("Enter Cough (Yes/No): ")
    fatigue = input("Enter Fatigue (Yes/No): ")
    difficulty = input("Enter Difficulty Breathing (Yes/No): ")
    age = input("Enter Age: ")
    gender = input("Enter Gender (Male/Female): ")
    blood_pressure = input("Enter Blood Pressure (Low/Normal/High): ")
    cholesterol = input("Enter Cholesterol Level (Low/Normal/High): ")
    outcome = input("Enter Outcome Variable (Positive/Negative): ")

    fever = 1 if fever == "Yes" else 0
    cough = 1 if cough == "Yes" else 0
    fatigue = 1 if fatigue == "Yes" else 0
    difficulty = 1 if difficulty == "Yes" else 0
    age = int(age)
    gender = 1 if gender == "Male" else 0
    blood_pressure = 0 if blood_pressure == "High" else 1 if blood_pressure == "Low" else 2
    cholesterol = 0 if cholesterol == "Low" else 1 if cholesterol == "Normal" else 2
    outcome = 1 if outcome == "Positive" else 0

    patient_data = pd.DataFrame([[
        fever,
        cough,
        fatigue,
        difficulty,
        age,
        gender,
        blood_pressure,
        cholesterol,
        outcome
    ]], columns=x.columns)

    prediction = model.predict(patient_data)

    print("\nPredicted Disease:", prediction[0])

    again = input("\nDo you want to test another patient? (Yes/Q): ")

    if again.upper() == "Q":
        print("\nProgram ended.")
        break