# 🛡️ Nmap GUI Tool – Network Scanning Made Easy

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)  
[![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)](https://docs.python.org/3/library/tkinter.html)  
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  

**Nmap GUI Tool** is a simple Python GUI application to automate **Nmap scans**.  
Perform TCP SYN ACK scans, UDP scans, or comprehensive scans easily and view results in a user-friendly interface.

---

## ✨ Features

- 🖥️ **Graphical User Interface**  
  - Built with **Tkinter**  
  - Input IP addresses and select scan type via dropdown  

- 📡 **Scan Types**  
  - **SYN ACK Scan (TCP)**  
  - **UDP Scan**  
  - **Comprehensive Scan** (TCP + Version detection + OS detection)  

- 📊 **Scan Results**  
  - Shows host status (up/down)  
  - Lists all protocols in use  
  - Displays open ports in a scrollable text box  

- ⚠️ **Error Handling**  
  - Gracefully handles missing Nmap or invalid IP addresses  

---

## 🛠️ Tech Stack

- **Language**: Python 3.x  
- **GUI Framework**: Tkinter  
- **Nmap Wrapper**: python-nmap  
- **Network Scanning Tool**: [Nmap](https://nmap.org/)  

---

## 📂 Project Structure

``` 
nmap_gui_tool/
├─ nmap_gui.py # Main GUI application
├─ README.md # Project documentation
├─ LICENSE # MIT License
```


---

## ⚙️ Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YourUsername/nmap_gui_tool.git
cd nmap_gui_tool
pip install python-nmap
```
### 2. Install Nmap
- Download Nmap from https://nmap.org/download.html

- Make sure nmap.exe (Windows) or nmap (Linux/Mac) is in your system PATH

### Run the GUI
``` python main.py ```

- Enter the IP address to scan

- Select a scan type

- Click Run Scan

- View results in the scrollable text area
