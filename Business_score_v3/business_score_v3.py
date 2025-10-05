def main(event):

    # Read input fields
    average_rotation = event["inputFields"].get("average_rotation")
    average_car_price_sold = event["inputFields"].get("average_car_price_sold")
    average_stock = event["inputFields"].get("average_stock")
    current_stock = event["inputFields"].get("current_stock")
    turnover_leparking = event["inputFields"].get("turnover_leparking")
    cars_sold = event["inputFields"].get("cars_sold")
    eligible_park = event["inputFields"].get("eligible_park")
    credit_score = event["inputFields"].get("credit_score")

    # Convert credit_score to float safely
    print("credit_score (raw):", credit_score)
    try:
        credit_score = float(credit_score)
    except (TypeError, ValueError):
        credit_score = None
    print("credit_score (converted):", credit_score)

    # Define scoring function
    def calculate_business_score(data, credit_score=None):

        # Constants
        TOTAL_POINTS = 100
        METRIC_COUNT = 7
        METRIC_WEIGHT = TOTAL_POINTS / METRIC_COUNT
        MISSING_POINTS = METRIC_WEIGHT / 2

        # Metric rules
        metrics = [
            {
                "name": "average_rotation",
                "min": 0,
                "max": 120,
                "higher_is_better": False
            },
            {
                "name": "average_car_price_sold",
                "min": 0,
                "max": 50000,
                "higher_is_better": False
            },
            {
                "name": "average_stock",
                "min": 10,
                "max": 100,
                "higher_is_better": True
            },
            {
                "name": "current_stock",
                "min": 5,
                "max": 100,
                "higher_is_better": True
            },
            {
                "name": "turnover_leparking",
                "min": 200000,
                "max": 3000000,
                "higher_is_better": True
            },
            {
                "name": "cars_sold",
                "min": 60,
                "max": 600,
                "higher_is_better": True
            },
            {
                "name": "eligible_park",
                "min": 0,
                "max": 100,
                "higher_is_better": True
            }
        ]

        business_score = 0

        for metric in metrics:
            value = data.get(metric["name"])

            # Attempt to convert to float if value is not None
            try:
                value = float(value)
            except (TypeError, ValueError):
                value = None

            min_val = metric["min"]
            max_val = metric["max"]

            if value is None:
                points = MISSING_POINTS
            else:
                if metric["higher_is_better"]:
                    if value < min_val or value > max_val:
                        points = 0
                    else:
                        points = METRIC_WEIGHT * (value - min_val) / (max_val - min_val)
                else:
                    if value < min_val or value > max_val:
                        points = 0
                    else:
                        points = METRIC_WEIGHT * (max_val - value) / (max_val - min_val)

            # Add to total
            business_score += points

        # Now handle match score logic
        if credit_score is None and business_score == 0:
            # If both missing, assign 50 to both
            credit_score = 50
            business_score = 50
        elif credit_score is None:
            credit_score = 50
        elif business_score == 0:
            business_score = 50

        # Final match score
        match_score = (0.7 * credit_score) + (0.3 * business_score)

        # Return results
        return {
            "business_score": round(business_score, 2),
            "credit_qualification_score": credit_score,
            "match_score": round(match_score, 2)
        }

    # Prepare data dictionary
    data = {
        "average_rotation": average_rotation,
        "average_car_price_sold": average_car_price_sold,
        "average_stock": average_stock,
        "current_stock": current_stock,
        "turnover_leparking": turnover_leparking,
        "cars_sold": cars_sold,
        "eligible_park": eligible_park
    }

    print("data:", data)

    # Call the function with correct variable
    result = calculate_business_score(data, credit_score)

    print("result:", result)

    # Final return
    return {
        "outputFields": {
            "business_score": result["business_score"],
            "match_score": result["match_score"],
            "credit_score": result["credit_qualification_score"]
        }
    }
