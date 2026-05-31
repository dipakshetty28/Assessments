# Orders Review API

## Task

Fix the incorrect order total calculation and add an optional status filter to `GET /orders`.

## Workspace checks

The interview environment is already provisioned. Use the Nexterview Run button to execute the visible checks against the current files and seed data.

The intentional bug is in `app/services/orders.py`: quantity is ignored when calculating totals.
