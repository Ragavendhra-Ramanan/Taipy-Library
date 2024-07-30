# import necessary libraries
import taipy as tp
from taipy import Config
from taipy import Core

#STEP 1 : Configure Taipy Application

# Define the build_message function which is called during task execution
# This method takes input data node and provide result in output data node
def build_message(name: str):
    return f"Hello {name}!"

# define the input data node configuration
name_data_node_cfg = Config.configure_data_node(id="input_name")

# define the output data node configuration
message_data_node_cfg = Config.configure_data_node(id="message")

# define the build_message task configuration which takes build_message function  
build_msg_task_cfg = Config.configure_task("build_message", build_message, name_data_node_cfg, message_data_node_cfg)

# define the scenario configuration which takes the task to be run.
scenario_cfg = Config.configure_scenario("scenario", task_configs=[build_msg_task_cfg])


#STEP 2 : Create Taipy Application and Run the Scenario

if __name__ == "__main__":
    Core().run()

#STEP 3 : Create Scenario and accessing data 

#create a specific scenario using scenario configuration which we created above
ipl_scenario = tp.create_scenario(scenario_cfg)

# write data to the input data node of the scenario using id
ipl_scenario.input_name.write("Dhoni")

# submit the scenario to run
ipl_scenario.submit()

# once the scenario has been run we can the see the output message which we got by executing the task under defined under the scenario
print(ipl_scenario.message.read())