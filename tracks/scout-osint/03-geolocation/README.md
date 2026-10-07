# Lab 03: Geolocation

**Track:** Scout | **Level:** Intermediate | **Time:** ~90 min

## What is it?
**Geolocation** is working out *where* an image or video was taken using only visual clues. **Chronolocation** works out *when*. It is the signature skill of open-source verification.

## The clue checklist
| Category | Examples |
|---|---|
| Language and script | Road signs, shop names, license plate formats |
| Infrastructure | Road markings, bollards, power poles, street lamps, rail gauge |
| Terrain and vegetation | Mountains, soil colour, tree species |
| Architecture | Roof shapes, building materials |
| Landmarks | Mosques, towers, bridges, billboards |
| Sun and shadows | Direction and length give time and orientation |
| Weather | Cross-check historical weather data |

## Setup
Free tools (browser only):
- Google Earth / Maps (Street View, satellite): https://earth.google.com
- OpenStreetMap: https://www.openstreetmap.org
- Overpass Turbo (query OpenStreetMap by feature): https://overpass-turbo.eu
- Mapillary (crowd-sourced street imagery): https://www.mapillary.com
- SunCalc (sun position and shadows): https://www.suncalc.org

## Walkthrough

### Step 1: Triage the image
List every clue on a sheet. **Don't zoom into one detail too early.** Narrow by country → region → city → street.

### Step 2: Narrow with infrastructure
Road markings, driving side and bollard style quickly eliminate most countries. Use a public reference such as Geoguessr-community cheat sheets (search "geolocation meta clues").

### Step 3: Search OpenStreetMap by features with Overpass
Suppose you see a pharmacy next to a mosque near a river. Overpass Turbo lets you search for that combo around a candidate area:
```
[out:json][timeout:25];
(
  node["amenity"="pharmacy"]({{bbox}});
  node["amenity"="place_of_worship"]["religion"="muslim"]({{bbox}});
);
out body;
```
In Overpass Turbo, zoom the map to your candidate city and run it. `{{bbox}}` fills in the visible area. Then look for locations where both appear close together.

Distance-based variant ("a pharmacy within 100 m of a place of worship"):
```
[out:json][timeout:25];
node["amenity"="place_of_worship"]({{bbox}})->.w;
node(around.w:100)["amenity"="pharmacy"];
out body;
```

### Step 4: Confirm with Street View and satellite
Match building shapes, skylines, trees and road layout. Confirm with at least **two independent matches**.

### Step 5: Chronolocation with shadows
1. Find the location, then use SunCalc to see sun direction through the day.
2. Compare shadow direction in the photo to find the **time window**.
3. Cross-check with weather and events.

### Step 6: State confidence
Write: "Located to <place> with **high** confidence because of matches X, Y, Z. Time of day approximately ..."

## Exercises
1. Take a photo of your own street, strip any metadata, give it to a friend, and see if they can locate it.
2. Do a published open-source geolocation challenge (e.g. from Bellingcat or the Quiztime community) blind, then compare to the answer.
3. Write the reasoning chain in `templates/osint-collection-log.md`.

## Checkpoint
- Why require two independent matches?
- What can you do with shadows?

## Ethics reminder
Geolocate public events, conflict imagery and public landmarks for verification. **Never** use this to find where private individuals live. See `ETHICS.md`.

## Go deeper
- Bellingcat geolocation guides and the Bellingcat online investigation toolkit (see `RESOURCES.md`)
- Practice: GeoGuessr, Quiztime challenges
