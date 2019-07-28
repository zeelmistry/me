TODO: Reflect on what you learned this week and what is still unclear.
To clone a repo, --> git pull "the link"
This week we completed the partner assignment. The setting up and cloning was relatively difficult compared to the work. 
The environment creation was interesting.

The y and x values are slightly different in coding compared to regular cartesian plane. The x axis goes from left to right but the y axis goes from top to bottom. This was important when calling certain parts. 
We decided that the wrist joint needed to be above the shoulder joint to be recognised as a hailing taxi. 
This meant the wrist y-value needed to be less than the shoulder y-value.

--> we got stuck in how to call the y-value.
After using the debugger and a similar way of calling dictionaries we were able to find a way to call the y-value. 
Once that was figured out we were simply able to create a code to only call the hailing taxi function when the wrist was above the shoulder.
This wasnt working with a simple if and elif statement so we needed to create a try loop. 
This try loop would try to see if the wrist was above the shoulder if it wasnt it wouldnt run the function however if it was it would. 
The try loop also contained an exception which stopped the terminal to constantly spit out 'hailing taxi' when it wasnt.
This code was repeated for both left and right sides. 