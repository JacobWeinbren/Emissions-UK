# Emissions UK

Mapping Per Capita Emissions in the UK

This project visualises per capita greenhouse gas emissions across the UK, covering Wales, England, Scotland, and Northern Ireland. It utilises geographic boundaries from the 2011 Census for Lower Layer Super Output Areas and Data Zones.

Source Study: [Per Capita Consumption-Based Greenhouse Gas Emissions for UK Lower and Middle Layer Super Output Areas, 2016](https://reshare.ukdataservice.ac.uk/854888/)

The study takes from three sources - Output Area Classification, the Living Costs and Food Survey, and a commercial household expenditure dataset by TransUnion. This project takes the average of these three datasets, to improve the output's reliability.

Geographic Data Source: [2011 Census Geography Boundaries (Lower Layer Super Output Areas and Data Zones)](https://statistics.ukdataservice.ac.uk/dataset/2011-census-geography-boundaries-lower-layer-super-output-areas-and-data-zones)

Developed in Python.

Frontend implemented with deck.gl and Astro. To run the project locally, navigate to the `site` directory and execute `npm run dev`.
