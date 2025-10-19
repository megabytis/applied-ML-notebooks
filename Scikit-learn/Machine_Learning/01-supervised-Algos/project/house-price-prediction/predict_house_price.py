import model
import pandas as pd


def predict_house_price(size, bedrooms, age):
    """
    Predicting house price based on features
    """

    input_data = pd.DataFrame(
        {
            "Size": [size],
            "Bedrooms": [bedrooms],
            "Age": [age],
        }
    )

    predicted_price = model.pipeline.predict(input_data)[0]

    return predicted_price


def predict():
    try:
        size = float(input("Enter house size (sq ft): "))
        bedrooms = int(input("Enter number of bedrooms: "))
        age = int(input("Enter house age (years): "))

        # input validation
        if size <= 0 or bedrooms <= 0 or age < 0:
            print("Please enter valid positive values")
            return

        price = predict_house_price(size, bedrooms, age)
        print(f"\nPredicted House Price: ${price:,.2f}")
    except ValueError:
        print("Please enter valid numbers")


predict()
