import pandas as pd
import pickle
import os


def load_model():
    """Load the trained pipeline with proper path handling"""
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, "churn_pipeline.pkl")

    if os.path.exists(model_path):
        return pickle.load(open(model_path, "rb"))
    else:
        raise FileNotFoundError(f"Model file not found at: {model_path}")


def predict_churn(pipeline, customer_data):
    """Predict churn for a single customer"""
    # Convert to DataFrame
    input_data = pd.DataFrame([customer_data])

    # Handle TotalCharges conversion (in case it's a string)
    if isinstance(input_data["TotalCharges"].iloc[0], str):
        try:
            input_data["TotalCharges"] = pd.to_numeric(input_data["TotalCharges"])
        except:
            input_data["TotalCharges"] = 0  # Default value for missing/invalid

    prediction = pipeline.predict(input_data)[0]
    probability = pipeline.predict_proba(input_data)[0, 1]
    return prediction, probability


def get_user_input():
    """Get customer information from user"""
    print("Customer Churn Prediction")
    print("-" * 25)

    # Numerical inputs
    tenure = int(input("Enter tenure (months): "))
    monthly_charges = float(input("Enter monthly charges ($): "))
    total_charges = input("Enter total charges ($): ")  # Keep as string initially

    # Categorical inputs
    gender = input("Enter gender (Male/Female): ").capitalize()
    senior_citizen = input("Senior citizen? (Yes/No): ").capitalize()
    partner = input("Has partner? (Yes/No): ").capitalize()
    dependents = input("Has dependents? (Yes/No): ").capitalize()
    phone_service = input("Has phone service? (Yes/No): ").capitalize()

    multiple_lines = input("Has multiple lines? (Yes/No/No phone service): ").title()
    internet_service = input("Internet service (DSL/Fiber optic/No): ").title()
    online_security = input("Has online security? (Yes/No/No internet): ").title()
    online_backup = input("Has online backup? (Yes/No/No internet): ").title()
    device_protection = input("Has device protection? (Yes/No/No internet): ").title()
    tech_support = input("Has tech support? (Yes/No/No internet): ").title()
    streaming_tv = input("Has streaming TV? (Yes/No/No internet): ").title()
    streaming_movies = input("Has streaming movies? (Yes/No/No internet): ").title()
    contract = input("Contract type (Month-to-month/One year/Two year): ").title()
    paperless_billing = input("Paperless billing? (Yes/No): ").capitalize()
    payment_method = input(
        "Payment method (Credit card, Bank transfer, etc.): "
    ).title()

    # Convert TotalCharges properly
    if total_charges.strip() == "" or total_charges.lower() == " ":
        total_charges = 0.0
    else:
        total_charges = float(total_charges)

    customer_data = {
        "gender": gender,
        "SeniorCitizen": 1 if senior_citizen == "Yes" else 0,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phone_service,
        "MultipleLines": multiple_lines,
        "InternetService": internet_service,
        "OnlineSecurity": online_security,
        "OnlineBackup": online_backup,
        "DeviceProtection": device_protection,
        "TechSupport": tech_support,
        "StreamingTV": streaming_tv,
        "StreamingMovies": streaming_movies,
        "Contract": contract,
        "PaperlessBilling": paperless_billing,
        "PaymentMethod": payment_method,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges,
    }

    return customer_data


def main():
    try:
        # Load trained model
        pipeline = load_model()

        # Get customer data
        customer_data = get_user_input()

        # Make prediction
        prediction, probability = predict_churn(pipeline, customer_data)

        # Display results
        print("\n" + "=" * 40)
        print("PREDICTION RESULTS")
        print("=" * 40)
        print(f"Churn Risk: {'YES' if prediction == 1 else 'NO'}")
        print(f"Churn Probability: {probability:.2%}")

        if prediction == 1:
            print("⚠️  High risk customer - Consider retention strategies!")
        else:
            print("✅ Customer is likely to stay")

        print(
            f"Confidence: {'HIGH' if abs(probability - 0.5) > 0.2 else 'MODERATE' if abs(probability - 0.5) > 0.1 else 'LOW'}"
        )
        print("=" * 40)

    except FileNotFoundError as e:
        print(f"Error: {e}")
        print("Please run model.py first to save the trained model.")
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
        print("Please enter numeric values for tenure, charges, etc.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

###################################
# ###### MANUL-VERSION ############
###################################

# import pandas as pd
# import pickle
# import os


# def load_model():
#     """Load the trained pipeline with proper path handling"""
#     current_dir = os.path.dirname(__file__)
#     model_path = os.path.join(current_dir, "churn_pipeline.pkl")

#     if os.path.exists(model_path):
#         return pickle.load(open(model_path, "rb"))
#     else:
#         raise FileNotFoundError(f"Model file not found at: {model_path}")


# def main():
#     try:
#         # Load trained model
#         pipeline = load_model()

#         # Manual customer data
#         customer_data = {
#             "gender": "Male",
#             "SeniorCitizen": 0,
#             "Partner": "Yes",
#             "Dependents": "No",
#             "tenure": 24,
#             "PhoneService": "Yes",
#             "MultipleLines": "No",
#             "InternetService": "DSL",
#             "OnlineSecurity": "No",
#             "OnlineBackup": "Yes",
#             "DeviceProtection": "No",
#             "TechSupport": "No",
#             "StreamingTV": "No",
#             "StreamingMovies": "Yes",
#             "Contract": "One year",
#             "PaperlessBilling": "Yes",
#             "PaymentMethod": "Credit card",
#             "MonthlyCharges": 69.99,
#             "TotalCharges": 1679.76,
#         }

#         # Convert to DataFrame
#         input_data = pd.DataFrame([customer_data])

#         # Make prediction
#         prediction = pipeline.predict(input_data)[0]
#         probability = pipeline.predict_proba(input_data)[0, 1]

#         # Display results
#         print("\n" + "=" * 40)
#         print("PREDICTION RESULTS")
#         print("=" * 40)
#         print(f"Churn Risk: {'YES' if prediction == 1 else 'NO'}")
#         print(f"Churn Probability: {probability:.2%}")

#         if prediction == 1:
#             print("⚠️  High risk customer - Consider retention strategies!")
#         else:
#             print("✅ Customer is likely to stay")

#         print(
#             f"Confidence: {'HIGH' if abs(probability - 0.5) > 0.2 else 'MODERATE' if abs(probability - 0.5) > 0.1 else 'LOW'}"
#         )
#         print("=" * 40)

#     except FileNotFoundError as e:
#         print(f"Error: {e}")
#         print("Please run model.py first to save the trained model.")
#     except Exception as e:
#         print(f"Error: {e}")


# if __name__ == "__main__":
#     main()
