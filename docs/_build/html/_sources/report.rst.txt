Report Endpoints
================

This section covers all report-related operations, including generating various types of reports such as energy reports, swap station logs, cycles reports, capacity retention reports, SoH reports, and vehicle speed reports.

**Table of Operations**

+------------------------+--------------------------------------------+------------------------------------+
| **Method**             | **Description**                            | **Endpoint**                       |
+========================+============================================+====================================+
| GET                    | Retrieve energy reports                    | /reports/energy                    |
+------------------------+--------------------------------------------+------------------------------------+
| GET                    | Retrieve swap station logs                 | /reports/swap_station_logs         |
+------------------------+--------------------------------------------+------------------------------------+
| GET                    | Retrieve cycles reports                    | /reports/cycles                    |
+------------------------+--------------------------------------------+------------------------------------+
| GET                    | Retrieve capacity retention reports        | /reports/capacity_retention        |
+------------------------+--------------------------------------------+------------------------------------+
| GET                    | Retrieve SoH reports                       | /reports/soh                       |
+------------------------+--------------------------------------------+------------------------------------+
| GET                    | Retrieve vehicle speed reports             | /reports/vehicle_speed             |
+------------------------+--------------------------------------------+------------------------------------+

---

GET /reports/energy
-------------------

**Summary:** Retrieve energy reports for a given date range.

- **Description:** This endpoint generates a report based on energy consumption data.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **from**: Start timestamp for the report.
- **to**: End timestamp for the report.
- **pack_number**: Battery Pack Number.

**Responses:**

- **200**: Report retrieved successfully.

  .. code-block:: text

     Content-Disposition: attachment; filename="energy_report.csv"

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /reports/swap_station_logs
------------------------------

**Summary:** Retrieve swap station logs for a given date range.

- **Description:** This endpoint generates swap station log reports within a specified date range.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **from**: Start timestamp for the report.
- **to**: End timestamp for the report.
- **i**: Unique identifier of swap station.

**Responses:**

- **200**: Report retrieved successfully.

  .. code-block:: text

     Content-Disposition: attachment; filename="swap_station_logs.csv"

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /reports/cycles
-------------------

**Summary:** Retrieve cycles reports for a given date range.

- **Description:** This endpoint generates cycles reports based on the usage of battery packs.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **from**: Start timestamp for the report.
- **to**: End timestamp for the report.
- **pack_number**: Battery Pack Number.

**Responses:**

- **200**: Report retrieved successfully.

  .. code-block:: text

     Content-Disposition: attachment; filename="cycles_report.csv"

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /reports/capacity_retention
-------------------------------

**Summary:** Retrieve capacity retention reports for a given date range.

- **Description:** This endpoint generates reports on battery capacity retention over time.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **from**: Start timestamp for the report.
- **to**: End timestamp for the report.
- **pack_number**: Battery Pack Number.

**Responses:**

- **200**: Report retrieved successfully.

  .. code-block:: text

     Content-Disposition: attachment; filename="capacity_retention_report.csv"

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /reports/soh
----------------

**Summary:** Retrieve SoH (State of Health) reports for a given date range.

- **Description:** This endpoint generates reports on the state of health of battery packs.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **from**: Start timestamp for the report.
- **to**: End timestamp for the report.
- **pack_number**: Battery Pack Number.

**Responses:**

- **200**: Report retrieved successfully.

  .. code-block:: text

     Content-Disposition: attachment; filename="soh_report.csv"

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /reports/vehicle_speed
--------------------------

**Summary:** Retrieve vehicle speed reports for a given date range.

- **Description:** This endpoint generates reports on vehicle speed data.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **from**: Start timestamp for the report.
- **to**: End timestamp for the report.
- **i**: Unique identifier of a vehicle.

**Responses:**

- **200**: Report retrieved successfully.

  .. code-block:: text

     Content-Disposition: attachment; filename="vehicle_speed_report.csv" (Downloadable)

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---
