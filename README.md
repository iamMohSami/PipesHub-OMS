## 📜 Problem Statement

We were asked to implement a **basic Order Management System** with the following requirements:

1. ✅ **Trading Window**

   * Orders are only accepted between **09:15 AM to 03:30 PM**.
   * Orders outside this window are rejected.

2. ✅ **Throttling**

   * Maximum **5 orders per second**.
   * Extra orders are rejected.

3. ✅ **Session Management**

   * Support for `sendLogon()` and `sendLogout()` methods.
   * Only process orders if the client is logged in.

---

## ✨ Features Implemented

### 🔹 Required Features (From Problem Statement)

* **Trading Window validation** (rejects orders outside window).
* **Order Throttling** (max 5 orders/sec).
* **Logon / Logout** flow.

### 🔹 Extra Features (Bonus / Enhancements)

* **Order Book**:

  * Stores active Buy/Sell orders.
  * Supports **New, Modify, Cancel** operations.
*  **Input Validation** (reject invalid quantity/price).
*  **Unique Order IDs** for tracking.
*  **Test Cases** for key scenarios (normal flow, throttling, window rejection, cancel/modify).

---

## 📊 System Architecture Diagram

![system architecture](image.png)

---

## 📖 Order Lifecycle (Simplified)

![alt text](image-1.png)

---

## 💡 Thought Process & Insights

* Started with **core OMS concepts** → logon/logout, trading hours, throttling.
* Gradually extended to **order lifecycle management** (new, modify, cancel).
* Kept the **Matching Engine out of scope** since it was not part of the PS.
* Designed the code with **modularity** → easy to extend later (e.g., adding matching).
* Used **only Python standard libraries** (`datetime`, `time`, `collections`).

---

## ⚙️ Implementation Details

* **OMS Class**:

  * Handles logon/logout.
  * Maintains order throttling & trading window rules.
  * Delegates order operations to the `OrderBook`.

* **OrderBook Class**:

  * Stores buy and sell orders separately.
  * Supports New / Modify / Cancel.
  * Maintains active orders in a dictionary.

* **Tests**:

  * Added to validate each core requirement.

---

## ✅ Test Results

### Case 1: Orders in trading window

```
sendLogon()
New order accepted ✅
New order accepted ✅
```

### Case 2: Orders outside trading window

```
Rejected ❌ : Outside trading hours
```

### Case 3: Throttling > 5 orders/sec

```
First 5 orders ✅ accepted
6th order ❌ rejected due to throttling
```

### Case 4: Cancel / Modify

```
Cancel ✅ successful
Modify ✅ successful
```

---

## ▶️ How to Run

### 1. Clone the repo

```bash
git clone https://github.com/iamMohSami/PipesHub-OMS.git
cd PipesHub-OMS
```

### 2. Run the OMS

```bash
python oms.py
```

### 3. Run Tests

```bash
python tests.py
```

---

## 📌 Future Enhancements

* Add **Matching Engine** (price-time priority).
* Add **Persistence** (DB or file-based storage).
* Add **REST API layer** using FastAPI/Flask.
* Add **Multi-user session handling**.

---

## 👨‍💻 Author

**Mohammad Sami**
Final Year CSE Student, IIIT Surat

