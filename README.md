## OpenSky Flight Tracker
This is a basic flight tracker app. I put this together mostly for fun and to try out [Bokeh](https://docs.bokeh.org/en/latest/index.html). Secondarily, I had seen several flight tracker tutorials online and none were really what I was looking for. So I put together a live updating tracker for myself that's live here: [https://all-in-one-300017.uc.r.appspot.com/app](https://all-in-one-300017.uc.r.appspot.com/app)

### Structure
This app is structured so that the front end reads from a data store that is refreshed every minute or so. The map and data table check for updates about every 10 seconds. The backend code, located [here](https://github.com/mgalla16-sn4g/flight-tracker/tree/master/backend) stands up an endpoint that GCP can hit on a cron schedule, triggering the endpoint to refresh the data store. I decided to structure this way to avoid having the front end make too many calls to the [OpenSky API](https://opensky-network.org/apidoc/index.html). Which can be a problem if more than a handful of people open this at once (longshot but possible).

### To-Do
- Update only when the data source updates
- Add flight details page
- Move non-updating elements into their own module

### Help me pls
If anyone has a good eye for design, I'd love some help making this thing actually look ok. As of now I'm just using a, let's say, minimalist style.