<h1> Documentation  </h1>

<h3>Project name: </h5>

* Software Developer Intern - Technical task 



<h3> Requirements </h3>

* Pandas 1.2.3
* Numpy 1.21.2
* Matplotlib 3.3.4
* googlesearch
* serpapi
* Jupyter Notebook 6.3.0

<h3> Installation </h3>

```
pip install pandas

pip install numpy

pip install jupyter

pip install matplotlib

pip install googlesearch

pip install serpapi

pip install jupyter
```
<p>After the installation you can open task_2.py task_3.ipynb<br>
     <br> task_1  doesn't require any additional program 
</p>

<h3> Description </h3>

<h4>Task 1 </h4> 
<p>a) Please describe your experience with one of the following areas:
- Python
- SQL
- Wordpress
- Web development
- Data science  </p>

<h4> Task 2 scraping the “site” command (optional) </h4>
<p>You can use a technology of your choice, but we prefer scripts written in Python as this is the
main technology we use in our applications.

Algorithm is as follows:
1. The program is looping through a list of keywords in the .txt file (keywords.txt)
2. Then it queries Google.com using the following set of queries:
a. site:https://www.searchenginejournal.com/ {keyword}
3. For every query, the program  goes through Google Search Results and extracts all the
links pointing to SearchEngineJournal. We need extractions only from the first page
of results but if you can get more, it would be a good addition.
4. We also want the total number of results (the number above the first result) to be
extracted </p>
5. The program saves all the links pointing to SearchEngineJournal to a CSV file.
6. The total numbers of results should be saved in a different file along with the associated
keyword

What’s needed?
- Program source code - we don’t need a compiled application.
- Short documentation on how the program works (in English) including description of
functions/classes (this might be added as comments in your code).
- Ideas on how the software can be improved in the future.
- Are there any risks associated with using such a program?
- The program doesn’t need to solve captchas.

<h4> Task 3: 120 Years of Olympic History data analysis
(optional) </h4>

<p>We would like to analyze the dataset containing information about the Olympics.

The dataset is available here:
https://www.kaggle.com/mysarahmadbhat/120-years-of-olympic-history

Questions to answer:
- What countries receive the most medals nowadays? Does it change much across the
timespan?
- Who wins the most medals? Women or men?
- What’s the trend for the number of participants?
- What is the relation between age and medals won?
- Do tall people win more medals?
- Which sports are dominated by short people? (You must define "short")
- Which families (same surname) win the most medals?</p>

Requirements:
- Software you use is up to you. You can use Excel, Jupyter Notebook, Tableau, R,
Python, MS Power BI or any software of your choice.
- Write a short summary in English.


<h3> Usage </h3>

<h4> Task 2 </h4>

<p>
After the installation we can easily run task_2.py

Then: 
* Create object of a class ScrappingTheSiteCommand() and as a parameter we need to give name of a csv file.
* Using the instance, run function loop_through_file()
* Using the instance, run function google_search()
* Define variable and assign to it the output from preparing_url_results() 
* Use save_file_to_csv() static method to save results of urls in the csv file as a parameter use formerly defined variable
* Define variable and assign the output from preparing_total_results_csv()
*  Use save_total_results_to_csv() static method to save total results in the csv file, as a parameter use formerly defined variable

<h4> Task 3 </h4>
<p> In terminal run: </p>

```
jupyter notebook
```

<p> Run task_3.ipynb inside jupyter notebook
<br><br>

To see the results you need to:
* Click Kernel option
* Click 'Restart & Run All'
* Click Restart and Run All Ceils

Now you can see the answer to each question.


</p>

