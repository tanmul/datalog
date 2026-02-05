# Autonomous Data Catalog

**Autonomous Data Catalog** is a library that brings automated data cataloging to non-technical engineers and analysts. It integrates seamlessly with a **SQLAlchemy Engine** to retrieve and update a cached catalog of your database tables.

## Features

- **Graph Analysis**
  - Lineage tracking (upstream/downstream)
  - Cyclic dependency detection
  - Root table analysis
- **Catalog Search**
  - Filtering and regex search across tables and columns
  - Column and SQL parsing
- **Flexible AI Integration**
  - Fully functional without GenAI
  - Optional GenAI plug-in for a “chat-like” interface to query catalog information
