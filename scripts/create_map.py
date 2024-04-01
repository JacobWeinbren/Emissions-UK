import csv
import json
from tqdm import tqdm


def load_csv_data(csv_file_path):
    """Load CSV data into a dictionary."""
    print("Loading CSV data...")
    data = {}
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in tqdm(csv_reader, desc="Processing CSV rows"):
            geo_code = row.pop("Geographic Code")
            attributes = {k: float(v) for k, v in row.items() if k != "population"}
            data[geo_code] = {
                "attributes": attributes,
                "total": sum(attributes.values()),
            }
    print("CSV data loaded successfully.")
    return data


def update_geojson_features(geojson_data, csv_data):
    """Update GeoJSON features with CSV data."""
    print("Updating GeoJSON features...")
    for feature in tqdm(geojson_data["features"], desc="Updating features"):
        geo_code = feature["properties"]["geo_code"]
        if geo_code in csv_data:
            feature["properties"] = {
                "geo_code": geo_code,
                "total": csv_data[geo_code]["total"],
            }
        else:
            print(geo_code)
    print("GeoJSON features updated successfully.")


def main():
    csv_file_path = "output/Average_COICOP3.csv"
    geojson_file_path = "data/map.geojson"
    updated_geojson_file_path = "output/updated_map.geojson"

    # Load the CSV data
    csv_data = load_csv_data(csv_file_path)

    # Load the GeoJSON data
    print("Loading GeoJSON data...")
    with open(geojson_file_path, mode="r", encoding="utf-8") as file:
        geojson_data = json.load(file)
    print("GeoJSON data loaded successfully.")

    # Update the GeoJSON features with the CSV data
    update_geojson_features(geojson_data, csv_data)

    # Save the updated GeoJSON data
    print("Saving updated GeoJSON data...")
    with open(updated_geojson_file_path, mode="w", encoding="utf-8") as file:
        json.dump(geojson_data, file, indent=4)
    print(f"Updated GeoJSON file saved to {updated_geojson_file_path}")


if __name__ == "__main__":
    main()
