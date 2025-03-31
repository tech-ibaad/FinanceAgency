# 💰 Finance Tracker Agency

## Overview  
Finance Tracker Agency is an automated financial management system built using **Agency Swarm**. It consists of two AI agents:  
- **CEO Agent**: Oversees financial planning and requests reports.  
- **Tracker Agent**: Manages an SQLite database, storing and retrieving transactions.  

## 📌 Features  
✅ **Automated financial tracking** with SQLite  
✅ **Intelligent agent communication** using Agency Swarm  
✅ **Customizable agent roles and instructions**  
✅ **Multiple query options** to retrieve financial data  

## 🛠️ Installation  

### 1️⃣ Install Dependencies  
```bash
pip install agency-swarm sqlite3
2️⃣ Set Up Database
bash
Copy
Edit
python setup/setup_db.py
3️⃣ Run the Agency
bash
Copy
Edit
python AgencySetup.py
🏗️ Project Structure
arduino
Copy
Edit
FinanceTrackerAgency/
│── agents/
│   │── CEOAgent/
│   │   │── CEOAgent.py
│   │   │── instructions.md
│   │── TrackerAgent/
│   │   │── TrackerAgent.py
│   │   │── instructions.md
│── tools/
│   │── FinanceDBTool.py
│── setup/
│   │── setup_db.py
│── AgencySetup.py
│── README.md
📊 Tracker Agent Capabilities
Action	Description
add	Add a new transaction
get_all	Retrieve all transactions
get_by_category	Get transactions by category
get_by_date	Get transactions by date
sum_by_category	Calculate total expenses per category
update	Modify an existing transaction
delete	Remove a transaction
