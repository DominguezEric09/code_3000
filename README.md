# code_3000
Collection of Assignments for CSE 3000: Contemporary Issues in Computer Science and Engineering

_Note_: Odd-numbered assignments are in HuskyCT, while even-numbered assignments are found in this repo and can be submitted to Gradescope via a Github connection.

## Outline of Assignments

### Module 02: Bot Predictor
Your goal is to build a machine learning model using given data and a Python template. You'll make changes to the GradientBoostingClassifer in mod02_build_bot_predictor.py and then test your changes in mod02_test_bot_predictor.ipynb. Can you minimize the misclassification rate on the test set?

### Module 04: Model Bias
You are given a model that was built to predict a mystery variable using zip code, income, and education level. The variable "group" represents a demographic that is prohibited and was NOT used in the model. Your goal is to use the SHAP package to review this model for bias.

### Module 06: Data De-Anonymization
Your goal is to connect anonymized data back to its source data and check the match rate. To complete this activity, write functions in the "deanonymize" script to (1) link the records in the two datasets and (2) calculate the rate at which you are successful doing so. 

### Module 08: Sustainability in Computing
You will be given a toy dataset and have the opportunity to explore the potential effects of choosing sustainable energy sources to perform computations. You'll code the energy calculation in "sustainability calculations" script, and then you can review the results of various decisions in the "check calculations" notebook. 

## Personal Statement on Ethics 
After reading Chapter 5 of Ethical Machines, I believe an ethics statement is only real if there is genuine feeling and care behind the words, not just polished wording. A company can say it values fairness, but if the people writing it don’t care about the people affected, the statement is only for show. In Homework 4, I saw how a model that never used the group variable could still treat groups differently, which showed me that technical claims about fairness can hide real harm to real people. For me, ethics starts with the creative intention behind what I make. I ask why I’m making it, who it affects, and whether I truly care about them. When I build things, I want my work to come from that heart, and I want the people it reaches to feel that care.