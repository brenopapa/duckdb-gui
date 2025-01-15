# DuckDB GUI 🦆📊

A graphical user interface designed to simplify the use of DuckDB outside the command line. This application uses Streamlit as a GUI, providing an intuitive way to interact with a DuckDB database.

## Purpose 🎯

DuckDB GUI enables users to easily execute queries, visualize results, and manage DuckDB databases directly through a Streamlit interface. It eliminates the need for the command line, making it more accessible to non-technical users and enhancing productivity.

## Features ⚡

- Execute SQL queries on DuckDB 📝
- Visualize query results in real-time 📈
- Manipulate data directly through the Streamlit interface 🖱️
- Configure DuckDB database settings within the app ⚙️

## Installation 🔧

1. Clone the repository:
   ```bash
   git clone https://github.com/brenopapa/duckdb-gui.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run Home.py
   ```

## Docker Deployment 🐳

This application includes a `Dockerfile` for easy deployment using Docker.

### Build the Docker Image 🏗️

To build the Docker image, run the following command in the project directory:

```bash
docker build -t duckdb-gui .
```

### Run the Docker Container 🚀

Once the image is built, you can run the app in a Docker container:

```bash
docker run -p 8501:8501 duckdb-gui
```

The app will be accessible at `http://localhost:8501`.

## Configuration ⚙️

You can configure the DuckDB database settings directly within the app to connect to an existing database or create a new one.

## TDB (To Be Developed) 🔮

The following features are planned for future development:

- **Custom Elements:** The app will allow users to create and add custom elements with distinct behaviors, offering greater flexibility in interacting with the database. ✨
- **Additional Charts:** More charts will be added to the volumes page, enhancing the data visualization capabilities. 📊
- **Default Queries:** The app will have predefined queries that run on startup, making it easier for users to begin working with the database immediately. 🔄

## Architecture Diagram 🔄

```
           ┌─────────────┐        ┌─────────────┐        ┌───────────────┐
           │  DuckDB     │ ◄───►  │ Streamlit   │ ◄───►  │     User      │
           │  Database   │        │ Interface   │        │ Interractions │
           └─────────────┘        └─────────────┘        └───────────────┘

```

## License 📝

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like more changes or improvements!