"""
"""
def quality_control(product_scores, threshold):
    new_dict={}
    for key, value in product_scores.items():
        if value >= threshold:
            new_dict[key] = "pass"
        else:
            new_dict[key] = "fail"

    return new_dict

#test case
product_scores = {"x0123": 75, "x0124": 40, "x0125": 90, "x0126": 55}
threshold= 60

print(quality_control(product_scores, threshold))
