### **The Problem 🚧**
Manually tracking vessel movements in marine conservation areas is crucial for mission-driven organizations like ReShark & RARCC. Inspired by the article [Can we undo extinction? A growing effort to restore lost sharks](https://news.mongabay.com/short-article/2025/08/can-we-undo-extinction-a-growing-effort-to-restore-lost-sharks/), this project tackles the time-consuming and inefficient process of manually tracking multiple AIS signals, analyzing vessel details, assessing potential risks to local marine life, and generating reports. This drains valuable time that could be spent on fieldwork and strategy.

### **The Solution ✨**
Over the course of this project, I designed and built an end-to-end automation workflow to solve this problem. Using n8n, a powerful low-code platform, I created a system that automatically:

* **Receives real-time vessel data** from an AIS stream via a webhook.

* **Analyzes the vessel's details, location, and potential risk** using a Google Vertex AI agent with specialized tools for vessel lookup and Google Search.

* **Removes duplicates** based on a unique vessel ID (MMSI) to ensure only new, unique alerts are reported.

* **Processes the AI's output** with a custom JavaScript Function node, creating a beautifully formatted email and a robust Block Kit message for Slack.

The project was built with a focus on robustness, scalability, and ease of maintenance. All of the process, assumptions, and findings are being documented in Notion and GitHub 📝, and I would be happy to share the JSON automation file if required.

### **The Real Impact 🚀**
* **100% Automation:** Eliminated the need for manual vessel tracking and reporting, saving significant time for the conservation team.

* **Data Integrity:** The "Remove Duplicates" functionality ensures the team only sees fresh, non-redundant vessel alerts.

* **Reliable Reporting:** The workflow’s robust error handling means there are no silent failures. The team is always informed of vessel activity.

* **Proof of Concept:** This project is a tangible demonstration of how automation can support a core mission—in this case, empowering a conservation team with continuous, clean, and reliable data for monitoring and intervention.

### **Limitations and Scalability 📈**
While effective for its current scope, this workflow can be built upon to handle enterprise-level needs.

* **Inherent Limitation:** The workflow cannot detect vessels that are not streaming AIS data, such as those engaged in illegal activities

* **Current Limitations:** The workflow relies on a Python script to be running to provide the AIS data stream, which introduces a point of failure. It is also limited to one data source.

* **Future Scalability:** The modular design allows for seamless upgrades. To scale, the workflow could be integrated with a database (e.g., PostgreSQL) to log all vessel detections for long-term analysis. Google Vertex AI could be further leveraged to dynamically normalize new data sources, removing the need for manual code updates. This architecture provides a solid foundation for a more comprehensive and robust data pipeline.
