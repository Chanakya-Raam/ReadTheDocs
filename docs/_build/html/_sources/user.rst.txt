User Endpoints
==============

This section covers all operations available for users, including creating, reading, updating, and deleting users.

**Table of Operations**

+--------------------+---------------------------------------------------+------------------------------------+
| **Method**         | **Description**                                   | **Endpoint**                       |
+====================+===================================================+====================================+
| POST               | Create a new user                                 | /user                              |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of a group of users           | /user                              |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of a group of users         | /user                              |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete a group of users                           | /user                              |
+--------------------+---------------------------------------------------+------------------------------------+
| GET                | Read the properties of an individual user         | /user/{i}                          |
+--------------------+---------------------------------------------------+------------------------------------+
| DELETE             | Delete an individual user                         | /user/{i}                          |
+--------------------+---------------------------------------------------+------------------------------------+
| PATCH              | Update the properties of an individual user       | /user/{i}                          |
+--------------------+---------------------------------------------------+------------------------------------+

---

POST /user
----------

**Summary:** Create a new user.

- **Description:** This endpoint allows the creation of a new user.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **search**: Search string.
- **sort**: Field to sort results by.
- **order**: Sort order (ascending or descending).

**Request Body (Example):**

.. code-block:: json

   {
     "first_name": "Demo",
     "last_name": "User",
     "email": "test@irasus.com",
     "company": "Irasus Techonolgies Pvt LTD",
     "role": "Admin",
     "user_enabled": "True",
     "password": "Qwerty@123"
   }

**Responses:**

- **201**: User created successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "User created successfully",
       "createdAt": "2024-09-04 00:00:00+05:30"
     }

- **400**: Invalid request parameters.

  .. code-block:: json

     {
       "status": "error",
       "message": "Invalid request parameters"
     }

---

GET /user
---------

**Summary:** Read the properties of a group of users.

- **Description:** Retrieve details of multiple users.
- **Security:** Requires JWT authentication.

**Query Parameters:**

- **limit**: Integer for result limit.
- **offset**: Integer for result offset.
- **search**: Search string.
- **sort**: Field to sort results by.
- **order**: Sort order (ascending or descending).

**Responses:**

- **200**: Successfully retrieved users.

  .. code-block:: json

     [
       {
         "first_name": "Demo",
         "last_name": "User",
         "email": "test@irasus.com",
         "company": "Irasus Techonolgies Pvt LTD",
         "role": "Admin"
       }
     ]

---

PATCH /user
-----------

**Summary:** Update the properties of a group of users.

- **Description:** Modify the details of multiple users by uploading a CSV file.
- **Security:** Requires JWT authentication.

**Request Body (multipart/form-data Example):**

.. code-block:: text

   file: (binary)

**Responses:**

- **200**: Users updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "User updated successfully",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }

---

DELETE /user
------------

**Summary:** Delete a group of users.

- **Description:** This endpoint allows the deletion of multiple users.
- **Security:** Requires JWT authentication.

**Responses:**

- **200**: Users deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "Users deleted successfully",
       "deletedAt": "2024-09-04 00:00:00+05:30"
     }

---

GET /user/{i}
-------------

**Summary:** Read the properties of an individual user.

- **Description:** Retrieve details of a specific user.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual user.

**Responses:**

- **200**: Successfully retrieved the user.

  .. code-block:: json

     {
       "first_name": "Demo",
       "last_name": "User",
       "email": "test@irasus.com",
       "company": "Irasus Techonolgies Pvt LTD",
       "role": "Admin"
     }

---

DELETE /user/{i}
----------------

**Summary:** Delete an individual user.

- **Description:** This endpoint allows the deletion of a specific user.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual user.

**Responses:**

- **200**: User deleted successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "User deleted successfully",
       "deletedAt": "2024-09-04 00:00:00+05:30"
     }

---

PATCH /user/{i}
---------------

**Summary:** Update the properties of an individual user.

- **Description:** Modify the details of a specific user.
- **Security:** Requires JWT authentication.

**Path Parameters:**

- **i**: Identifier of the individual user.

**Request Body (Example):**

.. code-block:: json

   {
     "first_name": "Demo",
     "last_name": "User",
     "email": "test@irasus.com",
     "company": "Irasus Techonolgies Pvt LTD",
     "role": "Admin",
     "user_enabled": "True"
   }

**Responses:**

- **200**: User updated successfully.

  .. code-block:: json

     {
       "status": "success",
       "message": "User updated successfully",
       "updatedAt": "2024-09-04 00:00:00+05:30"
     }
