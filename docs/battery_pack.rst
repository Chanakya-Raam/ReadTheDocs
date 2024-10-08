Battery Pack Endpoints
======================

This section covers all operations available for Battery Packs, including creating, reading, updating, deleting, and allocating individual or multiple battery packs.

---

POST `/battery_pack`
--------------------

**Summary:** Create a new battery pack.

- **Description:** This endpoint allows for the creation of a new battery pack or bulk creation via file upload.
- **Security:** Requires JWT authentication.

**Request Body (JSON Example):**

.. code-block:: json

   {
     "asset_tag": "IRASUS01",
     "company": "Irasus Technologies Private Limited",
     "status_label": "In Warehouse",
     "model": "Model X",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "location": "Delhi",
     "warranty_months": "3",
     "battery_pack": {
       "battery_cell_chemistry": "Li-NMC",
       "battery_pack_nominal_voltage": "48 V",
       "battery_pack_nominal_charge_capacity": "48 Ah",
       "bms_type": "Firmware",
       "battery_cell_type": "Cylindrical",
       "battery_pack_casing": "Plastic"
     }
   }

**Responses:**

- **201**: Battery pack created successfully.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **409**: Resource already exists.
- **500**: Internal server error.

---

DELETE `/battery_pack`
----------------------

**Summary:** Delete a group of battery packs.

- **Description:** This endpoint allows the deletion of a group of battery packs. Requires JWT authorization.

**Responses:**

- **200**: Successfully deleted.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

**Example Request:**

.. code-block:: bash

   curl -X DELETE "https://example.com/api/battery_pack" \
       -H "Authorization: Bearer <JWT>"

---

GET `/battery_pack`
-------------------

**Summary:** Read the properties of a group of battery packs.

- **Description:** Retrieve details of multiple battery packs. Supports filtering, sorting, and pagination.

**Query Parameters:**

- **limit**: Maximum number of battery packs to return.
- **offset**: Number of battery packs to skip before starting to collect the result set.
- **search**: General search term.
- **sort**: Field to sort by.
- **order**: Sort order, either `asc` or `desc`.
- **model_name**: Filter by model name.
- **manufacturer_name**: Filter by manufacturer name.
- **owner_name**: Filter by owner name.
- **location**: Filter by location.
- **status_label**: Filter by status label.

**Responses:**

- **200**: Successfully retrieved battery packs.

**Example Response (JSON):**

.. code-block:: json

   [
     {
       "asset_tag": "IRASUS01",
       "company": "Irasus Technologies Private Limited",
       "status_label": "In Warehouse",
       "model": "Model X",
       "manufacturer_name": "Irasus Technologies Private Limited",
       "location": "Delhi",
       "warranty_months": "3",
       "battery_pack": {
         "battery_cell_chemistry": "Li-NMC",
         "battery_pack_nominal_voltage": "48 V",
         "battery_pack_nominal_charge_capacity": "48 Ah",
         "bms_type": "Firmware",
         "battery_cell_type": "Cylindrical",
         "battery_pack_casing": "Plastic"
       }
     }
   ]

---

PATCH `/battery_pack`
---------------------

**Summary:** Update the properties of a group of battery packs.

- **Description:** This endpoint allows the bulk update of battery pack details. The updates are provided via a CSV file or JSON input.

**Request Body (CSV File):**

- **file**: (binary) A CSV file containing the asset details to update.

**Responses:**

- **200**: Assets updated successfully.
- **400**: Invalid request parameters.
- **401**: Unauthorized access.
- **403**: Access forbidden.
- **404**: Resource not found.
- **500**: Internal server error.

---

DELETE `/battery_pack/{i}`
--------------------------

**Summary:** Delete an individual battery pack.

- **Description:** This endpoint allows deletion of an individual battery pack.

**Path Parameters:**

- **i**: Identifier of the individual battery pack.

**Responses:**

- **200**: Asset deleted successfully.

**Example Response (JSON):**

.. code-block:: json

   {
     "status": "success",
     "message": "Asset deleted successfully",
     "deletedAt": "2024-07-30T12:34:56Z",
     "asset_tag": "IRASUS01"
   }

---

GET `/battery_pack/{i}`
-----------------------

**Summary:** Read the properties of an individual battery pack.

- **Description:** Retrieve details of a specific battery pack.

**Path Parameters:**

- **i**: Identifier of the individual battery pack.

**Responses:**

- **200**: Battery pack details returned successfully.

**Example Response (JSON):**

.. code-block:: json

   {
     "asset_tag": "IRASUS01",
     "company": "Irasus Technologies Private Limited",
     "status_label": "In Warehouse",
     "model": "Model X",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "location": "Delhi",
     "battery_pack": {
       "battery_cell_chemistry": "Li-NMC",
       "battery_pack_nominal_voltage": "48 V",
       "battery_pack_nominal_charge_capacity": "48 Ah",
       "bms_type": "Firmware",
       "battery_cell_type": "Cylindrical",
       "battery_pack_casing": "Plastic"
     }
   }

---

PATCH `/battery_pack/{i}`
-------------------------

**Summary:** Update the properties of an individual battery pack.

- **Description:** Modify the details of a specific battery pack.

**Path Parameters:**

- **i**: Identifier of the individual battery pack.

**Request Body (JSON):**

.. code-block:: json

   {
     "asset_tag": "IRASUS01",
     "company": "Irasus Technologies Private Limited",
     "status_label": "In Warehouse",
     "model": "Model X",
     "manufacturer_name": "Irasus Technologies Private Limited",
     "location": "Delhi",
     "battery_pack": {
       "battery_cell_chemistry": "Li-NMC",
       "battery_pack_nominal_voltage": "48 V",
       "battery_pack_nominal_charge_capacity": "48 Ah",
       "bms_type": "Firmware",
       "battery_cell_type": "Cylindrical",
       "battery_pack_casing": "Plastic"
     }
   }

**Responses:**

- **200**: Asset updated successfully.

---

POST `/battery_pack/{i}/allocate`
---------------------------------

**Summary:** Allocate an individual battery pack to another asset, user, or location.

- **Description:** Allocate a battery pack to a different entity such as a vehicle, location, or user.

**Path Parameters:**

- **i**: Identifier of the individual battery pack.

**Request Body (JSON):**

.. code-block:: json

   {
     "target_category": "Vehicle",
     "target_individual": "IRASUS01",
     "status_label": "In Vehicle"
   }

---

POST `/battery_pack/{i}/enable`
-------------------------------

**Summary:** Enable or disable an individual battery pack.

- **Description:** Enable or disable the battery pack.

**Path Parameters:**

- **i**: Identifier of the individual battery pack.

**Request Body (JSON):**

.. code-block:: json

   {
     "operation_type": "enable",
     "operation_specifications": "discharging",
     "status_label": "In Warehouse"
   }

**Responses:**

- **200**: Asset enabled or disabled successfully.

**Example Response (JSON):**

.. code-block:: json

   {
     "issuedAt": "2024-09-04 00:00:00+05:30",
     "enabledAt": "2024-09-04 00:00:00+05:30"
   }
