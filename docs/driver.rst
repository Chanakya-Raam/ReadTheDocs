Driver Endpoints
================

This section covers all operations available for drivers, including creating, reading, updating, deleting, and allocating drivers to vehicles.

**Table of Operations**

+--------------------+---------------------------------------------------+------------------------------------+
| **Method**         | **Description**                                   | **Endpoint**                       |
+====================+===================================================+====================================+
| POST               | Create a new driver                               | /driver                            |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of a group of drivers         | /driver                            |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Update the properties of an individual driver     | /driver/{i}                        |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of an individual driver       | /driver/{i}                        |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete an individual driver                       | /driver/{i}                        |
+--------------------+---------------------------------------------------+------------------------------------+
| POST               | Allocate a driver to a vehicle                    | /driver/{i}/allocate               |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Get drivers allocated to a vehicle                | /vehicle/{i}/driver                |
+--------------------+---------------------------------------------------+------------------------------------+

---

POST /driver
------------

**Summary:** Create a new driver.

- **Description:** This endpoint allows the creation of a new driver.
- **Security:** Requires JWT authentication.

**Request Body (multipart/form-data Example):**

.. code-block:: json

   {
     "driver_name": "Driver",
     "driver_phone": 9876543210,
     "aadhar_card": "aadhar_card.png",
     "pan_card": "pan_card.png",
     "driving_license": "driving_license.png"
   }

**Responses:**

- **201**: Driver created successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "driver created successfully",
       "createdAt": "2024-09-04 00:00:00+05:30"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /driver
-----------

**Summary:** Read the properties of a group of drivers.

- **Description:** Retrieve details of multiple drivers.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **driver_phone**: Filter by driver phone number.

**Responses:**

- **200**: Successfully retrieved drivers.

  .. code-block:: json

     [
       {
         "driver_name": "Driver",
         "driver_phone": 9876543210,
         "aadhar_card": "string",
         "pan_card": "string",
         "driving_license": "string"
       }
     ]

---

POST /driver/{i}
----------------

**Summary:** Update the properties of an individual driver.

- **Description:** Modify the details of a specific driver.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual driver.

**Request Body (multipart/form-data Example):**

.. code-block:: json

   {
     "driver_phone": 9876543210,
     "aadhar_card": "aadhar_card.png",
     "pan_card": "pan_card.png",
     "driving_license": "driving_license.png"
   }

**Responses:**

- **200**: Driver updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Driver updated successfully",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

---

GET /driver/{i}
---------------

**Summary:** Read the properties of an individual driver.

- **Description:** Retrieve details of a specific driver.

**Path Parameters:**

- **i**: Identifier of the individual driver.

**Responses:**

- **200**: Driver details retrieved successfully.

  .. code-block:: json

     {
       "driver_name": "Driver",
       "driver_phone": 9876543210,
       "aadhar_card": "aadhar_card.png",
       "pan_card": "pan_card.png",
       "driving_license": "driving_license.png"
     }

---

DELETE /driver/{i}
------------------

**Summary:** Delete an individual driver.

- **Description:** This endpoint allows the deletion of an individual driver.

**Path Parameters:**

- **i**: Identifier of the individual driver.

**Responses:**

- **200**: Driver deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Driver deleted successfully",
       "deletedAt": "2024-09-04 00:00:00+05:30"
     }

---

POST /driver/{i}/allocate
-------------------------

**Summary:** Allocate an individual driver to a vehicle.

- **Description:** This endpoint assigns a driver to a vehicle.

**Path Parameters:**

- **i**: Identifier of the individual driver.

**Request Body (Example):**

.. code-block:: json

   {
     "driver_name": "Driver"
   }

**Responses:**

- **200**: Driver allocated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Driver allocated successfully",
       "allocatedAt": "2024-09-04 00:00:00+05:30"
     }

---

GET /vehicle/{i}/driver
-----------------------

**Summary:** Get the properties of a group of drivers allocated to a vehicle.

- **Description:** Retrieve details of drivers allocated to a vehicle.

**Path Parameters:**

- **i**: Identifier of the individual vehicle.

**Responses:**

- **200**: Drivers allocated to the vehicle retrieved successfully.

  .. code-block:: json

     [
       {
         "driver_name": "Driver",
         "driver_phone": 9876543210,
         "aadhar_card": "string",
         "pan_card": "string",
         "driving_license": "string"
       }
     ]
