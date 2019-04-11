## Lesson 0: 

 1. # Installation
	
	See Milo [post](https://milo.sgh.com/community/software/blog/2019/02/15/abaqus-2019-is-available-and-some-thoughts-on-software-versions).
	
	Our current license server for Abaqus is: 27000@nastran2006
	
 2. # Running jobs
 
	On the command prompt, type:
	
	abaqus job=XXXX cpus=N interactive
	
	where XXXX is your jobname, i.e., the filename of the input file without the *.inp extension. By default, if you ignore the option "cpus=N", you will use N=1.
	
 3. # Batch files
 
	You may also batch your job if you put this command in a batch file:
	
	call abaqus job=XXXX cpus=N interactive
	
	All other windows commands can be used in this batch file (e.g., changing directories, copy or move files, etc.) so that you can automate the running of multiple input files.
	
 4. # Check license availability
 
	Put the following two lines in a batch file (e.g., check_abq_license.bat):
	
	"\\nastran2006\nastran2006_c\SIMULIA\License\lmutil.exe" lmstat -c 27000@nastran2006 -a >"%temp%\status.txt" 
	notepad "%temp%\status.txt"

	When you double-click the batch file, a notepad file will pop up to show you the number of licenses that are available.
	
	You may also check license availability by going to:
	
	http://alf.sgh.com/
	
	Scroll all the way down to find "Software License Usage".