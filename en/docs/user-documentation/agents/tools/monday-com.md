# Monday.com

Monday tools let an Agent inspect and manage boards, groups, items, columns, subitems, updates, and related workspace data. Available actions depend on the configured Monday identity and board permissions.

In **Spaces → Tools**, add Monday and complete the authentication shown by the form. Select personal or workspace credentials when available; personal credentials preserve each user's board access, while shared credentials act as the configured account. Confirm that the owner can access the required boards and private boards. Share the tool with the intended Space and add it to the Agent.

Start with one board read and one item lookup. Before changing data, inspect column IDs and types, group membership, and any subitems or updates that should be preserved. Specify the item and fields to change, then read that same item back in Monday. Missing boards or columns commonly indicate account membership, private-board access, or field visibility issues.

## Available operations

The Monday tool covers these areas; the names below are the operations shown in the source tool list:

- Boards: `get_boards`, `get_board_values`, `create_board`, `get_board_analytics`.
- Items: `get_board_items`, `get_item_details`, `search_items`, `create_item`, `create_multiple_items`, `update_item`, `update_item_name`, `delete_item`, `move_item_to_board`, `get_items_by_column_value`.
- Groups and columns: `create_group`, `get_group_details`, `delete_group`, `duplicate_group`, `create_column`, `get_column_values`, `get_file_column_values`, `upload_file_to_column`.
- Subitems and updates: `create_subitem`, `update_subitem`, `get_subitem_values`, `create_update`.
- People and activity: `find_user_by_name`, `get_user_details`, `get_activity_logs`.

Monday administrators must install the application in the target Monday workspace before OAuth completes. Personal credentials are preferable when actions should follow each user's access; a workspace credential makes actions use the configured account. The source tool list limits board and item listing responses to 100 records per call; use filters or follow-up queries for larger sets. Inspect column IDs before updates, and be cautious with bulk creation or deletion.

## Credential setup

Monday administrators must install the application in the target Monday workspace before OAuth authorization. The previous integration offered personal and workspace credentials; use whichever options the current tool form presents. Do not reuse a fixed authorization URL/client ID from another environment.
