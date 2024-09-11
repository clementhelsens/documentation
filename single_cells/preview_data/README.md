# Preview the data

## jupyter-lab is running

To pre-screen the `.nd2` movie you just acquired, a simple tool can be executed. It will open a browser window with an image example and the intensity trace for all the positions in the file. To achieve this open the notebook `Demo_preview` in the `notebooks` folder, change the `file` to point to your own file, and execute the cell. It will take 1-2 minutes to process and then will open an other browser window, it will take an other minute ot two to load the page 2-3 mins depending on the number of positions you have.

## jupyter-lab is not running

If `jupyter-lab` is not working, you need to launch it first. To do so open the `Anaconda Prompt` application (search for `Anaconda` in the bottom left search bar). In the prompt window, type 

```shell
cd software\singlecells_notebooks
```

and then:

```shell
conda activate django_seg_sam
```

once the environment is activated, the prompt line should have changed to `(django_seg_sam) C:\Users\Laurel\software\singlecells_notebooks>`.

Finally, launch `jupyter-lab` from the prompt (simply type `jupyter-lab` and press enter). A browser window will open with the notebooks, then follow [jupyter-lab is running](#jupyter-lab-is-running)