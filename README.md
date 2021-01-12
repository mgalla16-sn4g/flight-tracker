## OpenSky Flight Tracker

![Screenshot](/static/tracker.jpg)

This is a basic flight tracker app. I put this together mostly for fun and to try out [Bokeh](https://docs.bokeh.org/en/latest/index.html). Secondarily, I had seen several flight tracker tutorials online and none were really what I was looking for. So I put together a live updating tracker for myself that's live here: [https://all-in-one-300017.uc.r.appspot.com/app](https://all-in-one-300017.uc.r.appspot.com/app)

### Structure

#### Back-End
The backend of this app is rather simple. It consists of a simple Flask API that, when called, uses the [Traffic](https://traffic-viz.github.io/index.html) package to generate a json file with data on every flight currently tracked by the OpenSky project. The API is called on a Cloud Scheduler cron interval. The generated file is then sent to Cloud Storage where it can be read by the front end. The code in the /backend folder contains the Dockerfile used to build the API.

#### Front-End
The frontend is everything NOT in the /backend folder. It is a [Bokeh](https://docs.bokeh.org/en/latest/index.html) application that reads its underlying data from Cloud Storage. This occurs on a configurable interval. The layout is created by embedding each element then setting their locations and styling in the index.html template.

### To-Do
- Update only when the data source updates
- Add flight details page
- Move non-updating elements into their own module
- Remove Hello_World route from backend

### Help me pls
If anyone has a good eye for design, I'd love some help making this thing actually look ok. As of now I'm just using a, let's say, "minimalist" style.