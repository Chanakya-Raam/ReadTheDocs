Battery Pack Swapping Station Endpoints
=======================================

This section covers all operations available for Battery Pack Swapping Stations, including creating, reading, updating, deleting, allocating, and enabling/disabling battery pack swapping stations.

**Table of Operations**

+--------------------+--------------------------------------------------------------+--------------------------------------------+
| **Method**         | **Description**                                              | **Endpoint**                               |
+====================+==============================================================+============================================+
| POST               | Create a new battery pack swapping station                   | /battery_pack_swapping_station             |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| DELETE             | Delete a group of battery pack swapping stations             | /battery_pack_swapping_station             |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| GET                | Read the properties of a group of swapping stations          | /battery_pack_swapping_station             |
|                    |                                                              |                                            |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| PATCH              | Update the properties of a group of swapping stations        | /battery_pack_swapping_station             |
|                    |                                                              |                                            |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| DELETE             | Delete an individual swapping station                        | /battery_pack_swapping_station/{i}         |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| GET                | Read the properties of an individual swapping station        | /battery_pack_swapping_station/{i}         |
|                    |                                                              |                                            |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| PATCH              | Update the properties of an individual swapping station      | /battery_pack_swapping_station/{i}         |
|                    |                                                              |                                            |
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| POST               | Allocate a swapping station to another asset, user, or entity| /battery_pack_swapping_station/{i}/allocate|
+--------------------+--------------------------------------------------------------+--------------------------------------------+
| POST               | Enable or disable a swapping station                         | /battery_pack_swapping_station/{i}/enable  |
+--------------------+--------------------------------------------------------------+--------------------------------------------+

---

POST /battery_pack_swapping_station
-----------------------------------

**Summary:** Create a new battery pack swapping station.

- **Description:** This endpoint allows for the creation of a new battery pack swapping station.
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
     "battery_pack_swapping_station": {
       "podcabinet_count": "",
       "charger_rating": ""
     }
   }

**Responses:**

- **201**: Battery pack swapping station created successfully.

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

---

DELETE /battery_pack_swapping_station
-------------------------------------

**Summary:** Delete a group of battery pack swapping stations.

- **Description:** This endpoint allows the deletion of a group of battery pack swapping stations. Requires JWT authentication.

**Responses:**

- **200**: Battery pack swapping stations deleted successfully.

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

GET /battery_pack_swapping_station
----------------------------------

**Summary:** Read the properties of a group of battery pack swapping stations.

- **Description:** Retrieve details of multiple battery pack swapping stations.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **battery_pack_swapping_station**: Search term related to the station.
- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label (e.g., "In Warehouse").

**Responses:**

- **200**: Successfully retrieved battery pack swapping stations.

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
         "battery_pack_swapping_station": {
           "podcabinet_count": "",
           "charger_rating": ""
         }
       }
     ]

---

PATCH /battery_pack_swapping_station
------------------------------------

**Summary:** Update the properties of a group of battery pack swapping stations.

- **Description:** This endpoint allows the bulk update of battery pack swapping station details.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Battery pack swapping stations updated successfully.

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

DELETE /battery_pack_swapping_station/{i}
-----------------------------------------

**Summary:** Delete an individual battery pack swapping station.

- **Description:** This endpoint allows the deletion of an individual battery pack swapping station.

**Path Parameters:**

- **i**: Identifier of the individual battery pack swapping station.

**Responses:**

- **200**: Battery pack swapping station deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Asset deleted successfully",
       "deletedAt": "2024-07-30T12:34:56Z"
     }

---

GET /battery_pack_swapping_station/{i}
--------------------------------------

**Summary:** Read the properties of an individual battery pack swapping station.

- **Description:** Retrieve details of a specific battery pack swapping station.

**Path Parameters:**

- **i**: Identifier of the individual battery pack swapping station.

**Responses:**

- **200**: Battery pack swapping station details returned successfully.

  .. code-block:: json

     {
       "asset_tag": "IRASUS01",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "company": "Irasus Technologies Private Limited",
       "location": "Delhi",
       "warranty_months": "3",
       "battery_pack_swapping_station": {
         "podcabinet_count": "",
         "charger_rating": ""
       }
     }

---

PATCH /battery_pack_swapping_station/{i}
----------------------------------------

**Summary:** Update the properties of an individual battery pack swapping station.

- **Description:** Modify the details of a specific battery pack swapping station.

**Path Parameters:**

- **i**: Identifier of the individual battery pack swapping station.

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
     "battery_pack_swapping_station": {
       "podcabinet_count": "",
       "charger_rating": ""
     }
   }

**Responses:**

- **200**: Battery pack swapping station updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Asset updated successfully"
     }

---

POST /battery_pack_swapping_station/{i}/allocate
------------------------------------------------

**Summary:** Allocate an individual battery pack swapping station to another asset, a user, or a location.

- **Description:** This endpoint assigns a swapping station to another entity.

**Path Parameters:**

- **i**: Identifier of the individual battery pack swapping station.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "target_category": "Location",
     "target_individual": "Battery Pack Swapping Zone X",
     "status_label": "Available"
   }

**Responses:**

- **200**: Battery pack swapping station allocated successfully.

  .. code-block:: json

     {
       "status": "success",
       "allocatedAt": "2024-09-04 00:00:00+05:30"
     }

---

POST /battery_pack_swapping_station/{i}/enable
----------------------------------------------

**Summary:** Enable or disable an individual battery pack swapping station.

- **Description:** Enable or disable functionality for a specific swapping station.

**Path Parameters:**

- **i**: Identifier of the individual battery pack swapping station.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "charging",
     "status_label": "Available"
   }

**Responses:**

- **200**: Battery pack swapping station enabled successfully.

  .. code-block:: json

     {
       "issuedAt": "2024-09-04 00:00:00+05:30",
       "enabledAt": "2024-09-04 00:00:00+05:30"
     }
