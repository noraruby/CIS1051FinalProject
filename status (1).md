# Status Report

#### Your name

Nora Muma

#### Your section leader's name

I'm working by myself. Unless you mean my TA. My TA is Chong Li.

#### Project title

Your Perfect Running Route

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

I have created code that can generate maps based on location coordinates. Using folium, I learned how to draw polylines. Using openrouteservice, I learned how to make this polyline follow a suitable running path that avoids highways or illogical routes. I have also generated many potential routes but need to finish finding all of their coordinates and deciding their attributes.

#### What have you not done for your project yet?

I have not learned how to print directions or how to match the route to the runner based on their preferences. I am also deciding how I want this information to be made available to the runner. I would like if I could print the information outside of the program, but I am not quite sure if I will have time to worry about that. 

#### What problems, if any, have you encountered?

My biggest problem was iterating through the waypoint coordinate data to reverse the order. Since folium and openroute service both take different ordered inputs of longitude and latitude, I had to modify strings within a string to swap the coordinates for folium to interpret. For a while, I was inputing a route with start and end point in Philadelphia but receiving a path in Antarctica.
