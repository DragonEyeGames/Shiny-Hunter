from nxbt import NXBT

nx = NXBT()

index = nx.create_controller(nx.PRO_CONTROLLER)

print("Go to Change Grip/Order screen")

nx.wait_for_connection(index)

print("CONNECTED")