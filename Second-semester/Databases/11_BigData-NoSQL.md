## Big Data and NoSQL Overview

**Big Data** refers to extremely large datasets that are difficult to process and analyze using traditional data processing techniques. The three Vs of Big Data are:

1. **Volume**: Massive amounts of data.
2. **Velocity**: Rapid generation and processing of data.
3. **Variety**: Different types of data, such as structured, unstructured, and semi-structured.

## Selected Big Data Challenges
1. **Massive Point Clouds**: Example - 640 billion (x,y,z) points, 15 TB of data, requiring spatial joins.
2. **GPS Data**: Over 5 trillion GPS points growing at more than 60,000 points per second.
3. **File Storage**: Around 4 million files, approximately 500 GB.
4. **Satellite Imagery**: About 2 PB of satellite image data, requiring array data processing.
5. **GIS, Logistics, Seismology, and Remote Sensing**: High data volume and complexity in processing.

## Paradigm Shift in Scientific Research
Jim Gray identified a shift in scientific research paradigms:
1. **Empirical**: Experimental data collection.
2. **Theoretical**: Development of theories and models.
3. **Computational**: Simulation of complex systems.
4. **Data Exploration (eScience)**: Analysis and exploration of large datasets.

## DBMS Architecture Changes
1. **Memory Wall**: A significant performance bottleneck where the CPU waits for memory access, leading to high idle times.
2. **Columnar Storage**: Transition from row-wise to column-wise storage for better performance.
   - **DSM (Decomposed Storage Model)**: Storing data column-by-column instead of row-by-row.
3. **CPU and Cache-Conscious Algorithms**: Designing algorithms that optimize CPU and cache usage.

## Consistency Models
- **NoSQL**: BASE (Basically Available, Soft state, Eventual consistency).
- **RDBMS**: ACID (Atomicity, Consistency, Isolation, Durability).

## Modern Developments
1. **Relational Database as a Service in the Cloud**.
2. **Cloud-native Graph Analytics**.
3. **In-process Analytical Database**.
4. **Cloud-based Data Analysis Platforms**: Utilizing Spark and relational technologies.
5. **SQL:2023 Standard**: Incorporating Property Graph Queries (SQL/PGQ).
6. **Serverless Data Warehouses**: Powered by technologies like DuckDB.
