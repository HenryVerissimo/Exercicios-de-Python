from dataclasses import dataclass

@dataclass
class TemperatureAnalysis:
    anomalous: int
    valid_average: float
    first_maximum_valid_index: int


def calculate_temperature_analysis(list_values: list) -> TemperatureAnalysis:
    anomalous: int = 0
    valid_values: list = []
    valid_average: float = 0
    maximum_value: float | None = None
    first_maximum_valid_index: int = -1

    for index, value in enumerate(list_values):
        if (value < 10) or (value > 30):
            anomalous += 1
            continue

        valid_values.append(value)

        if (maximum_value is None) and (value >= 10):
            maximum_value = value
            first_maximum_valid_index = index

        elif value > maximum_value:
            maximum_value = value
            first_maximum_valid_index = index

    if len(valid_values) != 0:
        valid_average = sum(valid_values) / len(valid_values)

    return TemperatureAnalysis(anomalous, valid_average, first_maximum_valid_index)


if __name__ == "__main__":

    some_temperature_values = [20, 30, 35, 22, 33, 15, 29, 24, 22, 31]

    temperature_analysis = calculate_temperature_analysis(some_temperature_values)

    print(temperature_analysis.anomalous)
    print(temperature_analysis.valid_average)
    print(temperature_analysis.first_maximum_valid_index)