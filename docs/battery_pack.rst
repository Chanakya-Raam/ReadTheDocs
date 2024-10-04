Battery Pack Endpoints
======================

This section covers all operations available for Battery Packs, including creating, reading, updating, deleting, and allocating battery packs.

POST `/battery_pack`
--------------------

**Summary:** Create a new battery pack.

- **Description:** This endpoint allows for the creation of a new battery pack or bulk creation via file upload.
- **Security:** Requires JWT authentication.

**Request Body:**

- Choose either JSON input or upload a file with asset details.
- **file**: (binary) The file containing the details of battery packs for bulk upload.

**Responses:**

- **201**: Battery pack created successfully or bulk upload processed.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden action.
- **404**: Battery pack not found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request (JSON):**

.. code-block:: bash

   curl -X POST "https://example.com/api/battery_pack" \
       -H "Authorization: Bearer <JWT>" \
       -d '{ "model_name": "BP-1000", "manufacturer": "BatteryCo", "status": "active" }'


DELETE `/battery_pack/{i}`
--------------------------

**Summary:** Delete an individual battery pack.

- **Description:** This endpoint allows deletion of an individual battery pack specified by the `{i}` parameter.
- **Security:** Requires JWT authentication.

**Parameters:**

- **i**: (path) The ID of the battery pack to be deleted.

**Responses:**

- **200**: Battery pack deleted successfully.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden action.
- **404**: Battery pack not found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X DELETE "https://example.com/api/battery_pack/1" \
       -H "Authorization: Bearer <JWT>" 


GET `/battery_pack/{i}`
-----------------------

**Summary:** Read the properties of an individual battery pack.

- **Description:** Retrieve details of a specific battery pack identified by the `{i}` parameter.
- **Security:** Requires JWT authentication.

**Parameters:**

- **i**: (path) The ID of the battery pack to retrieve.

**Responses:**

- **200**: Battery pack details returned successfully.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden action.
- **404**: Battery pack not found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X GET "https://example.com/api/battery_pack/1" \
       -H "Authorization: Bearer <JWT>"


PATCH `/battery_pack/{i}`
-------------------------

**Summary:** Update the properties of an individual battery pack.

- **Description:** Modify the details of a specific battery pack.
- **Security:** Requires JWT authentication.

**Parameters:**

- **i**: (path) The ID of the battery pack to update.

**Request Body:**

- **JSON**: The properties to update for the battery pack.

**Responses:**

- **200**: Battery pack updated successfully.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden action.
- **404**: Battery pack not found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request (JSON):**

.. code-block:: bash

   curl -X PATCH "https://example.com/api/battery_pack/1" \
       -H "Authorization: Bearer <JWT>" \
       -d '{ "model_name": "BP-1000", "status": "inactive" }'


POST `/battery_pack/{i}/allocate`
---------------------------------

**Summary:** Allocate a battery pack to another asset, user, or location.

- **Description:** Allocate an individual battery pack to another asset, user, or location.
- **Security:** Requires JWT authentication.

**Parameters:**

- **i**: (path) The ID of the battery pack to allocate.

**Request Body:**

- **file**: (binary) The file containing allocation details, or JSON input specifying the allocation.

**Responses:**

- **200**: Allocation processed successfully.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden action.
- **404**: Battery pack not found.
- **408**: Request timeout.
- **409**: Conflict in allocation.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X POST "https://example.com/api/battery_pack/1/allocate" \
       -H "Authorization: Bearer <JWT>" \
       -d '{ "location": "Warehouse 12" }'


POST `/battery_pack/{i}/enable`
-------------------------------

**Summary:** Enable or disable an individual battery pack.

- **Description:** Toggle the enable/disable status of a battery pack.
- **Security:** Requires JWT authentication.

**Parameters:**

- **i**: (path) The ID of the battery pack to enable or disable.

**Request Body:**

- **JSON**: Enable/disable data.

**Responses:**

- **200**: Battery pack status updated successfully.
- **400**: Invalid request.
- **401**: Unauthorized access.
- **403**: Forbidden action.
- **404**: Battery pack not found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X POST "https://example.com/api/battery_pack/1/enable" \
       -H "Authorization: Bearer <JWT>" \
       -d '{ "enabled": true }'
