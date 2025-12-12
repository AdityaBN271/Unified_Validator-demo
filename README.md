🚀 Unified XML Validator Tool (Portfolio Demo)

⚠️ Note regarding this repository:
The source code provided here is a sanitized demonstration version of a production tool I built for a client.
Due to Non-Disclosure Agreements (NDAs) and data privacy regulations, the proprietary logic and specific client data have been removed. This repository reconstructs the UI and architecture to demonstrate the solution's capabilities.

📊 The Results

I built the production version of this tool for a data processing firm to automate their quality assurance workflow.

Impact: Reduced data validation time by 90%.

Time Saved: Process reduced from 4 hours of manual checking to < 5 minutes of automated processing.

Reliability: Eliminated human error in checking complex XML/FNT tags.

🖼️ Application Preview

(The interface allows non-technical staff to load folders, run validation logic, and view logs in real-time without using the command line.)

🛠️ Technical Implementation

This tool was designed to be a standalone desktop application that runs on Windows machines without requiring a Python installation.

GUI Framework: Built with Tkinter for a native Windows look and feel.

Multithreading: Implements threading to ensure the UI remains responsive while processing heavy datasets in the background.

Data Logic: Uses lxml and pandas (in the full version) for high-speed XML parsing and error reporting.

Deployment: Compiled using PyInstaller into a single .exe file for easy distribution to the client's team.

💻 How to Run This Demo

You can run this demo script to see the UI and simulated validation process in action.

Clone the repository

git clone [https://github.com/AdityaBN271/Unified_Validator-demo.git](https://github.com/AdityaBN271/Unified_Validator-demo.git)
cd Unified_Validator-demo


<img width="750" height="601" alt="Screenshot 2025-12-12 123855" src="https://github.com/user-attachments/assets/45b04f1f-a414-4830-a510-f79c6e4d5cff" />




Run the application

python main.py


📬 Hire Me for Automation

I specialize in building custom scripts and desktop tools that save businesses time.
If you have a repetitive process involving Excel, XML, PDFs, or Web Scraping, I can automate it.

Email: adityabn2004@gmail.com
