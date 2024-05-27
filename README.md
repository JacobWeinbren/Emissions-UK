# Emissions UK

Mapping Per Capita Emissions in the UK

This project visualises per capita greenhouse gas emissions across the UK, covering Wales, England, Scotland, and Northern Ireland. It utilises geographic boundaries from the 2011 Census for Lower Layer Super Output Areas and Data Zones.

## Source Study

[Per Capita Consumption-Based Greenhouse Gas Emissions for UK Lower and Middle Layer Super Output Areas, 2016](https://reshare.ukdataservice.ac.uk/854888/)

This study integrates data from three sources - Output Area Classification, the Living Costs and Food Survey, and a commercial household expenditure dataset by TransUnion. The project averages these datasets to enhance output reliability.

## Geographic Data Source

[2011 Census Geography Boundaries (Lower Layer Super Output Areas and Data Zones)](https://statistics.ukdataservice.ac.uk/dataset/2011-census-geography-boundaries-lower-layer-super-output-areas-and-data-zones)

## Setup

Clone the repository and navigate into it:

```bash
git clone <repository-url>
cd emissions-uk
```

### Backend Setup

1. Install Python dependencies:

    ```bash
    pip install pandas tqdm
    ```

2. Process the data:

    ```bash
    python scripts/process.py

    ```

3. Generate the map:

    ```bash
    python scripts/create_map.py

    ```

4. Generate map tiles (ensure `tippecanoe` is installed):

    ```bash
    tippecanoe --output="output/uk-emissions.pmtiles" \
        --layer="maplayer" \
        --no-feature-limit \
        --no-tile-size-limit \
        --detect-shared-borders \
        --coalesce-fraction-as-needed \
        --coalesce-densest-as-needed \
        --coalesce-smallest-as-needed \
        --increase-gamma-as-needed \
        --coalesce \
        --reorder \
        --minimum-zoom=0 \
        --maximum-zoom=17 \
        --force \
        --simplification=20 \
        output/updated_map.geojson
    ```

5. Data Analysis:

    ```bash
    python scripts/median.py
    ```

### Frontend Setup

Navigate to the `site` directory:

    ```bash
    cd site
    ```

Install dependencies:

    ```bash
    npm install
    ```

Run the project locally:

    ```bash
    npm run dev
    ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
