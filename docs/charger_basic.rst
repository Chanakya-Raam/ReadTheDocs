Charger (Basic) Endpoints
=========================

This section covers all operations available for basic chargers, including creating, reading, updating, deleting, allocating, and enabling/disabling basic chargers.

**Table of Operations**

+--------------------+--------------------------------------------------------------+------------------------------------------+
| **Method**         | **Description**                                              | **Endpoint**                             |
+====================+==============================================================+==========================================+
| POST               | Create a new basic charger                                   | /charger_basic                           |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| DELETE             | Delete a group of basic chargers                             | /charger_basic                           |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| GET                | Read the properties of a group of basic chargers             | /charger_basic                           |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| PATCH              | Update the properties of a group of basic chargers           | /charger_basic                           |
|                    |                                                              |                                          |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| DELETE             | Delete an individual basic charger                           | /charger_basic/{i}                       |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| GET                | Read the properties of an individual basic charger           | /charger_basic/{i}                       |
|                    |                                                              |                                          |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| PATCH              | Update the properties of an individual basic charger         | /charger_basic/{i}                       |
|                    |                                                              |                                          |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| POST               | Allocate a basic charger to another asset, user, or location | /charger_basic/{i}/allocate              |
+--------------------+--------------------------------------------------------------+------------------------------------------+
| POST               | Enable or disable a basic charger                            | /charger_basic/{i}/enable                |
+--------------------+--------------------------------------------------------------+------------------------------------------+

---

POST /charger_basic
-------------------

**Summary:** Create a new basic charger.

- **Description:** This endpoint allows for the creation of a new basic charger.
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
     "charger_basic": {}
   }

**Responses:**

- **201**: Basic charger created successfully.

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

DELETE /charger_basic
---------------------

**Summary:** Delete a group of basic chargers.

- **Description:** This endpoint allows the deletion of a group of basic chargers. Requires JWT authentication.

**Responses:**

- **200**: Basic chargers deleted successfully.

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

GET /charger_basic
------------------

**Summary:** Read the properties of a group of basic chargers.

- **Description:** Retrieve details of multiple basic chargers.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **charger_basic**: Search term related to the charger.
- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label (e.g., "In Warehouse").

**Responses:**

- **200**: Successfully retrieved basic chargers.

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
         "charger_basic": {}
       }
     ]

---

PATCH /charger_basic
--------------------

**Summary:** Update the properties of a group of basic chargers.

- **Description:** This endpoint allows the bulk update of basic charger details.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Basic chargers updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Assets updated successfully",
       "updatedAt": "2024-07-30T12:34:56Z"
     }

---

DELETE /charger_basic/{i}
-------------------------

**Summary:** Delete an individual basic charger.

- **Description:** This endpoint allows the deletion of an individual basic charger.

**Path Parameters:**

- **i**: Identifier of the individual basic charger.

**Responses:**

- **200**: Basic charger deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Asset deleted successfully",
       "deletedAt": "2024-07-30T12:34:56Z"
     }

---

GET /charger_basic/{i}
----------------------

**Summary:** Read the properties of an individual basic charger.

- **Description:** Retrieve details of a specific basic charger.

**Path Parameters:**

- **i**: Identifier of the individual basic charger.

**Responses:**

- **200**: Basic charger details returned successfully.

  .. code-block:: json

     {
       "asset_tag": "IRASUS01",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "company": "Irasus Technologies Private Limited",
       "location": "Delhi",
       "warranty_months": "3",
       "charger_basic": {}
     }

---

PATCH /charger_basic/{i}
------------------------

**Summary:** Update the properties of an individual basic charger.

- **Description:** Modify the details of a specific basic charger.

**Path Parameters:**

- **i**: Identifier of the individual basic charger.

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
     "charger_basic": {}
   }

**Responses:**

- **200**: Basic charger updated successfully.

---

POST /charger_basic/{i}/allocate
--------------------------------

**Summary:** Allocate an individual basic charger to another asset, user, or location.

- **Description:** This endpoint assigns a basic charger to another entity.

**Path Parameters:**

- **i**: Identifier of the individual basic charger.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "target_category": "Battery Pack",
     "target_individual": "IRASUS01",
     "status_label": "In Garage"
   }

**Responses:**

- **200**: Basic charger allocated successfully.

  .. code-block:: json

     {
       "status": "success",
       "allocatedAt": "2024-09-04 00:00:00+05:30"
     }

---

POST /charger_basic/{i}/enable
------------------------------

**Summary:** Enable or disable an individual basic charger.

- **Description:** Enable or disable functionality for a specific basic charger.

**Path Parameters:**

- **i**: Identifier of the individual basic charger.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "charging",
     "status_label": "In Garage"
   }

**Responses:**

- **200**: Basic charger enabled successfully.

  .. code-block:: json

     {
       "issuedAt": "2024-09-04 00:00:00+05:30",
       "enabledAt": "2024-09-04 00:00:00+05:30"
     }
