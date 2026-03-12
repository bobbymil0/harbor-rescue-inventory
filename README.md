Week 2 – Harbor Rescue Inventory
Summary

The Harbor Rescue Inventory program manages a list of emergency supplies for rescue missions.
It uses different list functions to check cargo, find supplies, and create reports.
Each function helps rescuers quickly locate items and organize inventory.
The program also checks priority supplies for urgent missions.

Approach

mission_snapshot:
Returns a copy of the full supply list so the original list stays unchanged.

cargo_window:
Returns a portion (slice) of the supply list between two positions.

first_supply_index:
Searches the list and returns the first position of the target supply item.

supply_report:
Counts how many times a supply item appears in the list.

priority_load (stretch):
Creates a new list where priority supplies are placed first without changing the original list.

Complexity Reasoning
Function	Time Complexity	Why
mission_snapshot	O(n)	It copies every element in the list once
cargo_window	O(k)	It copies only the sliced portion
first_supply_index	O(n)	It may need to check every item
supply_report	O(n)	It scans the full list to count items
priority_load (stretch)	O(n)	It goes through the list to reorder items
Edge-Case Checklist

✔ empty list
✔ one-item list
✔ target missing
✔ repeated values
✔ slice goes past end
✔ size is zero
✔ size is negative
✔ original list unchanged in priority_load

Assistance / Sources

Person / tool / website:
Blackbox and Google 

Help received:
Help understanding list operations, slicing, and time complexity explanation.

Person / tool / website:
Class slides / Professor Ben

Help received:
Explanation of list functions and algorithm concepts.
