import json
from datetime import datetime

class Experiment:
    def __init__(self, name, date, result):
        self.name = name
        self.date = date
        self.result = result

    def __str__(self):
        return f"{self.name} | {self.date} | Нәтиже: {self.result}"

    def to_dict(self):
        return {
            "name": self.name,
            "date": self.date,
            "result": self.result
        }

    @staticmethod
    def from_dict(data):
        return Experiment(data["name"], data["date"], data["result"])

experiments = []

n = int(input("Қанша эксперимент енгізгіңіз келеді? "))

for i in range(n):
    print(f"\n{i+1}-эксперимент:")
    name = input("Атауы: ")
    date = input("Күні (YYYY-MM-DD форматында): ")
    result = input("Нәтижесі: ")

    experiments.append(Experiment(name, date, result))

with open("experiments.json", "w", encoding="utf-8") as file:
    json.dump([e.to_dict() for e in experiments],
              file, ensure_ascii=False, indent=4)

print("\nЭксперименттер файлға сақталды.")

with open("experiments.json", "r", encoding="utf-8") as file:
    data = json.load(file)

loaded_experiments = [Experiment.from_dict(d) for d in data]

latest_experiment = max(
    loaded_experiments,
    key=lambda e: datetime.strptime(e.date, "%Y-%m-%d")
)

print("\nЕң соңғы эксперимент:")
print(latest_experiment)