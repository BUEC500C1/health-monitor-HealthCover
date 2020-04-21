# HEALTHCOVER

## Team Members
- Sensor module: Zhou Fang
- Database module: Yingqi Zhang
- Alert module: NingrongChen(noracnr@bu.edu)
- Display module: Yanyu Zhang(zhangya@bu.edu)
- Prediction module：Luxuan Qi
- Integrate: Yufeng Lin

## Product Definition

### Project Mission
- In order to help hospitals and patients get their health infromation, our aim is to design a health monitor named "HEALTHCOVER". 
- The HealthCover can receive the health information from different sensors and send to the central processor. The processor can make a prediction based on the linear regression and send a warning if the patients have a dangrous in the future. 

### Users
- Hospitals
- Patients

### User story
- As a user, I want to see my patient’s pulse on configurable time intervals (e.g., 10 minutes)
- As a user, I want to see my patient’s blood pressure on configurable time intervals (e.g., 10 minutes)
- As a user, I want to see my patient’s blood Oxygen levels on configurable time intervals (e.g., 10 minutes)
- As a user, I want to get alerts if any of the Vitals go above and/or below certain value.
- As a user, I want to get future prediction based on an AI module we have purchased and should be integrated into the system.
<p align="middle">
  <img src= "https://github.com/BUEC500C1/health-monitor-HealthCover/blob/master/graph.png">
</p>


## Method and Solotion
### Sensor module:
### Database module:
### Alert module:
<a href="https://github.com/BUEC500C1/health-monitor-HealthCover/blob/master/Alert/README.md">Click here to Alert README</a>
### Prediction module:
### Display module:
- In order to display all the patient's information and set an alarm for the alerts, I used a very useful Python tools: QT. PyQt is very useful tool to develop a cross-platform and it uses the system's resources to draw windows, controls, etc so your application will get a native look.

- Qt is open source and is developed by the Qt Group (formerly Trolltech) at Nokia so you have a very large enterprise maintaining it with the support from the community and ensuring it's evolution.

- It has the best GUI designer I've ever seen.

The result is showing below:
<p align="middle">
  <img src= "https://github.com/BUEC500C1/health-monitor-HealthCover/blob/master/Display/health_monitor.png" width= 500>
</p>

### Integration:
```
git clone https://github.com/BUEC500C1/health-monitor-HealthCover.git
```
"cd" to the Integrated folder and then 
```
python main.py
```
And you can see the following example result: <br/>
Green box: example of NORMAL state (Default is NORMAL) <br/>
Red box: example of WARNING state <br/>
Yellow box: example of prediction of future parameters <br/>
![res](https://github.com/BUEC500C1/health-monitor-HealthCover/blob/master/run.png)



