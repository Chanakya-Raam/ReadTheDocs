Energy Meter Endpoints
======================

This section covers all operations available for Energy Meters, including creating, reading, updating, deleting, allocating, and enabling or disabling individual or multiple energy meters.

**Table of Operations**

+--------------------+---------------------------------------------------+------------------------------------+
| **Method**         | **Description**                                   | **Endpoint**                       |
+====================+===================================================+====================================+
| POST               | Create a new energy meter or bulk upload          | /energy_meter                      |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete a group of energy meters                   | /energy_meter                      |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of a group of energy meters   | /energy_meter                      |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of a group of energy meters | /energy_meter                      |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete an individual energy meter                 | /energy_meter/{i}                  |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of an individual energy meter | /energy_meter/{i}                  |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of an individual energy meter | /energy_meter/{i}                |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Allocate an energy meter to an entity             | /energy_meter/{i}/allocate         |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Enable or disable an energy meter                 | /energy_meter/{i}/enable           |
+--------------------+---------------------------------------------------+------------------------------------+

---

POST /energy_meter
------------------

**Summary:** Create a new energy meter.

- **Description:** This endpoint allows for the creation of a new energy meter or bulk creation via file upload.
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
     "energy_meter": {}
   }

**Responses:**

- **201**: Energy meter created successfully.

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

- **409**: Conflict - Resource already exists.

  .. code-block:: json

     {
       "status": "error",
       "message": "Resource already exists"
     }

- **500**: Internal server error.

  .. code-block:: json

     {
       "status": "error",
       "message": "Internal server error"
     }

---

DELETE /energy_meter
--------------------

**Summary:** Delete a group of energy meters.

- **Description:** This endpoint allows the deletion of a group of energy meters. Requires JWT authentication.

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

GET /energy_meter
-----------------

**Summary:** Read the properties of a group of energy meters.

- **Description:** Retrieve details of multiple energy meters. Supports filtering, sorting, and pagination.

**Query Parameters:**

- **limit**: Maximum number of energy meters to return.
- **offset**: Number of energy meters to skip before starting to collect the result set.
- **search**: General search term.
- **sort**: Field to sort by.
- **order**: Sort order, either `asc` or `desc`.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label (e.g., Ready to Deploy, In Factory, In Warehouse, For Rework).

**Responses:**

- **200**: Successfully retrieved energy meters.

  .. code-block:: json

     [
       {
         "asset_tag": "IRASUS01",
         "status_label": "In Warehouse",
         "model": "Model X",
         "manufacturer_name": "Irasus Technologies Private Limited",
         "company": "Irasus Technologies Private Limited",
         "location": "Delhi",
         "warranty_months": "3",
         "energy_meter": {}
       }
     ]

---

PATCH /energy_meter
-------------------

**Summary:** Update the properties of a group of energy meters.

- **Description:** This endpoint allows the bulk update of energy meter details.
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

DELETE /energy_meter/{i}
------------------------

**Summary:** Delete an individual energy meter.

- **Description:** This endpoint allows deletion of an individual energy meter.

**Path Parameters:**

- **i**: Identifier of the individual energy meter.

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

GET /energy_meter/{i}
---------------------

**Summary:** Read the properties of an individual energy meter.

- **Description:** Retrieve details of a specific energy meter.

**Path Parameters:**

- **i**: Identifier of the individual energy meter.

**Responses:**

- **200**: Energy meter details returned successfully.

  .. code-block:: json

     {
       "asset_tag": "IRASUS01",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "location": "Delhi"
     }

---

PATCH /energy_meter/{i}
-----------------------

**Summary:** Update the properties of an individual energy meter.

- **Description:** Modify the details of a specific energy meter.

**Path Parameters:**

- **i**: Identifier of the individual energy meter.

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
     "energy_meter": {}
   }

---

POST /energy_meter/{i}/allocate
-------------------------------

**Summary:** Allocate an energy meter to another entity.

- **Description:** Allocate an energy meter to a different entity such as a battery pack, user, or location.

**Path Parameters:**

- **i**: Identifier of the individual energy meter.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "target_category": "Battery Pack",
     "target_individual": "IRASUS01",
     "status_label": "Available"
   }

---

POST /energy_meter/{i}/enable
-----------------------------

**Summary:** Enable or disable the energy meter.

- **Description:** Enable or disable the energy meter.

**Path Parameters:**

- **i**: Identifier of the individual energy meter.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "measuring",
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
