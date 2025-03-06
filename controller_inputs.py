from inputs import get_gamepad
from inputs import devices


for device in devices:
    print(device)


#ABS_Y, ABX_RY, ABS_Z, ABS_RZ, BTN_START
inputs_list = {"ABS_Y" : 0, "ABS_RY" : 0, "ABS_Z" : 0, "ABS_RZ" : 0, "BTN_START" : 0}

def return_controller_inputs():
    """
    Reads the gamepad inputs and updates the inputs_list dictionary
    with the current state of the controller's buttons and axes.
    """
    # Get events from the gamepad
    events = get_gamepad()
    # Update the inputs_list with the event states
    for event in events:
        if event.code in inputs_list:  # Only update if the event code exists in the inputs list
            inputs_list[event.code] = event.state

    print(inputs_list)
    return inputs_list
#return_controller_inputs()
