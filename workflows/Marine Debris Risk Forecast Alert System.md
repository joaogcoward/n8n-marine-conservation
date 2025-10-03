### **The Problem 🚧**
Manually analyzing complex oceanographic forecast data and determining the potential risk of floating debris is time-consuming and prone to human error. Without an automated system, mission-driven organizations (like those focused on coastal conservation) have slow response times and waste valuable fieldwork time manually aggregating multi-day, multi-point data from sources like Copernicus. This drains resources that could be spent on fieldwork and strategy.

### **The Solution ✨**
Over the course of this project, I designed and built an end-to-end automation workflow using a low-code platform. This system, which we call the Marine Debris Risk Forecast Alert System, automatically:

* **Ingests Data Reliably:** Fetches the granular, multi-hour 9-day ocean current forecast data from Copernicus via a highly robust setup (using Papermill executed on Google Cloud Run).

* **Aggregates and Pre-processes:** Uses a custom Code node to group and statistically reduce hundreds of hourly points into a clean, 9-day forecast table per beach.

* **Applies Strict Analysis:** Analyzes the structured forecast data using an AI Agent with a robust, calculated prompt (including riskCounts and JSON.stringify()) to apply the strict risk rules and generate natural language summaries.

* **Generates Visual and Email Reports:** Creates a GeoJSON map layer and a professional HTML email report. The "Create Object in GCS" node features a "Retry on Fail" mechanism for publishing the map, ensuring data integrity.

* **Proactive Alerting:** Uses the powerful .some() array method to dynamically generate an "🚨 URGENT ALERT" subject line, ensuring stakeholders are alerted only when a High Risk is detected.

---

### **Source Code & Repositories 💻**

The functional logic of this system is split between the low-code workflow platform and custom cloud-hosted services. The key technical files are hosted in the following folders:

* **[GCS Map Files (Visualization)](https://github.com/joaogcoward/n8n-marine-conservation/tree/main/DRSAS/GCSMapFiles):** Contains the **Leaflet.js** HTML template and the **GeoJSON** data file. This code is responsible for rendering the final interactive risk map and providing the user interface hosted on Google Cloud Storage.
* **[Papermill (Python-CloudRun)](https://github.com/joaogcoward/n8n-marine-conservation/tree/main/DRSAS/Papermill%20(Python-CloudRun)):** Contains the **Python script** and dependencies that run on Google Cloud Run. This custom code is essential for connecting to and reliably extracting the complex data from the **Copernicus API** using Papermill.

---

### **The Real Impact 🚀**
* **100% Automation:** Eliminates the manual process of data retrieval, aggregation, and risk calculation, freeing up conservation teams for fieldwork.

* **Reliable and Auditable Data:** The AI's logic is forced to show its calculation (riskCounts), ensuring the risk level is correct and auditable.

* **Proactive Intervention:** The Dynamic Subject Line provides conditional alerting, guaranteeing immediate attention when critical conditions are met.

* **System Robustness:** The GCS Retry Logic ensures the interactive forecast map link in the report is always live and up-to-date, preventing broken links and silent failures.

### **Limitations and Scalability 📈**
* **Inherent Limitation:** The workflow relies exclusively on ocean current forecast data and cannot account for real-time pollution events or debris sources outside the oceanic model's scope.

* **Current Limitations:** The AI analysis is constrained by the length of the forecast (9 days).

* **Future Scalability:** The modular design allows for seamless upgrades. The system could be integrated with a database to log all daily forecast results for long-term trend analysis. The AI Agent could be given the ability to use external web search to contextualize its pollution impact summary (though this would sacrifice some determinism).
