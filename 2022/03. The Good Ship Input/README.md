## Input:
Each test case will contain:<br>
* A line containing two positive integers separated by spaces:
  - The first integer (X) represents the number of systems listed in the shipyard database.
  - The second integer (Y) indicates the number of systems reported by the on-board computer. Y will be less than or equal to X.
* X rows containing the names of the systems listed in the shipyard database. The names are unique within a given test case and may contain letters and spaces.
* Y lines containing the names of systems reported by the on-board computer as operational. All names in this section will be duplicates of names stored in the database
shipyard data.
## Output:
For each test case, the program must return a list of systems requiring testing in alphabetical order (case-insensitive), one system per line.
