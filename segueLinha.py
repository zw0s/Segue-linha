def control(left_sensor, right_sensor, speed):
    
    calibragem= right_sensor - left_sensor
    Torque = 10000
    vrum= speed**2
    Z = Torque - 0.486 * vrum
    X = 0.33
    Y = X * calibragem
    
    if Y >= 0.28:
        0.28 
    elif speed >= 126.5:
         Z= 500
    
    return {
        'engineTorque': Z,
        'brakingTorque': 0,
        'steeringAngle': Y,
        'log': [
            { 'name': 'Speed', 'value': speed, 'min': 0, 'max': 200 },
            { 'name': 'Left_sensor', 'value': left_sensor, 'min': 0, 'max': 1 },
            { 'name': 'Right_sensor', 'value': right_sensor, 'min': 0, 'max': 1 }
        ]
    }
