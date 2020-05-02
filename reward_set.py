def reward_function(params):
    '''
    Example of rewarding the agent to stay inside two borders
    and penalizing getting too close to the objects in front
    '''

    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    objects_distance = params['objects_distance']
    _, next_object_index = params['closest_objects']
    objects_left_of_center = params['objects_left_of_center']
    is_left_of_center = params['is_left_of_center']
    speed = params['speed']
    heading = paarms['heading']

    #Maximising direction heading will allow maximum cornering speeds
    current_waypoint,next_waypoint = params[closest_waypoints]
    desired_heading = math.arctan((next_waypoint[0]-current_waypoint[0])/(next_waypoint[1]-current_waypoint[1]))
    
    if heading <= 1.05*desired_heading:
      elif heading >= 0.95*desired_heading
        reward_cornering = 10.0
    else:
      reward_cornering = 1e-3
    }
    # Initialize reward with a small number but not zero
    # because zero means off-track or crashed
    reward = 1e-3

    # Reward if the agent stays inside the two borders of the track
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward_lane = 1.0
    else:
        reward_lane = 1e-3

    # Penalize if the agent is too close to the next object
    reward_avoid = 1.0
    
    #Penalize if vehicle makes too many moves: smoother racing = objects_left_of_center
    reward_steps = -0.03*steps
    
    # Distance to the next object
    distance_closest_object = objects_distance[next_object_index]
    # Decide if the agent and the next object is on the same lane
    is_same_lane = objects_left_of_center[next_object_index] == is_left_of_center

    if is_same_lane:
        if 0.5 <= distance_closest_object < 0.8: 
            reward_avoid *= 0.5
        elif 0.3 <= distance_closest_object < 0.5:
            reward_avoid *= 0.2
        elif distance_closest_object < 0.3:
            reward_avoid = 1e-3 # Likely crashed

    # Calculate reward by putting different weights on 
    # the three aspects above and speed
    reward += 1.0 * reward_lane + 4.0 * reward_avoid + 0.8*speed + reward_steps + reward_cornering

    return reward
