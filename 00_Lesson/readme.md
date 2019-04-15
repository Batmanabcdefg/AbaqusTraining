# Lesson 0: Administrative

## Installation

See Milo [post](https://milo.sgh.com/community/software/blog/2019/02/15/abaqus-2019-is-available-and-some-thoughts-on-software-versions).

Our current license server for Abaqus is: 27000@nastran2006

## Abaqus documentation

You will very likely need to find certain information in the Abaqus documentation. You can choose to install the Abaqus Documentation during software installation. Alternatively, you can find the latest Abaqus documentation here:

https://www.3ds.com/support/knowledge-base/

You need to sign up for access.

## Checking license availability

Put the following two lines in a batch file (e.g., check_abq_license.bat):

	"\\nastran2006\nastran2006_c\SIMULIA\License\lmutil.exe" lmstat -c 27000@nastran2006 -a >"%temp%\status.txt" 
	notepad "%temp%\status.txt"	

When you double-click the batch file, a notepad file will pop up to show you the number of licenses available.

You may also check license availability by going to:

http://alf.sgh.com/

Scroll all the way down to find "Software License Usage".

## Coordinating software needs

We communicate our license needs on Slack:

## Running jobs

On the command prompt, type:

	abaqus job=XXXX cpus=N interactive

where XXXX is your jobname, i.e., the filename of the input file without the *.inp extension. By default, if you ignore the option "cpus=N", you will use N=1.

## Batch files

You may also batch your job if you put this command in a batch file (e.g., run_all.bat):

	call abaqus job=XXXX cpus=N interactive

All other windows commands can be used in this batch file (e.g., changing directories, copy or move files, etc.) to automate the running of multiple input files.

## Pre- and post-processing of models

We typically use the pre-post software FEMAP for defining model geometry and meshing. A basic Abaqus input file is then generated on which we further modify manually. FEMAP tutorials can be found in the FEMAP documentation.

For post-processing, we typically use Abaqus Viewer. To start Abaqus Viewer, type on the command prompt:

	abaqus viewer

For post-processing using Python scripts for output database (ODB) acess, type on the command prompt:

	abaqus python XXXX

where XXXX is the name of the Python script (including the extension .py)
	
For post-processing using Python scripts that invoke Abaqus Viewer for generating plots, type on the command prompt:

	abaqus viewer script=XXXX

where XXXX is the name of the Python script (including the extension .py). 

Simple examples of results visualization and querying are described as you work through the lessons here.
