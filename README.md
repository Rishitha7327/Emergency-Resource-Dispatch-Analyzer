# Emergency Resource Dispatch Analyzer 🚑

## 📌 Project Overview

This project is developed as part of the **Python: Code2Xplore - 60 Days Challenge (Day-5)** at **SRM University–AP**.

The program analyzes emergency resource requests received from different zones during a disaster drill. Since the data may contain invalid or unrealistic values, the system processes and filters the requests to generate a final dispatch report.

---

## 🎯 Objective

* Process a list of resource requests
* Categorize each request based on demand level
* Apply a **Personalized Logic Identifier (PLI)** rule
* Generate a final filtered dispatch report

---

## ⚙️ Classification Rules

Each request is classified as:

* `< 0` → Invalid Request
* `0` → No Demand
* `1 – 20` → Low Demand
* `21 – 50` → Moderate Demand
* `> 50` → High Demand

---

## 🔍 Personalization Logic (PLI)

* **L** = Length of full name (excluding spaces)
* **PLI = L % 3**

### Applied Rule:

* **PLI = 0 → Rule A**

  * Remove all Low Demand requests

* **PLI = 1 → Rule B**

  * Remove all High Demand requests

* **PLI = 2 → Rule C**

  * Keep only Moderate Demand requests

---

## 👤 My Personalization Details

* **Name:** Madireddy Rishitha
* **L value:** 19
* **PLI value:** 1
* **Applied Rule:** Rule B (Removed High Demand Requests)

---

## 📥 Example Input

```
[10, 25, 60, -3, 0, 45, 80]
```

---

## 📤 Output Description

The program generates:

* Categorized lists:

  * Low Demand
  * Moderate Demand
  * High Demand
  * Invalid Requests
* Total valid requests count
* Number of requests removed due to PLI
* Final filtered dispatch report

---

## 🛠️ Technologies Used

* Python (Basic concepts)

  * Lists
  * For loops
  * Conditional statements

---

## 🚫 Constraints Followed

* No list comprehension used
* No dictionaries or sets used
* No built-in functions like `max()`, `min()`, `sum()`
* No sorting functions used

---

## 📊 Learning Outcomes

* Understanding of data classification using loops
* Applying personalized logic in programs
* Handling invalid and edge case inputs
* Writing structured and constraint-based Python code

---

## 📁 Repository Structure

```
├── main.py
├── README.md
```

---

## ✅ Conclusion

This project demonstrates how raw emergency data can be processed and filtered efficiently using basic Python concepts and personalized logic rules.

---
