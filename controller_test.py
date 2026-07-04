from nxbt import Nxbt, PRO_CONTROLLER, Buttons

nx = Nxbt()
index = nx.create_controller(PRO_CONTROLLER)
print("Go to Change Grip/Order screen")
nx.wait_for_connection(index)
print("CONNECTED")