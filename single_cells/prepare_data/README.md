# Prepare the data

## On the Nikon acquisition machine

Once your movie is finished, it needs to be copied on the `nas-rcp` central storage. For that you need to prepare a folder named after your `raw-dataset` name that you want in the `raw-data catalog` , and that contains: 
* the un-split `.nd2` movie
* a folder per well `well1, well2, etc...`, each of containing all the split `.nd2` positions. 
* the two above should be located inside `E:\File_transfer`
For example, let's assume I have an experiment named `wscepfl0113` that contains 4 wells, each of them a different number of positions, the folder structure inside `E:\File_transfer` should look like:

```
├── wscepfl0113
│   ├── wscepfl0113.nd2
│   │   ├── 
│   ├── well1
│   │   ├── wscepfl0113_xy001.nd2
│   │   ├── wscepfl0113_xy002.nd2
│   │   ├── ...
│   │   ├── wscepfl0113_xy032.nd2
│   ├── well2
│   │   ├── wscepfl0113_xy033.nd2
│   │   ├── wscepfl0113_xy034.nd2
│   │   ├── ...
│   │   ├── wscepfl0113_xy071.nd2
│   ├── well3
│   │   ├── wscepfl0113_xy072.nd2
│   │   ├── wscepfl0113_xy073.nd2
│   │   ├── ...
│   │   ├── wscepfl0113_xy107.nd2
│   ├── well4
│   │   ├── wscepfl0113_xy108.nd2
│   │   ├── wscepfl0113_xy109.nd2
│   │   ├── ...
│   │   ├── wscepfl0113_xy131.nd2
```

Once this structure is ready, open the notebook, and change the `src` to point to where the data to copy is located. In this example `E:\File_transfer\wscepfl0113`. Then execute the cell that contains it, in our example:
```python
src=r'E:\File_transfer\wscepfl0113'
```

Then you can proceed with copying the files by executing the cell:

```python
copy_files_with_verification(src, dest)
```

You should immediately see something like this printed:
```shell
exp_name,  wscepfl0113
```

It is copying the full movie, taking some time. Once the copy is over, you will see something like:

```shell
File copied successfully and checksums match for wscepfl0113.nd2
```

Then the copy of individual positions for each well will start and you will see something like:

```shell
dir =  well1
src_file_path   E:\File_transfer\wscepfl0113\well1\wscepfl0113_xy001.nd2
dest_file_path  Z:\raw_data\microscopy\cell_culture\wscepfl0113_well1\raw_files\wscepfl0113_xy001.nd2
File copied successfully and checksums match for wscepfl0113_xy001.nd2
...
...
dir =  well2
src_file_path   E:\File_transfer\wscepfl0113\well2\wscepfl0113_xy033.nd2
dest_file_path  Z:\raw_data\microscopy\cell_culture\wscepfl0113_well2\raw_files\wscepfl0113_xy033.nd2
File copied successfully and checksums match for wscepfl0113_xy033.nd2
...
...
dir =  well3
src_file_path   E:\File_transfer\wscepfl0113\well3\wscepfl0113_xy072.nd2
dest_file_path  Z:\raw_data\microscopy\cell_culture\wscepfl0113_well3\raw_files\wscepfl0113_xy072.nd2
File copied successfully and checksums match for wscepfl0113_xy072.nd2
...
...
dir =  well4
src_file_path   E:\File_transfer\wscepfl0113\well4\wscepfl0113_xy108.nd2
dest_file_path  Z:\raw_data\microscopy\cell_culture\wscepfl0113_well4\raw_files\wscepfl0113_xy108.nd2
File copied successfully and checksums match for wscepfl0113_xy108.nd2
...
...
```

When it's done, please check the summary number of files copied and that failed:
```shell
Total files copied: 132
Total files failed: 0
```


For this example experiment `wscepfl0113` the total number of files copied should be equal to the total number of positions + 1 (un split movie), thus 132. Take actions in case the expected number of files differs from the files copied or is files failed to be copied.

## On your laptop


### Register

Once the data is copied to the `nas-rcp` you need to trigger the registration to the `raw-data catalog`. Using you favorite web browser open the [raw-data catalog](http://sv-upoates.epfl.ch:8000/rawdata_catalog/rawdatasets/) and click on `Register`. After ~10 seconds the page will reload and the new raw-datasets should appear. 

### Fill the admin part of the raw-data catalog

After the registration in the `raw-data catalog` is done, you can login to the [admin](http://sv-upoates.epfl.ch:8000/admin/) page, fill the relevant metadata for all your datasets:
* Click on `Experimental conditions`, filter based on your experiment name, click on each `Experimental conditions` individualy corresponding to your raw-dataset and edit them one by one. Don't forget to change `Fill` status to `True` when done. Don't forget to click on `Save`

* Click on `Experiment` and `ADD EXPERIMENT` to right corner. Fill the relevant field for you experiment, pay attention to the name that should correspond to the one of the folder you created on the Nikon acquisition machine and that is the experiment name in the `nas-rcp` where the unsplit file is located. The tag `SegmentMe` should be selected such that the raw-dataset could be segmented. Don't forget to click on `Save`

* Click on `Experimental datasets`, filter based on your experiment name, click on each `Experimental dataset` individualy and select the `Experiment` they correspond to. Don't forget to click on `Save`.

## On the HIVE

The single cell application runs on HIVE3026, thus you need to connect using the remote desktop application.

### Register single cell experiments to single cell database

It is now possible to register all the new raw-datasets to the single cell database. To do so, login to the  [single cell application](http://127.0.0.1:8001/segmentation/), and click on `Register raw datasets (build frames)`. After ~30 seconds the page will reload and the new raw-datasets should appear in the dropdown menu `--Choose an experiment--`.

### Build the ROI and detect the cells

To build the ROI and detect the cells, select the experiment in the left dropdown menu  `--Choose an experiment--`. Make sure it is properly selected by checking the metadata associated to the experiment displayed at the bottom. Then click `Build ROIs (sample)` at the bottom of the page (Note, you do not need to choose a well for the building the ROIs). This will take ~10 minutes (depending on the number of positions) to process all the positions of your experiments. You know when this is over when the page has finished to reload. When it is finished, you can open the [single cell dashboard](http://127.0.0.1:8001/segmentation/bokeh_dashboard) and look at your experiment, or the [summary dashboard](http://127.0.0.1:8001/segmentation/bokeh_summary_dashboard). On the single cell dashboard there is a plot of predicted time of death, that does not appear yet on the summary dashboard.



