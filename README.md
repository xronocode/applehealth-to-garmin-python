
# Apple Health to Garmin CSV (Python Version)

🩺→🖥→ 📊 A lightweight Python script to convert Apple Health export data into a Garmin-compatible CSV for weight tracking.

## 📊 What it does

This script parses `export.xml` from Apple Health and extracts:

- Body weight (kg)
- Body Mass Index (BMI)
- Body Fat Percentage (%)

Then it generates a `fitbit_full.csv` file compatible with Garmin Connect's Fitbit CSV import.

---

## 📆 Example output

```
Body
Date,Weight,BMI,Fat
2023-07-01,82.5,24.9,15.3
2023-07-03,82.2,25.1,14.7
```

---

## 📅 How to use it

### 1. Export data from Apple Health
- Open the Health app on your iPhone
- Tap your profile (top right)
- Scroll down and choose **Export All Health Data**
- Save the `.zip` and extract `export.xml`

### 2. Run the script

1. Install Python 3 (if not installed)
2. Clone this repository
3. Place `export.xml` next to the script
4. Run:

```bash
python extract_body_data_for_fitbit.py
```

You will get `fitbit_full.csv`

---

## 📥 Upload to Garmin

1. Go to: [https://connect.garmin.com/modern/weight](https://connect.garmin.com/modern/weight)
2. Click ⚙️ **Import** (top right)
3. Select **Fitbit CSV** format
4. Upload the `fitbit_full.csv` file

Your weight data will appear on the graph.

---

## 📊 Technical Details

- Written in **pure Python 3**
- Uses built-in libraries: `xml.etree.ElementTree`, `csv`, `datetime`
- No dependencies

Supports Apple Health types:
- `HKQuantityTypeIdentifierBodyMass`
- `HKQuantityTypeIdentifierBodyMassIndex`
- `HKQuantityTypeIdentifierBodyFatPercentage`

---

## 👉 Russian / Русская версия

### Для чего

Скрипт на Python позволяет экспортировать вес, ИМТ и процент жира из Apple Health в CSV-формат, совместимый с Garmin.

### Как использовать

1. Экспорт данных в Health на iPhone
2. Сохрани `export.xml`
3. Скопируй его в папку скрипта
4. Запусти в терминале:

```bash
python extract_body_data_for_fitbit.py
```

5. Файл `fitbit_full.csv` готов к загрузке в Garmin.

---

## 👤 Author

Forked and rewritten in Python by [Your Name] — lightweight alternative to JavaScript-based Apple Health parsing tools.

Original idea inspired by [arthurgousset/applehealth](https://github.com/arthurgousset/applehealth).
