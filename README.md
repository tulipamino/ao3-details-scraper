# ao3-details-scraper

The script ao3.py appends the details of an ao3 work to a csv. 

Dependencies:  
- requests
- beautifulsoup4

1. Navigate to the ao3 page that contains the work you would like to add to the csv, and copy the URL.
2. In the command line navigate to the directory containing the program. 
3. Run the program with command: python ao3.py <URL> <path_to_csv>
	where the <URL> is the URL of the ao3 work, and <path_to_csv> is the location of the csv you want to create or add to.

Example: `python ao3.py https://archiveofourown.org/works/42927006 myReadingList.csv`
	
- The example command will append the details of the ao3 work to myReadList.csv located in the same directory
