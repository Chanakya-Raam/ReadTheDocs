Vehicle Control Unit Endpoints
==============================

This section covers all operations available for Vehicle Control Units, including creating, reading, updating, deleting, and allocating individual or multiple vehicle control units.

**Table of Operations**

+--------------------+-------------------------------------------------------------+----------------------------------------+
| **Method**         | **Description**                                             | **Endpoint**                           |
+====================+=============================================================+========================================+
| POST               | Create a new vehicle control unit or bulk upload            | /vehicle_control_unit                  |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| DELETE             | Delete a group of vehicle control units                     | /vehicle_control_unit                  |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| GET                | Read the properties of a group of vehicle control units     | /vehicle_control_unit                  |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| PATCH              | Update the properties of a group of vehicle control units   | /vehicle_control_unit                  |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| DELETE             | Delete an individual vehicle control unit                   | /vehicle_control_unit/{i}              |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| GET                | Read the properties of an individual vehicle control unit   | /vehicle_control_unit/{i}              |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| PATCH              | Update the properties of an individual vehicle control unit | /vehicle_control_unit/{i}              |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| POST               | Allocate a vehicle control unit to an entity                | /vehicle_control_unit/{i}/allocate     |
+--------------------+-------------------------------------------------------------+----------------------------------------+
| POST               | Enable or disable a vehicle control unit                    | /vehicle_control_unit/{i}/enable       |
+--------------------+-------------------------------------------------------------+----------------------------------------+

---

POST /vehicle_control_unit
--------------------------

**Summary:** Create a new vehicle control unit.

- **Description:** This endpoint allows for the creation of a new vehicle control unit or bulk creation via file upload.
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
     "vehicle_control_unit": {}
   }

**Responses:**

- **201**: Vehicle control unit created successfully.

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

DELETE /vehicle_control_unit
----------------------------

**Summary:** Delete a group of vehicle control units.

- **Description:** This endpoint allows the deletion of a group of vehicle control units. Requires JWT authentication.

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

GET /vehicle_control_unit
-------------------------

**Summary:** Read the properties of a group of vehicle control units.

- **Description:** Retrieve details of multiple vehicle control units. Supports filtering, sorting, and pagination.

**Query Parameters:**

- **limit**: Maximum number of vehicle control units to return.
- **offset**: Number of vehicle control units to skip before starting to collect the result set.
- **search**: General search term.
- **sort**: Field to sort by.
- **order**: Sort order, either `asc` or `desc`.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label (e.g., Ready to Deploy, In Factory, In Warehouse, For Rework, In Vehicle).

**Responses:**

- **200**: Successfully retrieved vehicle control units.

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
         "vehicle_control_unit": {}
       }
     ]

---

PATCH /vehicle_control_unit
---------------------------

**Summary:** Update the properties of a group of vehicle control units.

- **Description:** This endpoint allows the bulk update of vehicle control unit details.
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

DELETE /vehicle_control_unit/{i}
--------------------------------

**Summary:** Delete an individual vehicle control unit.

- **Description:** This endpoint allows deletion of an individual vehicle control unit.

**Path Parameters:**

- **i**: Identifier of the individual vehicle control unit.

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

GET /vehicle_control_unit/{i}
-----------------------------

**Summary:** Read the properties of an individual vehicle control unit.

- **Description:** Retrieve details of a specific vehicle control unit.

**Path Parameters:**

- **i**: Identifier of the individual vehicle control unit.

**Responses:**

- **200**: Vehicle control unit details returned successfully.

  .. code-block:: json

     {
       "asset_tag": "IRASUS01",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "location": "Delhi"
     }

---

PATCH /vehicle_control_unit/{i}
-------------------------------

**Summary:** Update the properties of an individual vehicle control unit.

- **Description:** Modify the details of a specific vehicle control unit.

**Path Parameters:**

- **i**: Identifier of the individual vehicle control unit.

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
     "vehicle_control_unit": {}
   }

---

POST /vehicle_control_unit/{i}/allocate
---------------------------------------

**Summary:** Allocate a vehicle control unit to another entity.

- **Description:** Allocate a vehicle control unit to a different entity such as a vehicle, user, or location.

**Path Parameters:**

- **i**: Identifier of the individual vehicle control unit.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "target_category": "Vehicle",
     "target_individual": "IRASUS01",
     "status_label": "In Use"
   }

---

POST /vehicle_control_unit/{i}/enable
-------------------------------------

**Summary:** Enable or disable the vehicle control unit.

- **Description:** Enable or disable the vehicle control unit.

**Path Parameters:**

- **i**: Identifier of the individual vehicle control unit.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "active",
     "status_label": "In Use"
   }

**Responses:**

- **200**: Asset enabled or disabled successfully.

  .. code-block:: json

     {
       "issuedAt": "2024-09-04 00:00:00+05:30",
       "enabledAt": "2024-09-04 00:00:00+05:30"
     }

---
