Charger (Advanced) Endpoints
============================

This section covers all operations available for advanced chargers, including creating, reading, updating, deleting, allocating, and enabling/disabling advanced chargers, as well as starting/stopping charging transactions.

**Table of Operations**

+--------------------+---------------------------------------------------+------------------------------------+
| **Method**         | **Description**                                   | **Endpoint**                       |
+====================+===================================================+====================================+
| POST               | Create a new advanced charger                     | /charger_advanced                  |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete a group of advanced chargers               | /charger_advanced                  |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of a group of advanced        | /charger_advanced                  |
|                    | chargers                                          |                                    |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of a group of advanced      | /charger_advanced                  |
|                    | chargers                                          |                                    |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete an individual advanced charger             | /charger_advanced/{i}              |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of an individual advanced     | /charger_advanced/{i}              |
|                    | charger                                           |                                    |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of an individual advanced   | /charger_advanced/{i}              |
|                    | charger                                           |                                    |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Allocate an advanced charger to another asset,    | /charger_advanced/{i}/allocate     |
|                    | user, or location                                 |                                    |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Enable or disable an advanced charger             | /charger_advanced/{i}/enable       |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Start a charging transaction on an advanced       | /charger_advanced/{i}/start        |
|                    | charger                                           |                                    |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Stop a charging transaction on an advanced        | /charger_advanced/{i}/stop         |
|                    | charger                                           |                                    |
+--------------------+---------------------------------------------------+------------------------------------+

---

POST /charger_advanced
----------------------

**Summary:** Create a new advanced charger.

- **Description:** This endpoint allows for the creation of a new advanced charger.
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
     "charger_advanced": {}
   }

**Responses:**

- **201**: Advanced charger created successfully.

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

---

DELETE /charger_advanced
------------------------

**Summary:** Delete a group of advanced chargers.

- **Description:** This endpoint allows the deletion of a group of advanced chargers. Requires JWT authentication.

**Responses:**

- **200**: Advanced chargers deleted successfully.

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

---

GET /charger_advanced
---------------------

**Summary:** Read the properties of a group of advanced chargers.

- **Description:** Retrieve details of multiple advanced chargers.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **charger_advanced**: Search term related to the charger.
- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label (e.g., "In Warehouse").

**Responses:**

- **200**: Successfully retrieved advanced chargers.

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
         "charger_advanced": {}
       }
     ]

---

PATCH /charger_advanced
-----------------------

**Summary:** Update the properties of a group of advanced chargers.

- **Description:** This endpoint allows the bulk update of advanced charger details.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Advanced chargers updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Assets updated successfully",
       "updatedAt": "2024-07-30T12:34:56Z"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

DELETE /charger_advanced/{i}
----------------------------

**Summary:** Delete an individual advanced charger.

- **Description:** This endpoint allows the deletion of an individual advanced charger.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

**Responses:**

- **200**: Advanced charger deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Asset deleted successfully",
       "deletedAt": "2024-07-30T12:34:56Z"
     }

---

GET /charger_advanced/{i}
-------------------------

**Summary:** Read the properties of an individual advanced charger.

- **Description:** Retrieve details of a specific advanced charger.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

**Responses:**

- **200**: Advanced charger details returned successfully.

  .. code-block:: json

     {
       "asset_tag": "IRASUS01",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "company": "Irasus Technologies Private Limited",
       "location": "Delhi",
       "warranty_months": "3",
       "charger_advanced": {}
     }

---

PATCH /charger_advanced/{i}
---------------------------

**Summary:** Update the properties of an individual advanced charger.

- **Description:** Modify the details of a specific advanced charger.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

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
     "charger_advanced": {}
   }

**Responses:**

- **200**: Advanced charger updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Assets updated successfully"
     }

---

POST /charger_advanced/{i}/allocate
-----------------------------------

**Summary:** Allocate an individual advanced charger to another asset, user, or location.

- **Description:** This endpoint assigns an advanced charger to another entity.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "target_category": "Location",
     "target_individual": "Electric Vehicle Battery Charging Station X",
     "status_label": "Available"
   }

**Responses:**

- **200**: Advanced charger allocated successfully.

  .. code-block:: json

     {
       "status": "success",
       "allocatedAt": "2024-09-04 00:00:00+05:30"
     }

---

POST /charger_advanced/{i}/enable
---------------------------------

**Summary:** Enable or disable an individual advanced charger.

- **Description:** Enable or disable functionality for a specific advanced charger.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "charging",
     "status_label": "Available"
   }

**Responses:**

- **200**: Advanced charger enabled successfully.

  .. code-block:: json

     {
       "issuedAt": "2024-09-04 00:00:00+05:30",
       "enabledAt": "2024-09-04 00:00:00+05:30"
     }

---

POST /charger_advanced/{i}/start
--------------------------------

**Summary:** Start a charging transaction on an advanced charger.

- **Description:** Start charging a battery using a specific advanced charger.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

**Request Body (JSON Example):**

.. code-block:: json

   {}

**Responses:**

- **200**: Charging transaction started successfully.

---

POST /charger_advanced/{i}/stop
-------------------------------

**Summary:** Stop a charging transaction on an advanced charger.

- **Description:** Stop charging a battery using a specific advanced charger.

**Path Parameters:**

- **i**: Identifier of the individual advanced charger.

**Request Body (JSON Example):**

.. code-block:: json

   {}

**Responses:**

- **200**: Charging transaction stopped successfully.

