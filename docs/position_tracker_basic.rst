Position Tracker (Basic) Endpoints
===================================

This section covers all operations available for Position Trackers (Basic), including creating, reading, updating, deleting, and allocating individual or multiple position trackers.

**Table of Operations**

+-------------------+--------------------------------------------------+------------------------------------+
| **Method**        | **Description**                                  | **Endpoint**                       |
+===================+==================================================+====================================+
| POST              | Create a new position tracker (basic) or upload  | /position_tracker_basic            |
|                   | in bulk                                          |                                    |
+-------------------+--------------------------------------------------+------------------------------------+
| DELETE            | Delete a group of position trackers (basic)      | /position_tracker_basic            |
+-------------------+--------------------------------------------------+------------------------------------+
| GET               | Read the properties of a group of position       | /position_tracker_basic            |
|                   | trackers (basic)                                 |                                    |
+-------------------+--------------------------------------------------+------------------------------------+
| PATCH             | Update the properties of a group of position     | /position_tracker_basic            |
|                   | trackers (basic)                                 |                                    |
+-------------------+--------------------------------------------------+------------------------------------+
| DELETE            | Delete an individual position tracker (basic)    | /position_tracker_basic/{i}        |
+-------------------+--------------------------------------------------+------------------------------------+
| GET               | Read the properties of an individual position    | /position_tracker_basic/{i}        |
|                   | tracker (basic)                                  |                                    |
+-------------------+--------------------------------------------------+------------------------------------+
| PATCH             | Update the properties of an individual position  | /position_tracker_basic/{i}        |
|                   | tracker (basic)                                  |                                    |
+-------------------+--------------------------------------------------+------------------------------------+
| POST              | Allocate a position tracker (basic) to another   | /position_tracker_basic/{i}/allocate|
|                   | entity                                           |                                    |
+-------------------+--------------------------------------------------+------------------------------------+
| POST              | Enable or disable a position tracker (basic)     | /position_tracker_basic/{i}/enable |
+-------------------+--------------------------------------------------+------------------------------------+

---

POST /position_tracker_basic
----------------------------

**Summary:** Create a new position tracker (basic).

- **Description:** This endpoint allows for the creation of a new position tracker (basic) or bulk creation via file upload.
- **Security:** Requires JWT authentication.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "asset_tag": "TRACKER01",
     "company": "Irasus Technologies Private Limited",
     "status_label": "Active",
     "model": "Basic Tracker Model",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "location": "Delhi"
   }

**Responses:**

- **201**: Position tracker created successfully.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **409**: Resource already exists.
- **500**: Internal server error.

---

DELETE /position_tracker_basic
------------------------------

**Summary:** Delete a group of position trackers (basic).

- **Description:** This endpoint allows the deletion of a group of position trackers (basic). Requires JWT authorization.

**Responses:**

- **200**: Successfully deleted.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

---

GET /position_tracker_basic
---------------------------

**Summary:** Read the properties of a group of position trackers (basic).

- **Description:** Retrieve details of multiple position trackers (basic). Supports filtering, sorting, and pagination.

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

---

PATCH /position_tracker_basic
-----------------------------

**Summary:** Update the properties of a group of position trackers (basic).

- **Description:** This endpoint allows the bulk update of position tracker (basic) details. The updates are provided via a CSV file or JSON input.

**Request Body (CSV File):**

- **file**: (binary) A CSV file containing the asset details to update.

**Responses:**

- **200**: Position trackers updated successfully.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

---

DELETE /position_tracker_basic/{i}
-----------------------------------

**Summary:** Delete an individual position tracker (basic).

- **Description:** This endpoint allows deletion of an individual position tracker (basic).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Responses:**

- **200**: Position tracker deleted successfully.

---

GET /position_tracker_basic/{i}
-------------------------------

**Summary:** Read the properties of an individual position tracker (basic).

- **Description:** Retrieve details of a specific position tracker (basic).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Responses:**

- **200**: Position tracker details returned successfully.

---

PATCH /position_tracker_basic/{i}
---------------------------------

**Summary:** Update the properties of an individual position tracker (basic).

- **Description:** Modify the details of a specific position tracker (basic).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Request Body (JSON):**

.. code-block:: json

   {
     "asset_tag": "TRACKER01",
     "company": "Irasus Technologies Private Limited",
     "status_label": "Active",
     "model": "Basic Tracker Model",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "location": "Delhi"
   }

**Responses:**

- **200**: Position tracker updated successfully.

---

POST /position_tracker_basic/{i}/allocate
-----------------------------------------

**Summary:** Allocate an individual position tracker (basic) to another entity.

- **Description:** Allocate a position tracker to a different entity such as a vehicle, user, or location.

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Request Body (JSON):**

.. code-block:: json

   {
     "target_category": "Vehicle",
     "target_individual": "Vehicle001",
     "status_label": "In Use"
   }

---

POST /position_tracker_basic/{i}/enable
---------------------------------------

**Summary:** Enable or disable a position tracker (basic).

- **Description:** Enable or disable the position tracker (basic).

**Path Parameters:**

- **i**: Identifier of the individual position tracker.

**Request Body (JSON):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "tracking",
     "status_label": "Active"
   }

**Responses:**

- **200**: Position tracker enabled or disabled successfully.
