# ☁️ Cloud Automation Scripting Tool

> Automate AWS EC2 operations using Python, Boto3, Bash scripting, and cron jobs.

---

## 📌 Project Overview

This tool automates AWS EC2 instance management — provisioning, monitoring, logging, and S3 archival — with scheduled execution via cron jobs and full version control through Git & GitHub.

---

## ✨ Features

- **Create EC2 Instances** — Launch instances with pre-configured AMI, type, and key pair
- **List EC2 Instances** — View all instances and their current state
- **Start / Stop EC2 Instances** — Selectively toggle instance state via terminal menu
- **Automated Logging** — All operations logged to `logs/cloudops.log`
- **S3 Log Archival** — Logs automatically uploaded to an S3 bucket
- **Scheduled Monitoring** — Cron job runs `scheduled_task.py` every 2 minutes
- **Version Control** — Full project history maintained with Git & GitHub

---

## 🛠️ Technologies Used

| Category        | Tools                 |
|-----------------|-----------------------|
| Language        | Python 3              |
| Cloud SDK       | Boto3, AWS CLI        |
| Scripting       | Bash                  |
| Cloud Services  | Amazon EC2, Amazon S3 |
| Scheduling      | Cron jobs             |
| Version Control | Git & GitHub          |

---

## 📁 Project Structure

```
cloud_automation_scripting_tool/
├── README.md
├── requirements.txt
├── run_scheduler.sh
├── logs/
│   ├── cloudops.log
│   └── cron.log
├── screenshots/
└── scripts/
    ├── config.py
    ├── logger.py
    ├── create_ec2.py
    ├── list_ec2.py
    ├── toggle_ec2.py
    ├── upload_logs.py
    ├── scheduled_task.py
    └── main.py
```

---

## ⚙️ Setup Instructions

### 1. Install Required Packages

```bash
sudo apt update
sudo apt install python3-pip python3-venv awscli -y
```

### 2. Clone & Set Up Virtual Environment

```bash
git clone YOUR_REPOSITORY_URL
cd cloud_automation_scripting_tool
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Configure AWS CLI

```bash
aws configure
```

Provide:
- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g. `eu-north-1`)
- Output format: `json`

Verify:

```bash
aws sts get-caller-identity
```

### 4. Run the Tool

```bash
python3 scripts/main.py
```

Menu options:
1. Create EC2 instance
2. List EC2 instances
3. Toggle EC2 state (start/stop)
4. Exit

---

## 📋 Logging & S3 Upload

- All operations are logged to `logs/cloudops.log`
- Logs are automatically uploaded to the S3 bucket configured in `scripts/config.py`
- Cron output is captured in `logs/cron.log`

---

## ⏱️ Cron Job Automation

The `run_scheduler.sh` script triggers `scheduled_task.py` on a schedule.

To set up (runs every 2 minutes):

```bash
crontab -e
```

Add:

```
*/2 * * * * /bin/bash /home/ivan/cloud_automation_scripting_tool/run_scheduler.sh >> /home/ivan/cloud_automation_scripting_tool/logs/cron.log 2>&1
```

Verify:

```bash
crontab -l
```

---

## 🔄 Workflow

```
cron job
   ↓
run_scheduler.sh
   ↓
scheduled_task.py
   ↓
EC2 state monitoring
   ↓
logging (cloudops.log)
   ↓
S3 upload
```

---

## 📦 Deliverables

- [x] Source code (scripts folder)
- [x] GitHub repository
- [x] Usage documentation (this README)
- [x] Example log output (`cloudops.log`)
- [x] S3 log archival proof (screenshot)
- [x] Cron scheduling proof (`crontab -l` screenshot)

---

## 🖼️ Screenshots

| # | Description |
|---|-------------|
| 1 | Project folder structure |
| 2 | EC2 instance creation |
| 3 | EC2 instance listing |
| 4 | Toggle operation (start/stop) |
| 5 | `cloudops.log` output |
| 6 | S3 bucket with uploaded logs |
| 7 | `crontab -l` output |
| 8 | GitHub repository view |

---

## 💬 Viva Summary

> "This project automates AWS EC2 operations using Python and Boto3. It supports EC2 provisioning, instance management, automated logging, scheduled monitoring via cron jobs, and log archival to Amazon S3."
