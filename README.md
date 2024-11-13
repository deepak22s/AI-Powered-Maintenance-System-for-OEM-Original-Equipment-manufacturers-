# AI-Powered Maintenance System for OEM(Original Equipment manufacturers)

   **Note:** This repo only contains the project details,Files and codes of the Datascience process of the  AI-Powered Maintenance System for OEM(Original Equipment manufacturers).
 
----
## Problem Statement:

- The current vehicle maintenance model operates on either scheduled or reactive maintenance. In scheduled maintenance, vehicles are serviced after a fixed period, regardless of the actual condition of the vehicle parts. This leads to inefficiencies such as replacing parts too early or missing critical failures, resulting in unexpected breakdowns. Reactive maintenance, where repairs happen only after something has failed, often leads to higher repair costs, vehicle downtime, and customer dissatisfaction.
- **Original Equipment Manufacturers (OEMs)** are seeking innovative methods to overcome these challenges by predicting and preventing vehicle failures before they occur. The goal is to minimize unscheduled repairs, reduce maintenance costs, and improve vehicle reliability, safety, and overall customer satisfaction.
![Screenshot 2024-11-13 192630](https://github.com/user-attachments/assets/ede3df97-416b-4a54-af1b-c57801c8fae4)

----
## Solution: AI-Powered Predictive Maintenance

This system uses AI and IoT (Internet of Things) to predict when a specific part of a vehicle might fail, allowing for maintenance to be done before issues arise. It achieves this by continuously collecting and analyzing real-time data from vehicles.
![image](https://github.com/user-attachments/assets/fecd3c70-8d12-4148-b7b6-a9e0dc81e29b)




## Key Features:

- Real-Time Data Collection
- Machine Learning Algorithms
- Cloud-Based Dashboard for OEMs
- Driver Alerts via Mobile App

**Value Proposition with the solution:**

![2](https://github.com/user-attachments/assets/5300724b-d5f0-4c8c-b45e-2d0de13cf949)

1. **For OEMs:**
o	Reduced Costs: By fixing issues before they turn into expensive repairs, OEMs can save money on warranty claims and emergency fixes.
o	Improved Reliability: Vehicles that break down less often enhance the OEM's reputation, helping them sell more cars.
o	Better Vehicle Design: OEMs can use data from vehicle performance to improve the design of future models.
o	Efficient Maintenance: The system helps OEMs manage repairs more effectively, knowing exactly which parts need replacing and when.
2. **For Drivers:** 
o	Fewer Breakdowns: The system prevents unexpected vehicle failures, ensuring drivers don’t get stranded on the side of the road.
o	Lower Costs: Maintenance is only performed when necessary, avoiding early part replacements or expensive emergency repairs.
o	Improved Safety: By keeping the vehicle in top condition, the risk of accidents or safety issues from component failure is reduced.
o	Easy Maintenance Scheduling: Drivers can easily schedule repairs through the mobile app, making the process more convenient and stress-free.


### Dataset/Real-Time Data Collection

- Its hard to get a realtime data of vehicles  from the Internet hence we dont have any access to such data we have decided  to get the data from kaggle this data are seems real and very accurate to the real world generated data.
- As with the real time data we can build the datapipe line using cloud and fleet management.

The dataset contains following columns:
- ---  ------            --------------  -----  
- 0   Engine rpm       
- 1   Lub oil pressure
-  2   Fuel pressure     
- 3   Coolant pressure
- 4   lub oil temp      
- 5   Coolant temp     
- 6   Engine Condition  

### Machine Learning Algorithms

- **Model Training & Evaluation:** It trains several classification models including Decision Tree, KNN, XGBoost, Random Forest, Logistic Regression, GaussianNB, RidgeClassifier and ExtraTreesClassifier.
- **Performance Metrics:** Performance evaluation is done using various metrics like accuracy, precision, recall, F1 score, MCC, FPR, FNR, NLR, PLR, and ROC AUC.
- **Visualization:** Confusion matrices and ROC curves are plotted to visualize the model performance and aid in the interpretation of the results.


### Cloud management
- Move data processing and model inference to a cloud-based infrastructure.
-	Ensure scalability, data security, and real-time processing capabilities for the application


### Mobile application
-  Driver and Fleet App Development
- Develop or integrate the solution into a driver-facing or fleet management app.
- Create a user-friendly interface for visualizing data, alerts, or actionable insights derived from the model.



### Usage

Instructions on how to run the project:

1. This project is just a prototype for the datascience process of AI-Powered Predictive Maintenance System so the file only contains a jupyternotebook.
2. You can directly download the Jupyter notebook and use it. 
### Results

- Mentioned at the end of Jupyternotebook in the repo


### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
