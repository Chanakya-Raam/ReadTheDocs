Location Endpoints
==================

This section covers all operations available for locations, including creating, reading, updating, and deleting locations.

**Table of Operations**

+--------------------+---------------------------------------------------+------------------------------------+
| **Method**         | **Description**                                   | **Endpoint**                       |
+====================+===================================================+====================================+
| POST               | Create a new location                             | /location                          |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of a group of locations       | /location                          |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of a group of locations     | /location                          |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete a group of locations                       | /location                          |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of an individual location     | /location/{i}                      |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete an individual location                     | /location/{i}                      |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of an individual location   | /location/{i}                      |
+--------------------+---------------------------------------------------+------------------------------------+

---

POST /location
--------------

**Summary:** Create a new location.

- **Description:** This endpoint allows the creation of a new location.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **search**: Search string.
- **sort**: Field to sort results by.
- **order**: Sort order (ascending or descending).
- **city**: Filter by city.
- **state**: Filter by state.
- **country**: Filter by country.

**Request Body (Example):**

.. code-block:: json

   {
     "name": "Main Warehouse",
     "city": "San Francisco",
     "state": "CA",
     "country": "USA",
     "address": "123 Main St",
     "zip": "94105",
     "latitude": 37.7749,
     "longitude": -122.4194
   }

**Responses:**

- **201**: Location created successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Location created successfully",
       "createdAt": "2024-09-04 00:00:00+05:30"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /location
-------------

**Summary:** Read the properties of a group of locations.

- **Description:** Retrieve details of multiple locations.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **search**: Search string.
- **sort**: Field to sort results by.
- **order**: Sort order (ascending or descending).
- **city**: Filter by city.
- **state**: Filter by state.
- **country**: Filter by country.

**Responses:**

- **200**: Successfully retrieved locations.

  .. code-block:: json

     [
       {
         "name": "Main Warehouse",
         "city": "San Francisco",
         "state": "CA",
         "country": "USA",
         "address": "123 Main St",
         "zip": "94105",
         "latitude": 37.7749,
         "longitude": -122.4194
       }
     ]

---

PATCH /location
---------------

**Summary:** Update the properties of a group of locations.

- **Description:** Modify the details of multiple locations by uploading a CSV file.
- **Security:** Requires JWT authentication.

**Request Body (multipart/form-data Example):**

.. code-block:: text

   file: (binary)

**Responses:**

- **200**: Locations updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Location updated successfully",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

---

DELETE /location
----------------

**Summary:** Delete a group of locations.

- **Description:** This endpoint allows the deletion of multiple locations.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Locations deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Location deleted successfully",
       "deletedAt": "2024-09-04 00:00:00+05:30"
     }

---

GET /location/{i}
-----------------

**Summary:** Read the properties of an individual location.

- **Description:** Retrieve details of a specific location.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual location.

**Responses:**

- **200**: Successfully retrieved the location.

  .. code-block:: json

     {
       "name": "Main Warehouse",
       "city": "San Francisco",
       "state": "CA",
       "country": "USA",
       "address": "123 Main St",
       "zip": "94105",
       "latitude": 37.7749,
       "longitude": -122.4194
     }

---

DELETE /location/{i}
--------------------

**Summary:** Delete an individual location.

- **Description:** This endpoint allows the deletion of a specific location.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual location.

**Responses:**

- **200**: Location deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Location deleted successfully",
       "deletedAt": "2024-09-04 00:00:00+05:30"
     }

---

PATCH /location/{i}
-------------------

**Summary:** Update the properties of an individual location.

- **Description:** Modify the details of a specific location.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual location.

**Request Body (Example):**

.. code-block:: json

   {
     "name": "Main Warehouse",
     "city": "San Francisco",
     "state": "CA",
     "country": "USA",
     "address": "123 Main St",
     "zip": "94105",
     "latitude": 37.7749,
     "longitude": -122.4194
   }

**Responses:**

- **200**: Location updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Location updated successfully",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

