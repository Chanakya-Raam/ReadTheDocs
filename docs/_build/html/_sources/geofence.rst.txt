Geofence Endpoints
==================

This section covers all operations available for Geofences, including creating, reading, updating, deleting, allocating, and listing vehicles within geofences.

**Table of Operations**

+--------------------+---------------------------------------------------+------------------------------------+
| **Method**         | **Description**                                   | **Endpoint**                       |
+====================+===================================================+====================================+
| POST               | Create a new geofence                             | /geofence                          |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete a set of geofences                         | /geofence                          |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of a set of geofences         | /geofence                          |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of a set of geofences       | /geofence                          |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete an individual geofence                     | /geofence/{i}                      |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of an individual geofence     | /geofence/{i}                      |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of an individual geofence   | /geofence/{i}                      |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Assign a vehicle to a specific geofence           | /geofence/{i}/allocate             |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | List all vehicles for a geofence                  | /geofence/{i}/vehicles             |
+--------------------+---------------------------------------------------+------------------------------------+

---

POST /geofence
--------------

**Summary:** Create a new geofence.

- **Description:** This endpoint allows for the creation of a new geofence.
- **Security:** Requires JWT authentication.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "name": "Connaught Place in Delhi, DL, India",
     "area": {
       "name": "circle",
       "center": {
         "lat": 28.6328035,
         "lng": 77.2196819
       },
       "coordinates": {
         "center": {
           "lat": 28.6328035,
           "lng": 77.2196819
         },
         "radius": 333
       }
     }
   }

**Responses:**

- **201**: Geofence created successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Geofence created successfully",
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

- **500**: Internal server error.

  .. code-block:: json

     {
       "status": "error",
       "message": "Request timed out"
     }

---

DELETE /geofence
----------------

**Summary:** Delete a set of geofences.

- **Description:** This endpoint allows the deletion of a set of geofences. Requires JWT authentication.

**Responses:**

- **200**: Geofences deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Geofences deleted successfully",
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
       "message": "Request timed out"
     }

---

GET /geofence
-------------

**Summary:** Read the properties of a set of geofences.

- **Description:** Retrieve details of multiple geofences.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **geofence**: Search term related to the geofence.

**Responses:**

- **200**: Successfully retrieved geofences.

  .. code-block:: json

     {
       "name": "Connaught Place in Delhi, DL, India",
       "area": {
         "name": "circle",
         "center": {
           "lat": 28.6328035,
           "lng": 77.2196819
         },
         "coordinates": {
           "center": {
             "lat": 28.6328035,
             "lng": 77.2196819
           },
           "radius": 333
         }
       },
       "createdAt": "2024-09-04 00:00:00+05:30",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

---

PATCH /geofence
---------------

**Summary:** Update the properties of a set of geofences.

- **Description:** This endpoint allows the bulk update of geofence details.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Geofences updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Geofences updated successfully",
       "updatedAt": "2024-07-30T12:34:56Z"
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

DELETE /geofence/{i}
--------------------

**Summary:** Delete an individual geofence.

- **Description:** This endpoint allows the deletion of an individual geofence.

**Path Parameters:**

- **i**: Identifier of the individual geofence.

**Responses:**

- **200**: Geofence deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Geofence deleted successfully",
       "deletedAt": "2024-07-30T12:34:56Z"
     }

---

GET /geofence/{i}
-----------------

**Summary:** Read the properties of an individual geofence.

- **Description:** Retrieve details of a specific geofence.

**Path Parameters:**

- **i**: Identifier of the individual geofence.

**Responses:**

- **200**: Geofence details returned successfully.

  .. code-block:: json

     {
       "name": "Connaught Place in Delhi, DL, India",
       "area": {
         "name": "circle",
         "center": {
           "lat": 28.6328035,
           "lng": 77.2196819
         },
         "coordinates": {
           "center": {
             "lat": 28.6328035,
             "lng": 77.2196819
           },
           "radius": 333
         }
       },
       "createdAt": "2024-09-04 00:00:00+05:30",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

---

PATCH /geofence/{i}
-------------------

**Summary:** Update the properties of an individual geofence.

- **Description:** Modify the details of a specific geofence.

**Path Parameters:**

- **i**: Identifier of the individual geofence.

**Responses:**

- **200**: Geofence updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Geofence updated successfully",
       "updatedAt": "2024-07-30T12:34:56Z"
     }

---

POST /geofence/{i}/allocate
---------------------------

**Summary:** Assign a vehicle to a specific geofence.

- **Description:** This endpoint assigns a vehicle to a specific geofence.

**Path Parameters:**

- **i**: Identifier of the individual geofence.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "name": "Connaught Place in Delhi, DL, India",
     "area": {
       "name": "circle",
       "center": {
         "lat": 28.6328035,
         "lng": 77.2196819
       },
       "coordinates": {
         "center": {
           "lat": 28.6328035,
           "lng": 77.2196819
         },
         "radius": 333
       }
     }
   }

**Responses:**

- **201**: Vehicle assigned to geofence successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Geofence allocated successfully",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

---

GET /geofence/{i}/vehicles
--------------------------

**Summary:** List all vehicles assigned to a geofence.

- **Description:** Retrieve all vehicles allocated to a specific geofence.

**Path Parameters:**

- **i**: Identifier of the individual geofence.

**Responses:**

- **200**: Successfully retrieved vehicles.

  .. code-block:: json

     {
       "status": "success",
       "vehicles": [
         {
           "asset_tag": "IRASUS01"
         }
       ]
     }

---

