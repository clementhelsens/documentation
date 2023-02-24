# February

**[[CAT]](CAT_project) Cut And Tag**

* Started to reproduce the workflow
* Transferred the Zebra-fish sequencing data to Z-Fishator

--------------

**[[DLEC]](DLEC_project) Deep Learning Embryo Classification**

* Setup a dedicated Deep Learning environment on [[ZF]](ZF_project)
* Prototype code running with 2 images (treated, non-treated)
  * Classification works!
* Got new images from Virginie with fluorescent line
  * Classification still works, but too few images to get a descent training, need a few hundreds to get a convergent network

--------------

**[[DOC]](DOC_project) Documentation**

* Converged on using the same infrastructure for data management status reports and lab documentation (this website)
* Started to document what was done the past two months

--------------

**[[EQM]](EQM_project) Embryo Quality Monitoring**

* Guillaume sent us the protocol by email with the details about the screening procedure
  * Waiting for the first data to be added to Pyrat
* 2 crosses added from the fish facility
  * Follow up chat with lead developer at Scionics, less disappointed about the outcome
    * Need the EPFL server upgrade such that we can use the first API around May
    * Will be in principle able to navigate through the history by usage of custom code

--------------

**[[HMRC]](HMRC_project) HIVE Maintenance Restructuration Cleaning**

* Continue to brainstorm on HIVE structure
  * Need to clearly separate the lab users from invited users
  * Need a convention for storing videos and subsequent analyses
  * Need a first convention on user metadata
* Presentation at lab meeting (21st)
  * Agreed to set up a spreadsheet to categorize what is currently on the HIVE
  * Follow up at the next lab meeting (28th)
* Tried to setup ssh connection on the HIVE from the EPFL VPN (not working)
* Tried to setup remote connections (both ssh and remote desktop) to the machines next to the microscope, aka the `hot` data

--------------

**[[RTCT]](RTCT_project) Real-Time Cell Tracking**

* Discussion with Willi about the usage of real time cell tracking and cell state evaluation (to disturb the system at a precise time)
* Decided to name the project RTCT (Real-Time Cell Tracking)

--------------

**[[ZED]](ZED_project) Zebrafish Embryos Demultiplexing**

* Converge with Cristina on an analysis plan towards the lab meeting Feb. 14
  * Reproduce souporcell demultiplexing published results (contacts with authors)
  * Demonstrates souporcells works with labeled cells from embryos (wait reply from Loic)
* Able to reproduce the paper results
  * Spend a lot of time developing a more efficient pooling of bam files
  * Achieved very promising results
  * Contact author [nicholas.leigh@med.lu.se](nicholas.leigh@med.lu.se) is extremely enthusiast about this (consider adding me as author!)

  ```
      1) You’ve re-run the analysis and pointed out many aspects of the methods that could be improved. 
      This speaks to the reproducibly of the work and will improve the manuscript. 
      2) This new code may enable me to pool some datasets I was struggling with 
      (and I think it would help many others if they want to prove to themselves that this would work in their species)
      To me these are really nice contributions. 
      ```
      and
      ```
      others may have single cell datasets from species that aren’t in the paper. 
      Having a reliable means to pool those together would really help others. 
      This may include people working animals that don’t have a VCF file available…
      those people can’t use the vireo script now 
      (which is most people because VCF files are only available for well studied organisms). 
      Really appreciate your help on this!
  ```

--------------

**[[ZEN]](ZEN_project) Zenodo**

* Discussions with Jose to find the best way to publish on Zenodo
  * Converged that the best way for this one is to create a workflow that contains both code and data
* Discussions with Arianne and Laurel to find the best way to publish on Zenodo
  * Converged on publishing the most relevant dataset (to be identified) and part of the code to reproduce the main figures

--------------

**[[ZF]](ZF_project) Z-Fishator**

* Found out that there is already a 2TB (unmounted) disk on z-fishator, no need to buy one
* Continue with machine configuration with setting up specific environments for all users
* Thinking about connecting the machine to the HIVE
  * Need to investigate the possibility and need to physically connect the HIVE and Z-Fishator linux machine with optical fiber
