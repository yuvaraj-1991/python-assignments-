# Every morning your team asks:To check on which servers are healthy to check that I am writing a python program

# Write a Python tool that gives me a health report

Server Health Monitoring Tool

You are given a list of servers.

Each server has information like:

Hostname
IP Address
Environment
Status
CPU Usage
Memory Usage
Disk Usage

Your application should analyze this information and produce a health report.

Rules

🟢 Healthy
------------
CPU < 70%
Memory < 80%
Disk < 75%
Status = Running

🟡 Warning
------------
CPU 70–89%
OR Memory 80–89%
OR Disk 75–89%
Status = Running

🔴 Critical
------------
CPU >= 90%
OR Memory >= 90%
OR Disk >= 90%
OR Status != Running