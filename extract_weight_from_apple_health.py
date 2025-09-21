import xml.etree.ElementTree as ET
import csv
from datetime import datetime
from collections import defaultdict

INPUT_FILE = "export.xml"
OUTPUT_FILE = "fitbit_full.csv"

TYPES = {
    "HKQuantityTypeIdentifierBodyMass": "weight",
    "HKQuantityTypeIdentifierBodyMassIndex": "bmi",
    "HKQuantityTypeIdentifierBodyFatPercentage": "fat"
}

def extract_body_records(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data = defaultdict(dict)

    for record in root.findall('Record'):
        record_type = record.attrib.get('type')
        if record_type in TYPES:
            date_raw = record.attrib['startDate']
            value = float(record.attrib['value'])

            # Normalize date to YYYY-MM-DD
            try:
                parsed_date = datetime.strptime(date_raw, "%Y-%m-%d %H:%M:%S %z")
                date = parsed_date.strftime("%Y-%m-%d")
            except Exception:
                date = date_raw[:10]

            # Convert fat from 0.15 → 15.0%
            if record_type == "HKQuantityTypeIdentifierBodyFatPercentage":
                value *= 100

            key = TYPES[record_type]
            if key not in data[date]:
                data[date][key] = value  # keep first for date

    return data

def write_to_fitbit_csv(data, output_file):
    with open(output_file, mode='w', newline='') as f:
        f.write("Body\n")
        writer = csv.writer(f)
        writer.writerow(["Date", "Weight", "BMI", "Fat"])
        for date in sorted(data.keys()):
            weight = data[date].get("weight", "")
            bmi = data[date].get("bmi", "0")
            fat = data[date].get("fat", "0")
            if weight != "":
                writer.writerow([date, weight, bmi, fat])

    print(f"✅ Создан файл: {output_file} ({len(data)} дней с весом)")

if __name__ == "__main__":
    try:
        body_data = extract_body_records(INPUT_FILE)
        write_to_fitbit_csv(body_data, OUTPUT_FILE)
    except FileNotFoundError:
        print(f"❌ Файл не найден: {INPUT_FILE}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
