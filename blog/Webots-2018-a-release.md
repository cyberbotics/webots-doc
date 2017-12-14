# Version R2018a Released

<p id="publish-data">By Tom Norton - XXth XXX 2018</p>

---

Today we're happy to announce the release of the all-new Webots 2018a, packed with some great new features. We're going to talk about some of them here, but for a comprehensive list of changes please refer to the ChangeLog, found [here](https://www.cyberbotics.com/dvd/common/doc/webots/ChangeLog.html)).

### New Beginnings

This release brings a change to the way Webots is released. We have been looking for a means of improving our release schedule to provide reliability for our users, and a more strict release schedule that ensures updates are shipped predictably and reliably. Thus, we are migrating from a Major-Minor-Maintenance versioning system to follow the MathWorks model. We will now be aiming to release new editions of Webots annualy, with major intermediate releases every six months, starting with Webots 2018a, then Webots 2018b, then Webots 2019a etc. Maintenance revisions will still be shipped to fix critical bugs between these release milestones.

## Enhanced Viewpoint Movement

### Line It Up Just Right

Take better screenshots and record better videos of your robot by aligning the viewpoint on one of the six world axes, using the new Change View tool:

%figure "New Change View Menu"
![viewpoint menu](images/viewpoint_menu.png)
%end

### Smooth

Now, all automated Viewpoint movement is animated, when resetting the viewpoint, moving the viewpoint to an object, or moving to any of the six default views:

<video class="webm" autoplay loop>
  <source src="https://www.cyberbotics.com/files/repository/videos/viewpoint_animation.webm" type="video/webm">
</video>

---

## HTML5 Robot Windows

Over the last couple of years we have been slowly phasing out our native QT-based robot window system, in order to use Web technologies for more powerful layout & design tools, starting with the E-puck and Thymio II robots. The biggest and most comprehensive step in this task is implementing the default generic robot window in HTML5/JavaScript/CSS, as most of our distributed robot models use the generic window. This update brings a new, shiny generic window for use with any robot you create.

<video class="webm" autoplay loop>
  <source src="https://www.cyberbotics.com/files/repository/videos/html_robot_window.webm" type="video/webm">
</video>

---

## Python 3

---

## On The Road

### New Truck & Two-Wheeled Models

In addition to the `Bus` PROTO two new models of trucks have been added:

%figure "Models of large vehicles"
![large vehicles](images/large_vehicles.png)
%end

Furthermore, a model of a motorbike and a model of a scooter have been added:

%figure "Models of two wheels vehicles"
![two wheels](images/two_wheels.png)
%end

All these new models are now used in the SUMO interface.
