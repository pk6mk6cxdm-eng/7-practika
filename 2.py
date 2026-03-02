import json

class EcoRegion:
    def __init__(self, name, water_quality, air_pollution):
        self.name = name
        self.water_quality = water_quality
        self.air_pollution = air_pollution

    def __str__(self):
        return (f"{self.name} | "
                f"Су сапасы: {self.water_quality} | "
                f"Ауа индексі: {self.air_pollution}")

    def to_dict(self):
        return {
            "name": self.name,
            "water_quality": self.water_quality,
            "air_pollution": self.air_pollution
        }

    @staticmethod
    def from_dict(data):
        return EcoRegion(
            data["name"],
            data["water_quality"],
            data["air_pollution"]
        )


regions = []

n = int(input("Қанша аймақ енгізесіз? "))

for i in range(n):
    print(f"\n{i+1}-аймақ:")
    name = input("Аймақ атауы: ")
    water = float(input("Су сапасы мәні: "))
    air = float(input("Ауа ластану индексі: "))

    regions.append(EcoRegion(name, water, air))

with open("eco_data.json", "w", encoding="utf-8") as file:
    json.dump([r.to_dict() for r in regions],
              file, ensure_ascii=False, indent=4)

print("\nМәліметтер файлға сақталды.")


with open("eco_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

loaded_regions = [EcoRegion.from_dict(d) for d in data]


cleanest_region = max(loaded_regions, key=lambda r: r.water_quality)

print("\nЕң таза суы бар аймақ:")
print(cleanest_region)

polluted_regions = [r for r in loaded_regions if r.air_pollution > 50]

print("\nАуа ластануы 50-ден жоғары аймақтар:")
for r in polluted_regions:
    print(r)