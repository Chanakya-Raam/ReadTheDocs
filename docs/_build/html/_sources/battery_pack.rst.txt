Battery Pack Endpoints
======================

This section covers all operations available for Battery Packs, including reading, updating, and deleting groups of Battery Packs.

DELETE `/battery_pack`
----------------------

**Summary:** Delete a group of battery packs.

- **Description:** This endpoint allows the deletion of a group of battery packs. Only users with proper authorization (JWT) can perform this action.
- **Security:** Requires JWT authentication.
- **Tags:** Battery Pack, Delete Asset

**Responses:**

- **200**: Successful deletion of the battery pack group.
- **400**: Invalid request.
- **401**: Unauthorized access (JWT missing or invalid).
- **403**: Forbidden action.
- **404**: Battery pack group not found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X DELETE "https://example.com/api/battery_pack" \
       -H "Authorization: Bearer <JWT>" 


GET `/battery_pack`
-------------------

**Summary:** Retrieve the properties of a group of battery packs.

- **Description:** This endpoint fetches the details of a group of battery packs. Users can filter, sort, and paginate the results based on various query parameters.
- **Security:** Requires JWT authentication.
- **Tags:** Battery Pack, Read Asset

**Query Parameters:**

- **limit**: (integer) Maximum number of battery packs to return.
- **offset**: (integer) Number of battery packs to skip for pagination.
- **search**: (string) Search term to filter battery packs.
- **sort**: (string) Attribute to sort the results by (e.g., `model_name`, `location`).
- **order**: (string) Sorting order, either `asc` or `desc`.
- **status_label**: (string) Filter by status of the battery packs (e.g., `active`, `inactive`).

**Responses:**

- **200**: Successful retrieval of battery pack details.
- **400**: Invalid query parameters.
- **401**: Unauthorized access (JWT missing or invalid).
- **403**: Forbidden action.
- **404**: No battery packs found.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X GET "https://example.com/api/battery_pack?limit=10&sort=model_name&order=asc" \
       -H "Authorization: Bearer <JWT>"

**Example Response:**

.. code-block:: json

   [
     {
       "id": 1,
       "model_name": "BP-1000",
       "manufacturer": "BatteryCo",
       "owner": "Company A",
       "location": "Warehouse 12",
       "status": "active"
     },
     {
       "id": 2,
       "model_name": "BP-2000",
       "manufacturer": "BatteryCo",
       "owner": "Company B",
       "location": "Warehouse 15",
       "status": "inactive"
     }
   ]


PATCH `/battery_pack`
---------------------

**Summary:** Update the properties of a group of battery packs.

- **Description:** This endpoint allows the bulk update of battery pack details. The updates are provided via a CSV file, and the endpoint requires proper authorization.
- **Security:** Requires JWT authentication.
- **Tags:** Battery Pack, Update Asset

**Request Body:**

- **file**: (binary) A CSV file containing the asset details to update.

**Responses:**

- **200**: Successful update of battery pack details.
- **400**: Invalid CSV file or parameters.
- **401**: Unauthorized access (JWT missing or invalid).
- **403**: Forbidden action.
- **404**: No battery packs found for update.
- **408**: Request timeout.
- **500**: Internal server error.
- **502**: Bad gateway.

**Example Request:**

.. code-block:: bash

   curl -X PATCH "https://example.com/api/battery_pack" \
       -H "Authorization: Bearer <JWT>" \
       -F "file=@battery_pack_update.csv"

**Example CSV Format:**

.. code-block:: csv

   id,model_name,manufacturer,status
   1,BP-1000,BatteryCo,active
   2,BP-2000,BatteryCo,inactive
