## Data Analytics Portfolio

---

### Machine Learning with R 

- [TOPIC MODELING OF BBC NEWS USING LATEND DIRICHLET ALGORITHM (LDA)](/pdf/Project 4.pdf)  
The objectives of this report were as following:  
• Collect and preprocess a dataset of BBC news articles.  
• Apply the LDA algorithm to the preprocessed dataset and identify the main topics covered by the BBC news.  
• Evaluate the quality of the topic modelling results by measuring smoothness and accuracy.  
• Identify the most relevant keywords for each topic, analyze the semantic meaning of each topic, visualize it with the help of word clouds.  
• Provide insights and recommendations for businesses and researchers based on the findings of the topic modelling analysis.   
 
<img src="images/pic20.jpg?raw=true"/>
<img src="images/pic31.jpg?raw=true"/>

---    


- [PREDICTING LETTER PATTERNS IN ENGLISH WORDS USING HIDDEN MARKOV MODEL](/pdf/Project 3.pdf)  
The objectives of this report were as follows:  
• To provide an overview of Hidden Markov Models and their application in predicting letter patterns in English words, including its mathematical foundations.  
• To outline the methodology for building and training an HMM for letter pattern prediction.  
• To evaluate the performance of the HMM in predicting letter patterns in English words, including alternative methods for comparison.  
• To discuss the potential benefits and applications of using HMMs for letter pattern prediction in various industries including its limitations.  
• To provide recommendations for further research and development in this area.    

<img src="images/screen 1.jpg?raw=true"/>
<img src="images/screen 32.jpg?raw=true"/>  

---  




- [DIAGNOSING BREAST CANCER WITH A KNN ALGORITHM](/pdf/Project 1 - Diagnosing Brest Cancer by Kirill Samaray.pdf)  
The purpose of the project was to use machine learning algorithms in helping patients and clinics to identify cancerous cells. By automating the process of detection, it may reduce the time spent on examining the cells by a doctor and potentially could provide a better accuracy due to eliminating a human factor since some healthcare specialists might potentially make mistakes while diagnosing. The algorithm chosen for this project was kNN. With the help of this algorithm the computer studied the biopsied cells from both of the genders in order to identify cancer.  


<img src="images/project 1 crosstable.jpg?raw=true"/>
<img src="images/project 1 tables comparison.jpg?raw=true"/>



---


- [SPAM DETECTION USING NAIVE BAYESIAN ALGORITHM](/pdf/Project 2 - SPAM Detection by Kirill Samaray.pdf)  
The number of spam message in the modern world is significantly growing each year which can result in potential cyber security breach, loss of time and resources. The task of spam messages detection is becoming of a paramount importance in the wake of growing amount of data transferred through the Internet or via the mobile phones. The constant inundation of unsolicited messages online has caused a disruption in the digital world and has made it difficult to identify genuine messages out from the commercial spam or malicious malware. Filtering the messages and protecting people from spam can considerably change the ecosystem of email correspondence and bring more integrity into the system. Thus, introducing an effective algorithm capable of dissecting and classifying spam and genuine SMS messages should help people and organizations to maintain their efficiency levels and stay protected from scam.  


<img src="images/visualizing 1.jpg?raw=true"/>
<img src="images/algorithm 1.jpg?raw=true"/>


---

### SQL Projects

- [ADVANCED ERD CONVERSION]  

<img src="images/SQL 1.png?raw=true"/>  


- [WRITING SQL STATEMENTS]    

<img src="images/SQL 2.jpg?raw=true"/>  

-Find top 2 largest departments in terms of number of employees  

select * from (select deptno, count (ename) from emp group by deptno order by count(ename) desc)  
where rownum < 3;  

-Create a list of employee names and also their supervisor names if an employee has a manager  

select d.ename as Employees, cursor(select e.ename from emp e where e.empno=d.mgr)    
as Supervisors  
from emp d;  

-Create a list manager names and also his supervise names if the manager has any one  

select d.ename as Managers, cursor(select e.ename from emp e where e.mgr = d.empno)  
as Supervisees  
from emp d where job = 'MANAGER';  

-Find a random department and the total number of employees in the department  

select count(ename), deptno  
from emp where deptno = (select deptno from (select deptno from emp order by dbms_random.value)  
where rownum<2) group by deptno;  



---

### JMP Projects

- [HIERARCHICAL CLUSTER ANALYSIS]  


Data file: Lab6_Beer Data.jmp  
Used a Standardize data and Centroid method to run Hierarchical Cluster Analysis
with all four continuous variables as dependent variables & Brand as label.  

  Findings  
  Summary tables with Mean values for the ingredients was identified. Each cluster was interpreted accordingly. K-means cluster analysis was run with all four         continuous variables. The values of Cluster Cubic Criterion were identified.   

<img src="images/JMP 1.jpg?raw=true"/>
<img src="images/JMP 2.jpg?raw=true"/>

---

- [DECISION TREE ANALYSIS] 


Data File: Lab5_Credit Card Marketing.jmp  
A bank would like to understand the demographics and other characteristics associated with whether a customer accepts a credit card offer. Observational data is somewhat limited for this kind of problem, in that often the company sees only those who respond to an offer. To get around this, the bank designs a focused marketing study, with 18,000 current bank customers. This focused approach allows the bank to know who does and does not respond to the offer, and to use existing demographic data that is already available on each customer. 

  The designed approach also allows the bank to control for other potentially important factors so that the offer combination isn’t confused or confounded with the     demographic factors. Because of the size of the data and the possibility that there are complex relationships between the response and the studied factors, a         decision tree is used to find out if there is a smaller subset of factors that may be more important and that warrant further analysis and study.

  The Task   
  You want to build a classification model that will provide insight into why some bank customers accept credit card offers and others don’t. Because the response is   categorical (either Yes or No) and we have a large number of potential predictor variables, we use the Partition platform to build a Decision Tree for Offer         Accepted. We are primarily interested in understanding characteristics of customers who have accepted an offer, so the resulting model will be exploratory in         nature.

  Findings  
  A Decision Tree analysis was performed with ‘Offer Accepted’ as the dependent variable, all other variables (except Customer Number) as independent variables and     ‘Validation’ as   Validation column. The ideal number of splits was identified, sensitivity and specificity rates for Validation set were determined, rules of probability were found, prediction profiler was visualized.  
  
  <img src="images/JMP 3.jpg?raw=true"/>  
  
---

- [REGRESSION ANALYSIS AND NEURAL NETWORK]  

Performed correlation analysis & interpreted results to discover how the variables were correlated. Performed a simple linear regression analysis & interpreted the results such as p-value, R-square, residuals, and regression analysis. Performed a stepwise multiple regression analysis and interpreted the results such as VIF, residuals, profiler, and regression equation. Performed Neural Network and compared its results with Multiple Regression analysis.  


<img src="images/JMP 4.jpg?raw=true"/>  


---
<p style="font-size:11px">Page template forked from <a href="https://github.com/evanca/quick-portfolio">evanca</a></p>
<!-- Remove above link if you don't want to attibute -->
