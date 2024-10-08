SIM Card Endpoints
==================

This section covers all operations available for SIM Cards, including creating, reading, updating, deleting, and allocating individual or multiple SIM cards.

Table of Operations
===================

+-------------------+--------------------------------------------------+----------------------------------+
| **Method**        | **Description**                                  | **Endpoint**                     |
+===================+==================================================+==================================+
| POST              | Create a new SIM card or upload in bulk          | /sim_card                        |
+-------------------+--------------------------------------------------+----------------------------------+
| DELETE            | Delete a group of SIM cards                      | /sim_card                        |
+-------------------+--------------------------------------------------+----------------------------------+
| GET               | Read the properties of a group of SIM cards      | /sim_card                        |
+-------------------+--------------------------------------------------+----------------------------------+
| PATCH             | Update the properties of a group of SIM cards    | /sim_card                        |
+-------------------+--------------------------------------------------+----------------------------------+
| DELETE            | Delete an individual SIM card                    | /sim_card/{i}                    |
+-------------------+--------------------------------------------------+----------------------------------+
| GET               | Read the properties of an individual SIM card    | /sim_card/{i}                    |
+-------------------+--------------------------------------------------+----------------------------------+
| PATCH             | Update the properties of an individual SIM card  | /sim_card/{i}                    |
+-------------------+--------------------------------------------------+----------------------------------+
| POST              | Allocate a SIM card to another entity            | /sim_card/{i}/allocate           |
+-------------------+--------------------------------------------------+----------------------------------+
| POST              | Enable or disable a SIM card                     | /sim_card/{i}/enable             |
+-------------------+--------------------------------------------------+----------------------------------+
| POST              | Activate a telecommunication service subscription| /sim_card/{i}/activate           |
+-------------------+--------------------------------------------------+----------------------------------+

---

POST /sim_card
--------------

**Summary:** Create a new SIM card.

- **Description:** This endpoint allows for the creation of a new SIM card or bulk creation via file upload.
- **Security:** Requires JWT authentication.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "asset_tag": "SIM001",
     "company": "Irasus Technologies",
     "status_label": "Active",
     "iccid": "12345678901234567890",
     "imsi": "123456789012345",
     "msisdn": "1234567890"
   }

**Responses:**

- **201**: SIM card created successfully.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **409**: Resource already exists.
- **500**: Internal server error.

---

DELETE /sim_card
----------------

**Summary:** Delete a group of SIM cards.

- **Description:** This endpoint allows the deletion of a group of SIM cards. Requires JWT authorization.

**Responses:**

- **200**: Successfully deleted.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

---

GET /sim_card
-------------

**Summary:** Read the properties of a group of SIM cards.

- **Description:** Retrieve details of multiple SIM cards. Supports filtering, sorting, and pagination.

**Query Parameters:**

- **limit**: Maximum number of SIM cards to return.
- **offset**: Number of SIM cards to skip before starting to collect the result set.
- **search**: General search term.
- **sort**: Field to sort by.
- **order**: Sort order, either `asc` or `desc`.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label.

**Responses:**

- **200**: Successfully retrieved SIM cards.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

---

PATCH /sim_card
---------------

**Summary:** Update the properties of a group of SIM cards.

- **Description:** This endpoint allows the bulk update of SIM card details. The updates are provided via a CSV file or JSON input.

**Request Body (CSV File):**

- **file**: (binary) A CSV file containing the asset details to update.

**Responses:**

- **200**: SIM cards updated successfully.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

---

DELETE /sim_card/{i}
--------------------

**Summary:** Delete an individual SIM card.

- **Description:** This endpoint allows deletion of an individual SIM card.

**Path Parameters:**

- **i**: Identifier of the individual SIM card.

**Responses:**

- **200**: SIM card deleted successfully.

**Example Response (JSON):**

.. code-block:: json

   {
     "status": "success",
     "message": "SIM card deleted successfully",
     "deletedAt": "2024-07-30T12:34:56Z",
     "asset_tag": "SIM001"
   }

---

GET /sim_card/{i}
-----------------

**Summary:** Read the properties of an individual SIM card.

- **Description:** Retrieve details of a specific SIM card.

**Path Parameters:**

- **i**: Identifier of the individual SIM card.

**Responses:**

- **200**: SIM card details returned successfully.

**Example Response (JSON):**

.. code-block:: json

   {
     "asset_tag": "SIM001",
     "company": "Irasus Technologies",
     "status_label": "Active",
     "iccid": "12345678901234567890",
     "imsi": "123456789012345",
     "msisdn": "1234567890"
   }

---

PATCH /sim_card/{i}
-------------------

**Summary:** Update the properties of an individual SIM card.

- **Description:** Modify the details of a specific SIM card.

**Path Parameters:**

- **i**: Identifier of the individual SIM card.

**Request Body (JSON):**

.. code-block:: json

   {
     "asset_tag": "SIM001",
     "company": "Irasus Technologies",
     "status_label": "Active",
     "iccid": "12345678901234567890",
     "imsi": "123456789012345",
     "msisdn": "1234567890"
   }

**Responses:**

- **200**: SIM card updated successfully.

---

POST /sim_card/{i}/allocate
---------------------------

**Summary:** Allocate a SIM card to another entity.

- **Description:** Allocate a SIM card to a different entity such as a vehicle, user, or location.

**Path Parameters:**

- **i**: Identifier of the individual SIM card.

**Request Body (JSON):**

.. code-block:: json

   {
     "target_category": "Vehicle",
     "target_individual": "Vehicle001",
     "status_label": "In Use"
   }

---

POST /sim_card/{i}/enable
-------------------------

**Summary:** Enable or disable the SIM card.

- **Description:** Enable or disable the SIM card.

**Path Parameters:**

- **i**: Identifier of the individual SIM card.

**Request Body (JSON):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "active",
     "status_label": "In Use"
   }

**Responses:**

- **200**: SIM card enabled or disabled successfully.

---

POST /sim_card/{i}/activate
---------------------------

**Summary:** Activate a telecommunication service subscription.

- **Description:** Activate a telecommunication service subscription associated with the SIM card.

**Path Parameters:**

- **i**: Identifier of the individual SIM card.

**Request Body (JSON):**

.. code-block:: json

   {
     "operation_type": "activate",
     "service_provider": "Telco Provider",
     "plan": "Unlimited Data"
   }

**Responses:**

- **200**: SIM card activated successfully.
