# turtlebot_twist_mux
In this project we are controlling a default turtle robot with two different controls one is using teleop keyboard other is a random mover which gives random velocity commands.

# How to use this ros 2 package
- create a workspace <br>
  `mkdir -p ~/test_ws/src`<br>
- Change the directory to src<br>
  `cd ~/test_ws/src`<br>
- clone this repo <br>
  `git clone https://github.com/amitonlinepro/turtlebot_twist_mux.git`<br>
- Build the workspce<br>
  `cd ~/test_ws` <br>
  `colcon build`<br>
- Source the workspace<br>
  `source ~/test_ws/install/setup.bash` (if you are using bash shell)<br>
  `source ~/test_ws/install/setup.zsh` (if you are using zsh shell)<br>

  Now You are ready to run
  - Open four terminal windows
  - In Window 1:<br>
    - `source ~/test_ws/setup.bash`
    - `ros2 run turtlebot_twist_mux random_mover`
  - In Window 2:<br>
    - `source ~/test_ws/setup.bash`
    - `ros2 run turtlebot_twist_mux twist_mux`
  - In window 3:<br>
    - `ros2 run turtlesim turtlesim_node`
  - In window 4:<br>
    - `ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap /cmd_vel:=/teleop/cmd_vel`
   
  You Will obserbe That by default turtle robot is running from the velocity commands coming from random mover and when you send the command using teleop_twist_keyboard if follows this and 
  after you stop giving command using this method it goes back to random mover.
