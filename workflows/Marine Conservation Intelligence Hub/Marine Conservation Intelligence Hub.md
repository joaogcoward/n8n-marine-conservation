## *The Problem* 😫
Staying informed about environmental news is crucial for mission-driven organizations, but manually tracking multiple sources, filtering for relevance, and sharing consistent updates is time-consuming and prone to human error. This repetitive process drains valuable time that could be spent on deeper analysis and strategy.

## *The Solution* ✨
Over the course of one week, I designed and built an end-to-end automation workflow to solve this problem. Using n8n, a powerful low-code platform, I created a system that automatically:

Gathers real-time data from multiple news APIs (e.g., The Guardian API) using HTTP requests.

Cleans and processes the data, including a custom JavaScript code node to handle articles with differing data structures (e.g., from Forbes vs. Mongabay).

Removes duplicates to ensure only new, unique articles are reported.

Generates a formatted digest of articles in a single Slack message.

Handles failures gracefully, sending a separate report if no new articles are found.

The project was built with a focus on robustness, scalability, and ease of maintenance. All of the process, assumptions, and findings are being documented in Notion and GitHub 📝, and I would be happy to share the JSON automation file if required.

## *The Real Impact* 🚀
100% Automation: Eliminated manual searching, filtering, and reporting, saving significant time.

Data Integrity: The Remove Duplicates functionality ensures the team only sees fresh, non-redundant content.

Reliable Reporting: The workflow's robust error handling means there are no silent failures. The team is always informed, whether new articles are found or not.

Proof of Concept: This project is a tangible demonstration of how automation can support a core mission—in this case, empowering a team with continuous, clean, and reliable data.liable data.
