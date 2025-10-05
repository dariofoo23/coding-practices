def main(event):
    # Read input fields
    average_rotation = event["inputFields"].get("average_rotation")
    average_car_price_sold = event["inputFields"].get("average_car_price_sold")
    average_stock = event["inputFields"].get("average_stock")
    current_stock = event["inputFields"].get("current_stock")
    turnover_leparking = event["inputFields"].get("turnover_leparking")
    cars_sold = event["inputFields"].get("cars_sold")
    eligible_park = event["inputFields"].get("eligible_park")

    def match_range(value, ranges):
        for r in ranges:
            if isinstance(r, tuple) and r[0] <= value <= r[1]:
                return True
            elif isinstance(r, str) and r.startswith(">"):
                if value > float(r[1:]):
                    return True
        return False

    def calculate_score(metric_name, value, rules):
        try:
            val_float = float(value)
        except (TypeError, ValueError):
            print(f"{metric_name}: MISSING or invalid → 4.5 points")
            return 4.5

        if match_range(val_float, rules["good"]):
            print(f"{metric_name}: {val_float} → GOOD → 10 points")
            return 10
        elif match_range(val_float, rules["ok"]):
            print(f"{metric_name}: {val_float} → OK → 8 points")
            return 8
        elif match_range(val_float, rules["poor"]):
            print(f"{metric_name}: {val_float} → POOR → 5 points")
            return 5
        else:
            print(f"{metric_name}: {val_float} → OUTSIDE SCALE → 0 points")
            return 0

    # Rules per metric
    metric_rules = {
        "average_rotation": {
            "good": [(0, 60)],
            "ok": [(60, 100)],
            "poor": [(100, 120)]
        },
        "average_car_price_sold": {
            "good": [(10000, 20000)],
            "ok": [(5000, 10000), (20000, 30000)],
            "poor": [(0, 5000), (30000, 50000)]
        },
        "average_stock": {
            "good": [(30, 60)],
            "ok": [(10, 30)],
            "poor": [(5, 10), (60, 100)]
        },
        "current_stock": {
            "good": [(30, 60)],
            "ok": [(5, 30)],
            "poor": [(0, 5), (60, 100)]
        },
        "turnover_leparking": {
            "good": [">300000"],
            "ok": [(200000, 300000)],
            "poor": [(150000, 200000)]
        },
        "cars_sold": {
            "good": [(90, 180)],
            "ok": [(30, 90)],
            "poor": [(15, 30), (180, 300)]
        },
        "eligible_park": {
            "good": [(40, 100)],
            "ok": [(20, 40)],
            "poor": [(0, 20)]
        }
    }

    # Input mapping
    data = {
        "average_rotation": average_rotation,
        "average_car_price_sold": average_car_price_sold,
        "average_stock": average_stock,
        "current_stock": current_stock,
        "turnover_leparking": turnover_leparking,
        "cars_sold": cars_sold,
        "eligible_park": eligible_park
    }

    print("---- Metric Score Breakdown ----")
    total_points = 0
    for key, value in data.items():
        rules = metric_rules.get(key)
        score = calculate_score(key, value, rules)
        total_points += score

    # Final result
    business_score = round((total_points / 70) * 100, 2)

    print(f"Total unadjusted score: {total_points}")
    print(f"Final rebased business score (out of 100): {business_score}")

    return {
        "outputFields": {
            "business_score": business_score
        }
    }