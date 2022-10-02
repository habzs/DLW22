# UnrealHawker DLW2022


## Problem Statement
Finding seats at a hawker is always a challenge, especially during peak periods. In all likelihood, you have to physically go down and visually check if there are any seats at all. This would in turn waste time on finding space (especially for people with limited lunchtime). What if there was a convenient way to check if there are seats at a hawker and where it might be?

## Solution
Using computer vision, we can identify if a table is taken based on imagery. This system allows patrons to view the occupancy of tables in hawker centres in real time and locate vacant seats via the dashboard located on the hawker centre television screen.

## Elaboration Hardware/Software 
Most hawker centres are already equipped with cameras. Training the dataset based on the current CCTV video feed would be simple. If not enough data is available, Computer Simulated data can be used to supplement. Once trained, the model could be run on a remote server to update the web app.

## System Process 
After identifying the plates via object detection, the web app would update in real-time with accordance to the status of the table.

## Main Selling Points
UnrealHawker does not need any additional hardware parts. It taps into existing infrastructure that is available at hawker centres. Additionally, the television displays at hawkers can also be used to display the vacancy of the tables UnrealHawker would enable patrons to check the availability of the hawker centre before physically going down, thus optimising their lunch hour. The screens around hawker centres would also further aid them in finding empty tables which improves their dining experience by reducing the effort and time needed for them to find an empty table.
Apart from that, the screen displays would also allow non-smartphone users, seniors for example, to view the table vacancy of the hawker centre.

## Flow of Events
![IMG](https://raw.githubusercontent.com/habzs/DLW22/main/images/flow.png)

## Unreal Engine 5: Training Models Using Photorealistic Simulation for Fast Implementation
![IMG_1](https://raw.githubusercontent.com/habzs/DLW22/main/images/unreal1.png)
![IMG_2](https://raw.githubusercontent.com/habzs/DLW22/main/images/unreal2.png)

# Implementation
## Computer Vision Model
We created a dynamic model that tracks both plates, clutter, cups & tables, and connects the information to determine the vacancy of a table. This was implemented through openCV. If the hawker owner chooses to move tables around, our model will still be able to track correctly and accurately provide the required data

## Unreal Engine 5 (UE5) Simulations
By creating a fully configurable environment in UE5, we can train our models without the need to feed it real-world images. Furthermore, we can dynamically move user controlled actors to interfere with the environment, simulating real-life circumstances </br>
![Position](https://raw.githubusercontent.com/habzs/DLW22/main/images/position.gif)
![Moving](https://github.com/habzs/DLW22/blob/main/images/moving.gif)

https://github.com/habzs/DLW22/blob/main/images/moving.gif
![IMG_3](https://github.com/habzs/DLW22/blob/main/images/image.png)



## Internet-Of-Things through Responsive Websites
Additional sensors (pressure, ultrasonic) could be used to assist in more accurate vacancy data. Implementation and iteration is simple through Progressive Web Applications. We can directly update the results of our Model to users online. This enables users to make informed decisions based on our findings. Such models can also be configured and tested using UE5.

## Getting Started 
UnrealHawker makes use of the following libraries 
- openCV
- mss
- Pillow
- Firebase
- Node.js and Material Design Bootstrap
- Unreal Engine 5

```
sudo pip install opencv
sudo pip install mss
sudo pip install pillow
sudo pip install firebase-python
sudo pip install nodejs
```

## Usage
Start by running the camWithCalibration.py. Point the virtual camera toward the scene.
- Press 'C' to start calibrating the tables.
- Plates and cups will begin to detect.
- Press 'q' to exit program.

# Contributors
🗿 [Owen Lee / habzs](https://github.com/habzs)

🐔 [Ryan Goh / Gyanroh](https://github.com/Gyanroh)

🐓 [Kai / SlothKai](https://github.com/SlothKai)

🌗 [Ryan Phoen / rphoen](https://github.com/rphoen)
