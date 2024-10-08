Position Tracker (Advanced) Endpoints
=====================================

This section covers all operations available for Position Trackers (Advanced), including creating, reading, updating, deleting, and allocating individual or multiple advanced position trackers.

**Table of Operations**

+--------------------+-----------------------------------------------------------+------------------------------------------+
| **Method**         | **Description**                                           | **Endpoint**                             |
+====================+===========================================================+==========================================+
| POST               | Create a new position tracker (advanced) or bulk upload   | /position_tracker_advanced               |
|                    |                                                           |                                          |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| DELETE             | Delete a group of position trackers (advanced)            | /position_tracker_advanced               |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| GET                | Read the properties of a group of trackers (advanced)     | /position_tracker_advanced               |
|                    |                                                           |                                          |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| PATCH              | Update the properties of a group of trackers (advanced)   | /position_tracker_advanced               |
|                    |                                                           |                                          |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| DELETE             | Delete an individual tracker (advanced)                   | /position_tracker_advanced/{i}           |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| GET                | Read the properties of an individual tracker (advanced)   | /position_tracker_advanced/{i}           |
|                    |                                                           |                                          |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| PATCH              | Update the properties of an individual tracker (advanced) | /position_tracker_advanced/{i}           |
|                    |                                                           |                                          |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| POST               | Allocate a tracker (advanced) to an entity                | /position_tracker_advanced/{i}/allocate  |
+--------------------+-----------------------------------------------------------+------------------------------------------+
| POST               | Enable or disable a tracker (advanced)                    | /position_tracker_advanced/{i}/enable    |
+--------------------+-----------------------------------------------------------+------------------------------------------+

---

POST /position_tracker_advanced
-------------------------------

**Summary:** Create a new position tracker (advanced).

- **Description:** This endpoint allows for the creation of a new position tracker (advanced) or bulk creation via file upload.
- **Security:** Requires JWT authentication.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "asset_tag": "IRASUS01",
     "status_label": "In Warehouse",
     "model": "Model X",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "company": "Irasus Technologies Private Limited",
     "location": "Delhi",
     "warranty_months": "3",
     "position_tracker_advanced": {
         "imei": "",
         "position_tracker_hardware_version": ""
     }
   }

**Responses:**

- **201**: Position tracker created successfully.

  .. code-block:: json

     {
       "createdAt": "2024-09-04 00:00:00+05:30"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

- **401**: Unauthorized access.

  .. code-block:: json

     {
       "status": "error",
       "message": "Unauthorized access"
     }

- **403**: Access forbidden.

  .. code-block:: json

     {
       "status": "error",
       "message": "Access forbidden"
     }

- **404**: Resource not found.

  .. code-block:: json

     {
       "status": "error",
       "message": "Resource not found"
     }

- **500**: Internal server error.

  .. code-block:: json

     {
       "status": "error",
       "message": "Internal server error"
     }

---

DELETE /position_tracker_advanced
---------------------------------

**Summary:** Delete a group of position trackers (advanced).

- **Description:** This endpoint allows the deletion of a group of position trackers (advanced). Requires JWT authentication.

**Responses:**

- **200**: Successfully deleted.

  .. code-block:: json

     {
       "status": "success",
       "message": "Assets deleted successfully",
       "deletedAt": "2024-07-30T12:34:56Z"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

- **401**: Unauthorized access.

  .. code-block:: json

     {
       "status": "error",
       "message": "Unauthorized access"
     }

- **500**: Internal server error.

  .. code-block:: json

     {
       "status": "error",
       "message": "Internal server error"
     }

---

GET /position_tracker_advanced
------------------------------

**Summary:** Read the properties of a group of position trackers (advanced).

- **Description:** Retrieve details of multiple position trackers (advanced). Supports filtering, sorting, and pagination.

**Query Parameters:**

- **limit**: Maximum number of position trackers to return.
- **offset**: Number of position trackers to skip before starting to collect the result set.
- **search**: General search term.
- **sort**: Field to sort by.
- **order**: Sort order, either `asc` or `desc`.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label.

**Responses:**

- **200**: Successfully retrieved position trackers.

  .. code-block:: json

     [
       {
         "asset_tag": "IRASUS01",
         "company": "Irasus Technologies Private Limited",
         "status_label": "In Warehouse",
         "model": "Model X",
         "manufacturer_name": "Irasus Technologies Private Limited",
         "location": "Delhi"
       }
     ]

---

PATCH /position_tracker_advanced
--------------------------------

**Summary:** Update the properties of a group of position trackers (advanced).

- **Description:** This endpoint allows the bulk update of position tracker (advanced) details.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Assets updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Assets updated successfully"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

- **401**: Unauthorized access.

  .. code-block:: json

     {
       "status": "error",
       "message": "Unauthorized access"
     }

---

DELETE /position_tracker_advanced/{i}
-------------------------------------

**Summary:** Delete an individual position tracker (advanced).

- **Description:** This endpoint allows deletion of an individual position tracker (advanced).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Responses:**

- **200**: Asset deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Asset deleted successfully",
       "deletedAt": "2024-07-30T12:34:56Z",
       "asset_tag": "IRASUS01"
     }

---

GET /position_tracker_advanced/{i}
----------------------------------

**Summary:** Read the properties of an individual position tracker (advanced).

- **Description:** Retrieve details of a specific position tracker (advanced).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Responses:**

- **200**: Position tracker details returned successfully.

  .. code-block:: json

     {
       "asset_tag": "IRASUS01",
       "company": "Irasus Technologies Private Limited",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "location": "Delhi"
     }

---

PATCH /position_tracker_advanced/{i}
------------------------------------

**Summary:** Update the properties of an individual position tracker (advanced).

- **Description:** Modify the details of a specific position tracker (advanced).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "asset_tag": "IRASUS01",
     "status_label": "In Warehouse",
     "model": "Model X",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "company": "Irasus Technologies Private Limited",
     "location": "Delhi",
     "warranty_months": "3",
     "position_tracker_advanced": {
       "imei": "",
       "position_tracker_hardware_version": ""
     }
   }

---

POST /position_tracker_advanced/{i}/allocate
--------------------------------------------

**Summary:** Allocate a position tracker (advanced) to another entity.

- **Description:** Allocate a position tracker (advanced) to a different entity such as a vehicle, user, or location.

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "target_category": "Vehicle",
     "target_individual": "IRASUS01",
     "status_label": "In Use"
   }

---

POST /position_tracker_advanced/{i}/enable
------------------------------------------

**Summary:** Enable or disable the position tracker (advanced).

- **Description:** Enable or disable the position tracker (advanced).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "tracking",
     "status_label": "In Warehouse"
   }

**Responses:**

- **200**: Asset enabled or disabled successfully.

  .. code-block:: json

     {
       "issuedAt": "2024-09-04 00:00:00+05:30",
       "enabledAt": "2024-09-04 00:00:00+05:30"
     }

---

