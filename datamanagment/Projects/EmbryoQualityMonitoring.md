(EQM_project)=
# Embryos Quality Monitoring (EQM)


## Project summary
* **Status:** Ongoing
* **Goals:** Monitor the zebra fish embryos quality to spot correlations in defects. Potentially help the animalerie with a setting up a long term solution
* **Contributors:** Chloé, Laurel
* **Starting date:** Dec. 2022
* **Tools involved:** PyRat
* **Project documentation**

----
## Project issues/caveats
* PyRat exports do not provide history. Very difficult to track changes in tanks as tank situation might have changed between two exports

## Project TODO list
- Add amount of food per fish 
- Consolidate the history between tanks such that the amount of food given corresponds to the actual number of fishes in the tank
- Send a summary of the discussion (24/01/2023) to Scionics to put some pressure

----
## Project History
* 2023
    * Week 4: 
        * Discussion with Scionics about implementation of missing features and SV-IT deployement
            * Still a sever side issue at EPFL (python versions) thus running old PyRat version
            * Export to different format to keep tank history, status of API
            * Very disapointing discussion, does not look like a compagny that provides a commercial tool. They will come back to us within 15 days
        * Guillaume confirmed that Florian will be in charge of scoring the embryos
    * Week 3: 
        * Agreed during lab meeting about the common severiry notation
        * Guillaume Valentin agreed to use wildtype lines frenquently crossed to provide us with a benchmark dataset
    * Week 2: 
        * Brainstormed about the severity notation (e.g. 2x1:4x2:1x3:ydm) 
        * Analysed the first cross with embryo quality entered in PyRat by users
* 2022
    * Weeks 49-52: 
        * Prototype code ready to read PyRat ```csv``` exports
        * Match ```tankID``` and ```crossingID``` database to extract information
        * Push the results to a google sheet



