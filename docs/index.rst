Irasus API Documentation
=========================

Welcome to the **Irasus REST API Documentation**. This document outlines all available categories of operations in the **Irasus Battery Management System**, allowing users to manage assets like Battery Packs, Vehicles, SIM Cards, and more. The API is designed to offer a unified solution for monitoring, controlling, and managing these assets from anywhere in the world.

Overview
--------

The Irasus API provides endpoints that help manage battery packs and other related assets efficiently. Whether you’re building applications for electric vehicle fleet management, battery health monitoring, or location tracking, this API enables seamless integration with your systems.

Key Features
------------

- **Battery Pack Management**: Create, read, update, delete, allocate, and enable/disable battery packs.
- **Vehicle Control**: Manage vehicle assets linked to battery packs.
- **SIM Card Operations**: Manage SIM cards used in battery tracking and communication.
- **Swapping Stations**: Manage battery pack swapping stations, including operations and status checks.
- **Charger Operations**: Monitor and manage charger assets (both advanced and basic models).
- **Geofencing & Location**: Track and update location-based data, including geofences.
- **User Management**: Assign assets to users and manage user-specific operations.


Getting Started
---------------

All API operations require authentication via JSON Web Tokens (JWT). Ensure that the token is passed in the `Authorization` header in the following format:

.. code-block:: bash

   Authorization: Bearer <JWT>

Contents
--------

.. toctree::
   :maxdepth: 2
   :caption: Asset Categories:

   assets_category