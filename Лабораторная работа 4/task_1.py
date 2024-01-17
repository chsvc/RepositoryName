# # TODO решите задачу
import json


def task(file) -> float:
    with open(file) as f:
        json_data = json.load(f)

    sum_values = sum([item["score"] * item["weight"] for item in json_data])
    return round(sum_values, 3)


input_ = "input.json"
print(task(input_))
