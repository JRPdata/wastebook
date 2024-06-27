# Mainly Hurricane/Cyclone/Typhoon Links (forecasting, analysis, observations)
Also extreme weather, climate, various environmental hazards, and random notes

---

#### Table of Contents
- [Surface Analysis](#surface)
- [General Analysis](#generalanl)
- [Satellite Products](#satellite)
- [Realtime/Live Imagery, Analysis](#live)
- [Ocean Temperatures (SST, OHC)](#oceantemp)
- [Decks & Fixes - Automated data (ATCF)](#atcf)
- [TC Genesis and Forecasts](#genesis)
- [Official Sites](#ofcl)
- [Dropsondes (hurricane hunter planes)](#dsonde)
- [Best tracks](#besttracks)
- [Archives and Verification](#archives)
- [Forecast websites for Model products](#models)
- [Public Discussion on social sites](#social)
- [General weather and environmental sites](#general)
- [Data (gribs)](#gribdata)
- [Other hazards](#other)
- [Climate](#climate)
- [High altitude weather & climate](#strato)
- [Other sites with data](#misclinks)
- [Satellite imagery archive](#satarchive)
- [Radar imagery archive](#radararchive)
- [Random sites](#random)
- [Experimental personal projects](#expnotes)

---

<a name="surface"/>

## Surface Analysis (Synoptic)
- see also mesoscale analysis (HRRR) expert in general links

- [https://www.nhc.noaa.gov/tafb/?C=M;O=D](https://www.nhc.noaa.gov/tafb/?C=M;O=D)
    - (sort by date: USA_XXZ.pdf) - PDFs have highest quality
    - See also OHC (ocean heat content)
        - NHC relies TAFB analysis

- [https://ocean.weather.gov/unified_analysis.php](https://ocean.weather.gov/unified_analysis.php)

- DOCUMENTATION:
    - [https://www.wpc.ncep.noaa.gov/sfc/UASfcManualVersion1.pdf#page3](https://www.wpc.ncep.noaa.gov/sfc/UASfcManualVersion1.pdf#page3)

<a name="generalanl"/>

## General Analysis
- [https://mag.ncep.noaa.gov/](https://mag.ncep.noaa.gov/)
    - model & analyses (tons of products): mesoscale, observations (i.e. skew-t), etc

<a name="satellite"/>

## Satellite (Visible, Microwave) Imagery and Products
- NRL NEW,OLD microwave imagery (active storms only):
    - [https://www.nrlmry.navy.mil/tcweb/active/](https://www.nrlmry.navy.mil/tcweb/active/)
        - (Educational) Training documentation [https://www.nrlmry.navy.mil/training-bin/training.cgi](https://www.nrlmry.navy.mil/training-bin/training.cgi)
    - [https://www.nrlmry.navy.mil/TC.html](https://www.nrlmry.navy.mil/TC.html)
- FNMOC microwave imagery (active storms only):
    - [https://www.fnmoc.navy.mil/tcweb/cgi-bin/tc_home.cgi](https://www.fnmoc.navy.mil/tcweb/cgi-bin/tc_home.cgi)

- BEST winds (in meters/sec!) (ASCAT; includes chinese satellites also!)
    - [https://scatterometer.knmi.nl/tile_prod/](https://scatterometer.knmi.nl/tile_prod/)
- winds/rain (slower updates) ASCAT, SSM/I, ASMR, etc.
    - [https://manati.star.nesdis.noaa.gov/datasets/ASCATBData.php](https://manati.star.nesdis.noaa.gov/datasets/ASCATBData.php)
        - DOCUMENTATION FOR SSM/I
            - [https://www.ncei.noaa.gov/products/climate-data-records/ssmis-brightness-temperature-rss](https://www.ncei.noaa.gov/products/climate-data-records/ssmis-brightness-temperature-rss)
- alternative winds (satellite only)
    - [https://www.star.nesdis.noaa.gov/goesr/winds/index.php](https://www.star.nesdis.noaa.gov/goesr/winds/index.php)
    - SAR winds (winds by quadrant and distance, with imagery and fixes: very useful!)
    - for cyclones:
        - [https://www.star.nesdis.noaa.gov/socd/mecb/sar/sarwinds_tropical.php?year=latest](https://www.star.nesdis.noaa.gov/socd/mecb/sar/sarwinds_tropical.php?year=latest)
    - for invests:
        - [https://www.star.nesdis.noaa.gov/socd/mecb/sar/sarwinds_rcm_rs2.php](https://www.star.nesdis.noaa.gov/socd/mecb/sar/sarwinds_rcm_rs2.php)

- DOCUMENTATION:
    - [https://groups.ssec.wisc.edu/groups/iwwg/information](https://groups.ssec.wisc.edu/groups/iwwg/information)


- microwave (GMI) rain/water/wind analysis:
    - [https://images.remss.com/gmi/gmi_data_daily.html](https://images.remss.com/gmi/gmi_data_daily.html)
- ASMR2 analyses (wind/rain/temps):
    - [https://www.ospo.noaa.gov/Products/atmosphere/gpds/maps.html?GPOWS#gpdsMaps](https://www.ospo.noaa.gov/Products/atmosphere/gpds/maps.html?GPOWS#gpdsMaps)

- global rain rates (SCOPE):
    - [https://sigma.cptec.inpe.br/scope/](https://sigma.cptec.inpe.br/scope/)
- global rain rates (NESDIS - JPSS: CMORPH2):
    - [https://www.star.nesdis.noaa.gov/jpss/EDRs/products_blended_cmorph.php](https://www.star.nesdis.noaa.gov/jpss/EDRs/products_blended_cmorph.php)
        - (near) real time (a few hours late?), with 30 min animations
- global rain rate (medium res static):
    - [https://gpm.nasa.gov/data/imerg#latesthalf-hourlyimage](https://gpm.nasa.gov/data/imerg#latesthalf-hourlyimage)
- global rain rate JAXA (interactive, hourly, can specify lat/long)
    - [https://sharaku.eorc.jaxa.jp/GSMaP/](https://sharaku.eorc.jaxa.jp/GSMaP/)

- viirs (CIMSS): high resolution (but not searchable/indexed for storms)
- [https://cimss.ssec.wisc.edu/viirs/imagery-viewer/?satellite=npp](https://cimss.ssec.wisc.edu/viirs/imagery-viewer/?satellite=npp)

- NHC analysis products (Hovmoller satelltie imagery for TC development regions, upper air time sections, etc):
    - [https://www.nhc.noaa.gov/analysis_tools.php](https://www.nhc.noaa.gov/analysis_tools.php)

<a name="live"/>

## Live Imagery, Analysis, Data (Good Also for Looking for Genesis)
- Note: CIRA and CIMSS have the most useful collection of products for analysis

- [https://rammb-slider.cira.colostate.edu/](https://rammb-slider.cira.colostate.edu/)
    - Satellite imagery from RAMMB SLIDER
        - for active storms can sometimes get 1 min HIGH RES imagery updates when mesoscale is active, select appropriate source
        - also has many other products
        - DOCUMENTATION on bands (educational):
            - [https://www.noaa.gov/jetstream/goes_east](https://www.noaa.gov/jetstream/goes_east)
- (lower res for meteosats if rammb slider not available for meteo10)
    - [https://view.eumetsat.int/productviewer?v=msg_fes:ir108](https://view.eumetsat.int/productviewer?v=msg_fes:ir108)
- alternative GOES viewer with 1 min data:
    - [https://geosphere.ssec.wisc.edu/](https://geosphere.ssec.wisc.edu/)

- [https://hurricanes.ral.ucar.edu/realtime/current/](https://hurricanes.ral.ucar.edu/realtime/current/)
    - Real time link collection from UCAR (from a variety of sources)
    - (Don't forget buoy data links)

- CIRA real time (tons of useful data, slightly different versions/data then used by OSPO (ie experimental satellite winds))
    - [https://rammb-data.cira.colostate.edu/tc_realtime](https://rammb-data.cira.colostate.edu/tc_realtime)
    - see also [https://cat.cira.colostate.edu/sport/layered/advected/LPW_alt.htm](https://cat.cira.colostate.edu/sport/layered/advected/LPW_alt.htm)
        - (Advected Layered Precipitable Water), similar but complentary to MIMIC TPW from CIMSS

- invests & active storms:
    - [https://tropicaltidbits.com](https://tropicaltidbits.com)
        - has good dvorak type image loops for invests/active cyclones
    - [https://tropic.ssec.wisc.edu/](https://tropic.ssec.wisc.edu/)
        - CURRENT STORMS/INVESTS: click on storm on map for popup analysis (feat. MICROWAVE analysis products!)

        - quicklinks under map (active storms/invests):
            - MIMIC-TC very good for visualizing storm (AI + satellite/microwave imagery)
            - MIMIC-TPW for genesis (similar to CIRA) (look for mixing/swirls, note amount of water at and nearby storm path)
                - [https://tropic.ssec.wisc.edu/real-time/mtpw2](https://tropic.ssec.wisc.edu/real-time/mtpw2)
            - Other intensity/position products all fairly useful and are used operationally (ADT/ARCHER/mint/dmint)
                - SATCON is best for intensity (when its working, and has lots of good recent data)
            - ARCHER/MPERC has good track fixes, analyses for cyclones that are understandable (including eyewall replacement predictions!)
                - (useful extra info = click on data points in charts/tables)
                - (bonus is get good satellite imagery & analysis for active storms - gmi/ssmi/asmr)

        - ALL Regional products have very good (satellite) analysis visualizations == especially useful for genesis
            - especially winds as it provides different analyses: shear/vorticity/convergence/divergence) == very useful
            - NOTE: winds products charts can shift slightly from one analysis to the next so note grid lines
            - [https://tropic.ssec.wisc.edu/real-time/windgridmain.php?&basin=atlantic&sat=wg8](https://tropic.ssec.wisc.edu/real-time/windgridmain.php?&basin=atlantic&sat=wg8)

- SSD (NOAA) Microwave, Winds:
    - [https://www.ssd.noaa.gov/PS/TROP/mwtc-ospo.html](https://www.ssd.noaa.gov/PS/TROP/mwtc-ospo.html)
    - [https://www.ssd.noaa.gov/PS/TROP/mtcswa.html](https://www.ssd.noaa.gov/PS/TROP/mtcswa.html)

- OSPO (NOAA) satellite analysis (human dvorak)
    - [https://www.ospo.noaa.gov/Products/ocean/tropical/bulletins.html](https://www.ospo.noaa.gov/Products/ocean/tropical/bulletins.html)
    - tc positions:
    - [https://www.ospo.noaa.gov/Products/ocean/tropical/tdpositions.html](https://www.ospo.noaa.gov/Products/ocean/tropical/tdpositions.html)

    - TAFB doesn't publish their dvorak analyses (:sadface:)

- NDBC buoy data (NOAA):
    - [https://www.ndbc.noaa.gov/radial_search.php](https://www.ndbc.noaa.gov/radial_search.php)

- [https://zoom.earth/](https://zoom.earth/)
    - Satellite imagery with a useful visualization purpose:
    - Since it overlays the interpolated model storm track, you can notice deviations from forecast track (space & time)

- NESDIS hurricane tracker:
    - [https://www.nesdis.noaa.gov/imagery/hurricanes/live-hurricane-tracker](https://www.nesdis.noaa.gov/imagery/hurricanes/live-hurricane-tracker)
        - visualizations of satellite imagery with track/wind radii etc.

- NEXTSAT (never used, but has JPSS imagery)
    - [https://www.nrlmry.navy.mil/NEXSAT.html](https://www.nrlmry.navy.mil/NEXSAT.html)

machine dvorak (ADT):

- [https://www.ssd.noaa.gov/PS/TROP/adt.html](https://www.ssd.noaa.gov/PS/TROP/adt.html)

SHIPS / Intensification
- [https://ftp.nhc.noaa.gov/atcf/stext/?C=M;O=D](https://ftp.nhc.noaa.gov/atcf/stext/?C=M;O=D)
    - (need to reference a couple papers to understand which types of analysis provide the best prediction for different intervals)
    - (take into account data (or lack of) fed into such systems (recent hurricane hunter/sondes data, microwave, satellite (daylight-vis or IR))

<a name="oceantemp"/>

## SST, OHC
- Observations and Forecast (a week out?):
    - [https://data.marine.copernicus.eu/viewer/expert?view=viewer](https://data.marine.copernicus.eu/viewer/expert?view=viewer)
        - Has other modes but expert is most useful but time consuming:
        - can draw a polygon ("areas" at bottom right) for current day and for a few forecast days for SST
            - (hit the "i" button for keyboard shortcuts:
                - SHIFT ? for shortcuts
                - shift + or shift - for zoom on center screen
            - no storm track, add layer to get fix for previous day to get approximate area for last fix:
                - goto current/previous day
                - add layer: filter by wind, "Global Ocean Hourly Sea Surface Wind and Stress from Scatterometer"
                    - add wind variable
                - adjust opacity downwards and change style to solid+vectors to 20%
            - draw box around storm path:
                - click Areas:
                    - add rough points from bdeck/adecks manually by hovering over lat longs
                    - (make sure to adjust slider, hit ESC to complete polygon)
            - if you want a lot of JUST sample points and boxes get in the way:
                - minimize each point once after adding it (the down arrow next to X button)
                - and click and drag the box it away so can add more points

- Observations:
    - [https://www.nhc.noaa.gov/sst/](https://www.nhc.noaa.gov/sst/)
        - Reynolds 2 deg contours (1 day old), regional only

    - [https://ghrsst-pp.metoffice.gov.uk/ostia-website/img/global_sst_analysis.png](https://ghrsst-pp.metoffice.gov.uk/ostia-website/img/global_sst_analysis.png)
        - high res 2 deg contours (GLOBAL)

    - [https://www.ospo.noaa.gov/Products/ocean/sst/contour/](https://www.ospo.noaa.gov/Products/ocean/sst/contour/)
        - only regional charts have scales
            - unfortunately the contours aren't labeled on map and the scale is also not easy to read
        - globally
            - see also anomaly page
                - [https://www.ospo.noaa.gov/Products/ocean/sst/anomaly/index.html](https://www.ospo.noaa.gov/Products/ocean/sst/anomaly/index.html)
            - and blended page which does have scale but is medium res (and a day old):
                - [https://www.ospo.noaa.gov/Products/ocean/sst/blended_sst_5km.html?product=bdn](https://www.ospo.noaa.gov/Products/ocean/sst/blended_sst_5km.html?product=bdn)

    - [https://www.ospo.noaa.gov/Products/ocean/ohc/](https://www.ospo.noaa.gov/Products/ocean/ohc/)
        - No contours

- TAFB:
    - [https://www.nhc.noaa.gov/tafb/?C=M;O=D](https://www.nhc.noaa.gov/tafb/?C=M;O=D)
    - sometimes they produce OHC

- DOCUMENTATION AND MORE LINKS:
    - [https://www.ghrsst.org/ghrsst-data-services/for-sst-data-users/products/](https://www.ghrsst.org/ghrsst-data-services/for-sst-data-users/products/)
        - Documentation and links (they produce the product that is a blend/compilation of various SST products)

- [https://www.star.nesdis.noaa.gov/socd/ov/](https://www.star.nesdis.noaa.gov/socd/ov/)
    - requires powerful computer (I can't run it as it is too slow for me)
        - might be better than

<a name="atcf"/>

## a,b,e,f decks: ATCF products, fixes
- (a=official forecast, b=best track, f=fixes
- UCAR mirrors (don't rely on sort by time! search by extension "24.dat" etc...):
    - [https://hurricanes.ral.ucar.edu/repository/data/adecks_open/?C=M;O=D](https://hurricanes.ral.ucar.edu/repository/data/adecks_open/?C=M;O=D)
    - [https://hurricanes.ral.ucar.edu/repository/data/bdecks_open/2024/](https://hurricanes.ral.ucar.edu/repository/data/bdecks_open/2024/)
    - [https://hurricanes.ral.ucar.edu/repository/data/fdecks_open/](https://hurricanes.ral.ucar.edu/repository/data/fdecks_open/)
    - TCVITALS ~= CARQ storm info fed into computer model (precedes public forecast and -only- hints at what official forecast might be)
    - [https://hurricanes.ral.ucar.edu/repository/data/tcvitals_open/2024/](https://hurricanes.ral.ucar.edu/repository/data/tcvitals_open/2024/)
    - [https://hurricanes.ral.ucar.edu/repository/data/carq/2024/](https://hurricanes.ral.ucar.edu/repository/data/carq/2024/)
- NOAA
    - adeck (might be more delayed and not work sometimes?)
        - [https://ftp.nhc.noaa.gov/atcf/aid_public](https://ftp.nhc.noaa.gov/atcf/aid_public)
    - bdeck (first best track -- not the final best track that comes months later)
        - [https://ftp.nhc.noaa.gov/atcf/btk](https://ftp.nhc.noaa.gov/atcf/btk)
    - fdeck
        - [https://ftp.nhc.noaa.gov/atcf/fix/](https://ftp.nhc.noaa.gov/atcf/fix/)
    - tcvitals
        - [https://ftp.nhc.noaa.gov/atcf/com/tcvitals](https://ftp.nhc.noaa.gov/atcf/com/tcvitals)
    - edeck (error,probability info)
        - [https://ftp.nhc.noaa.gov/atcf/gpce/](https://ftp.nhc.noaa.gov/atcf/gpce/)

- AMSU (microwave) ATCF:
    - [https://tropic.ssec.wisc.edu/real-time/amsu/2024/AMSU_ATCF/?C=M;O=D](https://tropic.ssec.wisc.edu/real-time/amsu/2024/AMSU_ATCF/?C=M;O=D)

- NESDIS ATCF:
    - [https://satepsanone.nesdis.noaa.gov/pub/tropics/sabatcf/](https://satepsanone.nesdis.noaa.gov/pub/tropics/sabatcf/)

- FORMAT INFOS:
    - [https://www.nrlmry.navy.mil/atcf_web/docs/database/new/abdeck.txt](https://www.nrlmry.navy.mil/atcf_web/docs/database/new/abdeck.txt)
    - [https://www.nrlmry.navy.mil/atcf_web/docs/database/new/newfdeck.txt](https://www.nrlmry.navy.mil/atcf_web/docs/database/new/newfdeck.txt)
    - [https://ftp.nhc.noaa.gov/atcf/README](https://ftp.nhc.noaa.gov/atcf/README)
    - [https://www.nrlmry.navy.mil/atcf_web/docs/database/new/edeck.txt](https://www.nrlmry.navy.mil/atcf_web/docs/database/new/edeck.txt)

<a name="genesis"/>

# TC Genesis and Forecasts:

- [https://moe.met.fsu.edu/modelgen/summary168al.php](https://moe.met.fsu.edu/modelgen/summary168al.php)
    - Robert Hart's site has lots of useful products:
        - [https://moe.met.fsu.edu/~rhart/web.php](https://moe.met.fsu.edu/~rhart/web.php)
    - Especially:
        - genesis (above) (an operational version used by NHC as part of the data for there outlooks)
        - cyclone phase plots for determining confidence on model predictions
            - includes also model forecast SSTs (with useful contours which is not often seen on SST maps)
            - also ensembles for product
            - READ documentation/ppts on his site AND!
            - READ powerpoints from the WMO educational powerpoints in training materials (TCFW) for a more complete understanding

- [https://www.ospo.noaa.gov/Products/ocean/tropical/](https://www.ospo.noaa.gov/Products/ocean/tropical/)
- [https://www.ssd.noaa.gov/PS/TROP/TCFP/index.html](https://www.ssd.noaa.gov/PS/TROP/TCFP/index.html)
    - DOCUMENTATION:
        - [https://www.ssd.noaa.gov/PS/TROP/TCFP/description.html](https://www.ssd.noaa.gov/PS/TROP/TCFP/description.html)
    - LOG file sometimes useful:
        - [https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/tcfpmain.log](https://www.ssd.noaa.gov/PS/TROP/TCFP/data/current/tcfpmain.log)


- [https://charts.ecmwf.int/?facets=%7B%22Product%20type%22%3A%5B%5D%2C%22Range%22%3A%5B%5D%2C%22Parameters%22%3A%5B%22Tropical%20cyclones%22%5D%7D](https://charts.ecmwf.int/?facets=%7B%22Product%20type%22%3A%5B%5D%2C%22Range%22%3A%5B%5D%2C%22Parameters%22%3A%5B%22Tropical%20cyclones%22%5D%7D)
    - ECMWF Genesis, frequency, intensity, ACE, etc Probabilities and tracks

- CPC ENSO(El Nino La Nina)/MJO products (storm tracks not updated)
    - [https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/mjo.shtml](https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/mjo.shtml)
    - [https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/enso.shtml](https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/enso.shtml)
        - See also links and pdfs at bottom for MJO/ENSO

- rain rates and many other analysis (CMC model)
    - [https://eccc-msc.github.io/msc-animet/?layers=GDPS.ETA_RT%3B0.75%3B0%3B1%3B0%3B1&extent=-23717480,-1408201,5811428,13494670](https://eccc-msc.github.io/msc-animet/?layers=GDPS.ETA_RT%3B0.75%3B0%3B1%3B0%3B1&extent=-23717480,-1408201,5811428,13494670)
    - and many other ways to analyze (adjust layers)

- ECMWF MJO (MJO used many ways: placing confidence in model forecasts for storms per region, predicting increased storm activity long term):
    - [https://charts.ecmwf.int/products/mofc_multi_mjo_family_index](https://charts.ecmwf.int/products/mofc_multi_mjo_family_index)

- Tropical waves:
    - Velocity potential anomaly (GFS 200 hPa, fast animations):
        - [https://www.atmos.albany.edu/student/ventrice/real_time/maps/velocity_pot/anom/global_forecast.html](https://www.atmos.albany.edu/student/ventrice/real_time/maps/velocity_pot/anom/global_forecast.html)
    - extended range GEFS velocity potential anomaly (00z run has 35 days out, other runs only to 16 days):
        - [https://www.tropicaltidbits.com/analysis/models/?model=gfs-ens&region=global&pkg=chi200Mean](https://www.tropicaltidbits.com/analysis/models/?model=gfs-ens&region=global&pkg=chi200Mean)

- EMC/NOAA TC genesis probability charts, storm tracks, and text files (esp. useful for ensemble tracks):
    - [https://www.emc.ncep.noaa.gov/gmb/tpm/emchurr/tcgen/](https://www.emc.ncep.noaa.gov/gmb/tpm/emchurr/tcgen/)

- CIRA experimental TCGI (genesis probability trends charts for invests, not too accurate but roughly useful as a sanity check?):
    - [https://rammb.cira.colostate.edu/research/tropical_cyclones/tc_genesis_index/](https://rammb.cira.colostate.edu/research/tropical_cyclones/tc_genesis_index/)
    - Active directory: [https://rammb.cira.colostate.edu/realtime_data/nhc/tcgi/](https://rammb.cira.colostate.edu/realtime_data/nhc/tcgi/)

- ECMWF (essential means public) gribs/bufr for storms:
    - [https://essential.ecmwf.int/](https://essential.ecmwf.int/)

<a name="ofcl"/>

## OFFICIAL sites:

- RSMC:
    - US (NHC - NOAA, with analysis done by TAFB)
        - Atlantic/ Eastern Pacific
            - [https://www.nhc.noaa.gov](https://www.nhc.noaa.gov)
        - Central Pacific:
            - [http://www.prh.noaa.gov/cphc/](http://www.prh.noaa.gov/cphc/)

        - [https://www.nhc.noaa.gov/gtwo.php](https://www.nhc.noaa.gov/gtwo.php)
            - (Noaa outlook for genesis, change basin for Atlantic, East Pacific, Central Pacific)

        - CPC (extended GLOBAL genesis forecasts (week 2-3):
            - [https://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghaz/index.php](https://www.cpc.ncep.noaa.gov/products/precip/CWlink/ghaz/index.php)
                - Especially see discussion (below graphics) and PDF links
                - The "Product" and "Briefing" (contains Prognostic reasoning, charts/graphs) PDF links are at the bottom right

    - Taiwan (CWB)
        - [https://www.cwa.gov.tw/eng/](https://www.cwa.gov.tw/eng/)

    - Japan (JMA)
        - [https://www.jma.go.jp/bosai/map.html#contents=typhoon&lang=en](https://www.jma.go.jp/bosai/map.html#contents=typhoon&lang=en)

    - India (IMD)
        - [https://rsmcnewdelhi.imd.gov.in/index.php](https://rsmcnewdelhi.imd.gov.in/index.php)

    - Fiji (Fiji MET)
        - [https://www.met.gov.fj/international_warn.htm](https://www.met.gov.fj/international_warn.htm)
        - [https://www.met.gov.fj](https://www.met.gov.fj)

    - France (LaReunion)
    - [https://meteofrance.re/fr/cyclone](https://meteofrance.re/fr/cyclone)

- TCWC:
    - Indonesia (BMKG):
        - [http://wis.bmkg.go.id/index.php?portal=dcpc&lang=en](http://wis.bmkg.go.id/index.php?portal=dcpc&lang=en)

    - Australia (BOM)
        - [http://www.bom.gov.au/](http://www.bom.gov.au/)

    - Papa New Guinea (PNG MET)
        - [https://www.pngmet.gov.pg/](https://www.pngmet.gov.pg/)

    - New Zealand - Tasman Sea (Metservice)
        - [https://www.metservice.com/warnings/home](https://www.metservice.com/warnings/home)

- [https://severeweather.wmo.int/](https://severeweather.wmo.int/)

<a name="dsonde"/>

## Dropsondes (hurricane hunter planes), Recon, and other data:
- [https://www.nhc.noaa.gov/recon.php](https://www.nhc.noaa.gov/recon.php)
    Schedules and Educational information about recon (Links to Plan of the day and other resources)
- [https://tropicaltidbits.com](https://tropicaltidbits.com)
    - The best source
    - Educational see recon link above and various WMO Training materials on it (i.e.):
        - [https://severeweather.wmo.int/TCFW/RAIV_Workshop2023/21_Analysis-Aircraft-Reconnaissance-Data_LisaBucci.pdf](https://severeweather.wmo.int/TCFW/RAIV_Workshop2023/21_Analysis-Aircraft-Reconnaissance-Data_LisaBucci.pdf)
        - [https://www.nhc.noaa.gov/outreach/presentations/nhc2013_aircraftData.pdf](https://www.nhc.noaa.gov/outreach/presentations/nhc2013_aircraftData.pdf)
    - or raw source:
        - [https://tgftp.nws.noaa.gov/SL.us008001/DF.an/DC.vsndn/DS.dropw/](https://tgftp.nws.noaa.gov/SL.us008001/DF.an/DC.vsndn/DS.dropw/)
        - FORMAT (also see WMO doc in the educational links):
            - [https://www.aoml.noaa.gov/hrd/format/tempdrop_format.html](https://www.aoml.noaa.gov/hrd/format/tempdrop_format.html)
            - [https://www.aoml.noaa.gov/hrd/Storm_pages/sondeformat.html](https://www.aoml.noaa.gov/hrd/Storm_pages/sondeformat.html)
        - DOCUMENTATION for more raw data types on NOAA:
            - [https://www.weather.gov/tg/engfiles](https://www.weather.gov/tg/engfiles)
            - [https://www.weather.gov/tg/obsfiles](https://www.weather.gov/tg/obsfiles)
            - [https://w2.weather.gov/source/datamgmt/filstnd.html](https://w2.weather.gov/source/datamgmt/filstnd.html)
        - Other data:
            - [https://tgftp.nws.noaa.gov/SL.us008001/](https://tgftp.nws.noaa.gov/SL.us008001/)
        - Recon (i.e. AF surveys):
            - [https://tgftp.nws.noaa.gov/SL.us008001/DF.an/DC.sluan/DS.recco/?C=M;O=D](https://tgftp.nws.noaa.gov/SL.us008001/DF.an/DC.sluan/DS.recco/?C=M;O=D)
- NESDIS:
    - (not live):
        - [https://manati.star.nesdis.noaa.gov/datasets/IWRAPDataDisplay.php?&category=IWRAP&storm=NIGEL&year=2023&flight=20230920I1&product=1](https://manati.star.nesdis.noaa.gov/datasets/IWRAPDataDisplay.php?&category=IWRAP&storm=NIGEL&year=2023&flight=20230920I1&product=1)
    - (live? latest mission?)
        - [https://manati.star.nesdis.noaa.gov/datasets/AircraftDataNew.php](https://manati.star.nesdis.noaa.gov/datasets/AircraftDataNew.php)
            - different spatial decompositions for the data, ie: all surface-wind data
            - super cool 3d visualizations of the drop-sonde data
            - Don't remember if I've used this

<a name="besttracks"/>

## Best Tracks and Reports
- (official, FINAL, US best tracks / reports)
- [https://www.nhc.noaa.gov/data/tcr/](https://www.nhc.noaa.gov/data/tcr/)

- other track data (not necessary final best track):
    - [https://www.nhc.noaa.gov/gis/](https://www.nhc.noaa.gov/gis/)

- IB best tracks (authoritative, international collection):
    - [https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/](https://www.ncei.noaa.gov/data/international-best-track-archive-for-climate-stewardship-ibtracs/)
- IB best tracks documentation:
    - [https://www.ncei.noaa.gov/sites/default/files/2021-07/IBTrACS_v04_column_documentation.pdf](https://www.ncei.noaa.gov/sites/default/files/2021-07/IBTrACS_v04_column_documentation.pdf)

- Other sites best tracks/reports (harder to find in different languages):
    - Brazil
        - [https://www.marinha.mil.br/chm/dados-do-smm-monitoramento-de-ciclones](https://www.marinha.mil.br/chm/dados-do-smm-monitoramento-de-ciclones)

<a name="archives"/>

## Archived data, analysis/reanalysis, verification
- (HURDAT text table)
    - [https://www.aoml.noaa.gov/hrd/hurdat/All_U.S._Hurricanes.html](https://www.aoml.noaa.gov/hrd/hurdat/All_U.S._Hurricanes.html)

- [https://www.nhc.noaa.gov/data/](https://www.nhc.noaa.gov/data/)
    - SEE HURDAT2 for reanalysis archive data
        - REANALYSIS DOC:
            - [https://www.aoml.noaa.gov/hrd/data_sub/re_anal.html](https://www.aoml.noaa.gov/hrd/data_sub/re_anal.html)
    - lots of data and summaries

- VERIFICATION: NHC OFCL FORECAST ERRORS (useful data for assigning confidence/probability to OFCL forecasts):
- [https://www.nhc.noaa.gov/verification/](https://www.nhc.noaa.gov/verification/)

- NOAA TEXT archive:
- [https://www.nhc.noaa.gov/archive/text/](https://www.nhc.noaa.gov/archive/text/)

- (Operational) Model verification (EMC/NOAA)
    - [https://www.emc.ncep.noaa.gov/users/verification/global/gfs/prod/](https://www.emc.ncep.noaa.gov/users/verification/global/gfs/prod/)
        - Main models, ensembles comparison (operational verification, and past years)
    - For other models, see also [https://www.emc.ncep.noaa.gov/emc/pages/verification.php](https://www.emc.ncep.noaa.gov/emc/pages/verification.php)

<a name="models"/>

## Forecast model products (many sites)
- [https://storm.aoml.noaa.gov/viewer/](https://storm.aoml.noaa.gov/viewer/)
    - Invests and Active Storms Model Data
        - Useful live error and validation information for models!
    - ATL/PAC Wide is useful for quick looks at genesis
    - Also see links to other specific model sites used by it (as they have different useful charts, and SHIPS data)
- [https://products.hfip.org/nhc-display/](https://products.hfip.org/nhc-display/)
    - Quick and useful for plotting lots of different models and specific ensemble members
    - Also plot and look at different wind field data for models
- [https://www.tropicaltidbits.com](https://www.tropicaltidbits.com)

- [https://mag.ncep.noaa.gov/](https://mag.ncep.noaa.gov/)
    - wide variety of model guidance and observations (not as jazzy as other sites)
- [https://www.fnmoc.navy.mil/wxmap_cgi/index.html#global](https://www.fnmoc.navy.mil/wxmap_cgi/index.html#global)
    - Navy collection of model charts (NAVGEM, GFS, COAMPS, etc)

- [https://ocean.weather.gov/windprob.php](https://ocean.weather.gov/windprob.php)
    - Wind exceedance probability charts for GEFS & NAEFS (good for getting forecast probabilities on specific wind speeds: can choose from several limits in 5 to 10 ~kt increments)

- [https://www.atmos.albany.edu/facstaff/tang/tcguidance/](https://www.atmos.albany.edu/facstaff/tang/tcguidance/)
    - TC guidance

- [https://charts.ecmwf.int/products/medium-uv-z?base_time=202405311200&level=925&projection=opencharts_central_america&valid_time=202405311200](https://charts.ecmwf.int/products/medium-uv-z?base_time=202405311200&level=925&projection=opencharts_central_america&valid_time=202405311200)
    - model tradewind forecasts for US

- [https://weather.us/](https://weather.us/)
    - Spaghetti tracks (useful visualization for ensemble member intensities + ECMWF data)

- [https://www.weathernerds.org/](https://www.weathernerds.org/)
    - has unique way to track live storm paths, and other unique products

- [https://www.pivotalweather.com/model.php?m=gfs&p=qpf_048h-imp](https://www.pivotalweather.com/model.php?m=gfs&p=qpf_048h-imp)
    - many models and very extensive products
    - has many other products (haven't used much)
        - subscription service (commercial use requires subscription)

- [https://meteocentre.com/numerical-weather-prediction/map-animation.php?mod=ecmwf&run=00&stn=PNM&mode=latest&map=hnord&lang](https://meteocentre.com/numerical-weather-prediction/map-animation.php?mod=ecmwf&run=00&stn=PNM&mode=latest&map=hnord&lang)
    - CMC,ECMWF-HRES,ETC HURRICANE GLOBAL MODELS  - / Animations
    - Harder to use as maps are polar

- Tomer Burg's site
    - [http://arctic.som.ou.edu/tburg/products/realtime/tropical/](http://arctic.som.ou.edu/tburg/products/realtime/tropical/)
        - Tropical
    - [http://arctic.som.ou.edu/tburg/products/realtime/strat/](http://arctic.som.ou.edu/tburg/products/realtime/strat/)
        - Stratosphere

- Brian McNoldy's site
    - [https://bmcnoldy.earth.miami.edu/tropics/atlantic/](https://bmcnoldy.earth.miami.edu/tropics/atlantic/)
        - ton's of links also

- spaghetti (ASIA only, complementary to weather.us)
    - [https://www.easterlywave.com/typhoon/ensemble/](https://www.easterlywave.com/typhoon/ensemble/)

- Australia only forecast site (unofficial):
- [https://stormcast.com.au/stormcast.html](https://stormcast.com.au/stormcast.html)
    - BOM and GFS forecasts (lots of products)

- Per model tracks (MANY models)
    - [http://tropicalatlantic.com/models/models.cgi?viewer=1](http://tropicalatlantic.com/models/models.cgi?viewer=1)

- DOCUMENTATION:
    - [https://www.nhc.noaa.gov/modelsummary.shtml](https://www.nhc.noaa.gov/modelsummary.shtml)
        - model summaries
    - [https://www.wpc.ncep.noaa.gov/mdlbias/biastext.shtml](https://www.wpc.ncep.noaa.gov/mdlbias/biastext.shtml)
        - subjective model characteristics & biases

<a name="ed"/>

## Educational powerpoints & training docs:
- basic:
    - [https://blog.weather.us/tropical-cyclones-101-what-exactly-is-a-tropical-cyclone/](https://blog.weather.us/tropical-cyclones-101-what-exactly-is-a-tropical-cyclone/)
    - TC genesis theory factors (BOM):
        - [https://severeweather.wmo.int/TCFW/13WMO_Workshop2019/03_TC_genesis_WMO2019.pdf](https://severeweather.wmo.int/TCFW/13WMO_Workshop2019/03_TC_genesis_WMO2019.pdf)
    - NHC genesis forecasts:
        - [https://www.noaa.gov/sites/default/files/2022-05/2Blake-SECARTwebinar-20220517.pdf](https://www.noaa.gov/sites/default/files/2022-05/2Blake-SECARTwebinar-20220517.pdf)
    - General Meteorological knowledge, assembled by Houston CWSU (ZHU):
        - [https://www.weather.gov/source/zhu/ZHU_Training_Page/ZHU_Training_Page.html](https://www.weather.gov/source/zhu/ZHU_Training_Page/ZHU_Training_Page.html)
            - a wide survey of many different concepts
- NHC library (link collection page, not actual library but meta page to all library type resources):
    - [https://www.aoml.noaa.gov/general/lib/lib1/nhclib/](https://www.aoml.noaa.gov/general/lib/lib1/nhclib/)

- CPC product pages have educational links at the bottom:
    - [https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/enso.shtml#educational%20material](https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/enso.shtml#educational%20material)
    - [https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/enso.shtml#educational%20material](https://origin.cpc.ncep.noaa.gov/products/precip/CWlink/MJO/enso.shtml#educational%20material)

- [https://severeweather.wmo.int/TCFW/](https://severeweather.wmo.int/TCFW/)
    - Lots of training powerpoints for cyclones, and other info on forecasting
    - also see [https://severeweather.wmo.int/TCFW/](https://severeweather.wmo.int/TCFW/)

- WMO areas of responsibility (which agency/country is responsible):
    - [https://wwmiws.wmo.int/index.php](https://wwmiws.wmo.int/index.php)
- RSMCS:
    - [https://www.nhc.noaa.gov/aboutrsmc.shtml](https://www.nhc.noaa.gov/aboutrsmc.shtml)

- Various blogs:
    - i.e. CIMSS blog:
        - [https://cimss.ssec.wisc.edu/satellite-blog/archives/54989](https://cimss.ssec.wisc.edu/satellite-blog/archives/54989)

- ICON model:
    - [https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html](https://www.dwd.de/EN/research/weatherforecasting/num_modelling/01_num_weather_prediction_modells/icon_description.html)

- DOCUMENTATION:
    - [https://www.icams-portal.gov/resources/ofcm/nhop/nhop2.htm](https://www.icams-portal.gov/resources/ofcm/nhop/nhop2.htm)
        - NHOP (lots of documentation on NOAA operations)

    - [https://www.weather.gov/DIRECTIVES/010](https://www.weather.gov/DIRECTIVES/010)
        - Lots of operational documentation...
            - i.e. "10-607 Tropical Cyclone Forecast Center Products"
                - which provides more precise documentation on NHC products

    - [https://severeweather.wmo.int/TCFW/](https://severeweather.wmo.int/TCFW/)
        - See all sidebar links
        - Especially "Training Materials" for powerpoints on how each agency trains (lots of great info)
        - WMO Technical Publications
            - [https://community.wmo.int/en/tropical-cyclone-operational-plans](https://community.wmo.int/en/tropical-cyclone-operational-plans)
            - [https://cyclone.wmo.int/](https://cyclone.wmo.int/)
                - Guide to forecasting
        - "TC Cases: Difficult and extreme cases"
            - Forecast Agencies produce descriptions of epic fails (occasional self reports)

        - "Advisory and Warning Centres"
            - has all RSMC links

    - WMO doc for WMO file/message formats used online:
    - [https://community.wmo.int/en/ahl-table-definitions](https://community.wmo.int/en/ahl-table-definitions)

    - NOAA TC advisory products  - numbering (also useful for folders)
        - [https://www.weather.gov/media/notification/pdfs/pns18-27hurricane_numbering.pdf](https://www.weather.gov/media/notification/pdfs/pns18-27hurricane_numbering.pdf)

- Hodographs (especially useful to understand for predicting tornadoes):
    - [https://www.weather.gov/media/zhu/ZHU_Training_Page/convective_parameters/Hodograph_Extensive.pdf](https://www.weather.gov/media/zhu/ZHU_Training_Page/convective_parameters/Hodograph_Extensive.pdf)
    - [https://www.weather.gov/media/lmk/soo/Hodographs_Wind-Shear.pdf](https://www.weather.gov/media/lmk/soo/Hodographs_Wind-Shear.pdf)

<a name="social"/>

# Third-party social:
- [https://www.reddit.com/r/TropicalWeather](https://www.reddit.com/r/TropicalWeather)

<a name="general"/>

# General weather and environmental sites (not necessarily cyclone specific):
- CAP (WMO):
    - [https://severeweather.wmo.int/](https://severeweather.wmo.int/)

- METARS (automated station info reports)
    - [https://www.ogimet.com/metars.phtml.en](https://www.ogimet.com/metars.phtml.en)
    - [https://metar-taf.com/](https://metar-taf.com/)
    - [https://aviationweather.gov/data/metar/](https://aviationweather.gov/data/metar/)
    - [https://aviationweather.gov/gfa/#obs](https://aviationweather.gov/gfa/#obs)
    - [https://aviationweather.gov/](https://aviationweather.gov/)
- US
    - [https://www.weather.gov/](https://www.weather.gov/)
    - [https://www.wrh.noaa.gov/map/](https://www.wrh.noaa.gov/map/)
        - interactive
    - SPC (Storm prediction center) - useful for storms/tornadoes
        - [https://www.spc.noaa.gov/](https://www.spc.noaa.gov/)
        - [https://www.spc.noaa.gov/products/outlook/day1otlk.html](https://www.spc.noaa.gov/products/outlook/day1otlk.html)
        - [https://www.spc.noaa.gov/products/](https://www.spc.noaa.gov/products/)
            - severe weather outlooks and discussions for US
        - Also expert forecasting tools:
        - [https://www.spc.noaa.gov/exper/](https://www.spc.noaa.gov/exper/)
            - [https://www.spc.noaa.gov/exper/mesoanalysis/new/viewsector.php?sector=19](https://www.spc.noaa.gov/exper/mesoanalysis/new/viewsector.php?sector=19)
                - mesoscale analysis (expert tool: tons of products)
                    - NOTE: default is CONUS but can change region
            - [https://www.spc.noaa.gov/exper/hrrr/](https://www.spc.noaa.gov/exper/hrrr/)
                - HRRR model viewer (very fast updated models (hourly))
    - [https://cimss.ssec.wisc.edu/data/](https://cimss.ssec.wisc.edu/data/)
    - [https://www.weather.gov/DIRECTIVES/010](https://www.weather.gov/DIRECTIVES/010)
        - Operational documentation for NWS (US) (documentation (message formatting) & educational for understanding operations)
    - [https://www.ncei.noaa.gov/access/monitoring/products/](https://www.ncei.noaa.gov/access/monitoring/products/)
        - especially NCEI monthly reports - useful for US/Global climate tracking
            - (releases roughly 9 then 11 days after each month start -- see schedule)

    - HRRR (rapid refresh model and analysis data):
        - [https://rapidrefresh.noaa.gov/hrrr/](https://rapidrefresh.noaa.gov/hrrr/)
            - track/predict weather (including cyclones!), smoke, etc without waiting 6-12 hours

    - MRMS (radar rain)
        - [https://mrms.nssl.noaa.gov/qvs/product_viewer/](https://mrms.nssl.noaa.gov/qvs/product_viewer/)

    - Sondes (station observations: skew-t, hodographs):
        - [https://weather.rap.ucar.edu/upper/](https://weather.rap.ucar.edu/upper/)
        - [https://weather.uwyo.edu/upperair/sounding.html](https://weather.uwyo.edu/upperair/sounding.html)

    - Alaska Satellite Imagery:
        - [https://feeder.gina.alaska.edu/](https://feeder.gina.alaska.edu/)

    - Air quality (smoke/particulate risk from wildfires, pollution etc.)
        - [https://rapidrefresh.noaa.gov/hrrr/HRRRsmoke/](https://rapidrefresh.noaa.gov/hrrr/HRRRsmoke/)
            - Model predictions, rapidly updated
        - [https://www.iqair.com/](https://www.iqair.com/)
        - [https://atmosphere.copernicus.eu/charts/packages/cams/products/particulate-matter-forecasts](https://atmosphere.copernicus.eu/charts/packages/cams/products/particulate-matter-forecasts)
            - requires interpretation

    - [https://www.accuweather.com/en/us/severe-weather](https://www.accuweather.com/en/us/severe-weather)
        - severe weather alerts

    - [http://tropicalatlantic.com/models/models.cgi?page=models](http://tropicalatlantic.com/models/models.cgi?page=models)
        - A list of models

    - WeatherStar 4000 (nostalgic the weather channel recreation -- enter your zip code!)
        - [https://battaglia.ddns.net/twc/](https://battaglia.ddns.net/twc/)

    - GODAS - archived data (assimilated):
        - [https://www.psl.noaa.gov/data/gridded/data.godas.html#detail](https://www.psl.noaa.gov/data/gridded/data.godas.html#detail)

    - Moored buoy data (historical to present day):
        - [https://www.pmel.noaa.gov/tao/drupal/disdel/](https://www.pmel.noaa.gov/tao/drupal/disdel/)

- EU

    - [https://www.meteoalarm.org/en/live/](https://www.meteoalarm.org/en/live/)
        - Alerts/Warnings for Europe

    - [https://charts.ecmwf.int/](https://charts.ecmwf.int/)
        - the main charts website for ECMWF

    - Extreme weather links (Temp/Wind/Tornadoes):
        - [https://charts.ecmwf.int/products/opencharts_efi-cdf-meteogram?base_time=202405311200&lat=51.5084&lon=-0.125533&station_name=London&valid_time=202406020000](https://charts.ecmwf.int/products/opencharts_efi-cdf-meteogram?base_time=202405311200&lat=51.5084&lon=-0.125533&station_name=London&valid_time=202406020000)
            - EFI probabilities (CDF) point products (elevation and nearest lat/long point makes it tricky for accuracy)
        - [https://charts-dev.ecmwf.int/products/efi2web_10fg?area=Europe&base_time=202405311200&day=1&quantile=99](https://charts-dev.ecmwf.int/products/efi2web_10fg?area=Europe&base_time=202405311200&day=1&quantile=99)
            - EFI wind 10m (with Shift of tails)
            - CODE:
                - see [https://github.com/JRPdata/wastebook/blob/main/ireland_weather_stations.ipynb](https://github.com/JRPdata/wastebook/blob/main/ireland_weather_stations.ipynb)
        - [https://charts.ecmwf.int/products/extended-efi-sot-2t](https://charts.ecmwf.int/products/extended-efi-sot-2t)
            - EFI 2m temp (with Shift of tails)
        - [https://charts.ecmwf.int/products/medium-shear](https://charts.ecmwf.int/products/medium-shear)
            - Wind shear and MUCAPE
        - [https://charts.ecmwf.int/products/medium-2mt-wind30](https://charts.ecmwf.int/products/medium-2mt-wind30)
            - 30m wind + 2m temp
        - [https://charts.ecmwf.int/products/extended-anomaly-2t](https://charts.ecmwf.int/products/extended-anomaly-2t)
            - weekly mean 2m temp anomalies (goes out 6 weeks!)

        - [https://www.estofex.org/](https://www.estofex.org/)
            - Extreme weather (useful for predicting tornadoes in EU)

    - Archived data:
        - [https://data.europa.eu/data/datasets](https://data.europa.eu/data/datasets)

- Canada:
    - [https://weather.gc.ca/?alertTableFilterSearchpublic=&alertTableFilterSearchhighway=](https://weather.gc.ca/?alertTableFilterSearchpublic=&alertTableFilterSearchhighway=)
        - (find out about wildfires here)

- Australia:
    - [http://www.bom.gov.au/australia/warnings/?ref=ftr](http://www.bom.gov.au/australia/warnings/?ref=ftr)
        - warnings
    - [http://www.bom.gov.au/australia/meteye/](http://www.bom.gov.au/australia/meteye/)
        - interactive map with lots of products

- UK
    - [https://www.metoffice.gov.uk/weather/maps-and-charts/wind-gusts-map](https://www.metoffice.gov.uk/weather/maps-and-charts/wind-gusts-map)
    - [https://www.metoffice.gov.uk/](https://www.metoffice.gov.uk/)
    - [https://www.realweather.co.uk/ukv-1-5km-model/](https://www.realweather.co.uk/ukv-1-5km-model/)
    - [https://datahub.metoffice.gov.uk/](https://datahub.metoffice.gov.uk/)
        - Get gribs from UKMET models (1GB month free last I checked)
        - See doc: [https://www.metoffice.gov.uk/services/data/met-office-weather-datahub](https://www.metoffice.gov.uk/services/data/met-office-weather-datahub)
        - CODE:
            - Also see end of experimental python notebook: [https://github.com/JRPdata/wastebook/blob/main/ireland_weather_stations.ipynb](https://github.com/JRPdata/wastebook/blob/main/ireland_weather_stations.ipynb)

    - [https://www.theweatheroutlook.com/forecast/14-day-uk-weather-forecast](https://www.theweatheroutlook.com/forecast/14-day-uk-weather-forecast)
        - with discussion of 2 weeks

- Italy:
    - [https://www.isac.cnr.it/dinamica/projects/forecasts/bolam/](https://www.isac.cnr.it/dinamica/projects/forecasts/bolam/)
        - Forecasting page for Italy & Europe (lots of products, easy to reach)
    - [https://www.politicheagricole.it/flex/FixedPages/Common/miepfy200_reteAgrometeorologica.php/L/IT](https://www.politicheagricole.it/flex/FixedPages/Common/miepfy200_reteAgrometeorologica.php/L/IT)
    - Observations:
        - [https://www.politicheagricole.it/flex/FixedPages/Common/miepfy300_interrogazionepergrandezze.php/L/IT](https://www.politicheagricole.it/flex/FixedPages/Common/miepfy300_interrogazionepergrandezze.php/L/IT)
    - Data:
        - [https://www.mistralportal.it/opendata/](https://www.mistralportal.it/opendata/)
        - [https://dati.gov.it/](https://dati.gov.it/)

- Russia (no english version):
    - [https://meteoinfo.ru/egmb](https://meteoinfo.ru/egmb)

- India
    - [https://mausam.imd.gov.in/responsive/all_india_forcast_bulletin.php](https://mausam.imd.gov.in/responsive/all_india_forcast_bulletin.php)
    - [https://mausam.imd.gov.in/responsive/districtWiseWarning.php](https://mausam.imd.gov.in/responsive/districtWiseWarning.php)
        - district warnings -- click on each day
    - [https://nwp.imd.gov.in/fdp_now/fdp_bulletins/fdp.pdf](https://nwp.imd.gov.in/fdp_now/fdp_bulletins/fdp.pdf)
        - storm bulletins


- Mixed (including World):
    - [https://climatereanalyzer.org/](https://climatereanalyzer.org/)
        - Different reanalyses
            - Global / Hemispheric / Regions
            - 2m temps, Sea surface Temps, etc
    - [https://oz4caster.wordpress.com/cfsr/](https://oz4caster.wordpress.com/cfsr/)
        - CFSR Global anomaly and other charts

    - SST:
        - [https://coralreefwatch.noaa.gov/product/5km/index_5km_sst.php](https://coralreefwatch.noaa.gov/product/5km/index_5km_sst.php)
            - Unfortunately not contoured so hard to get exact values
        - See also Outlook and google maps interface (make sure to click SST at top):
            - [https://coralreefwatch.noaa.gov/product/vs/map.php](https://coralreefwatch.noaa.gov/product/vs/map.php)

    - CPC Links:
        - Expert assements/discussions massive link page:
            - [https://origin.cpc.ncep.noaa.gov/products/expert_assessment/](https://origin.cpc.ncep.noaa.gov/products/expert_assessment/)
        - Forecasts (including extended):
            - [https://origin.cpc.ncep.noaa.gov/products/forecasts/](https://origin.cpc.ncep.noaa.gov/products/forecasts/)
        - SST forecasts (CPC):
            - [https://origin.cpc.ncep.noaa.gov/products/predictions/90day/tools/briefing/unger.pri.php](https://origin.cpc.ncep.noaa.gov/products/predictions/90day/tools/briefing/unger.pri.php)
        - Different days:
            - [https://www.cpc.ncep.noaa.gov/products/predictions/threats/threats.php](https://www.cpc.ncep.noaa.gov/products/predictions/threats/threats.php)
                - 3-7 days US
            - [https://www.cpc.ncep.noaa.gov/products/predictions/threats/threats.php](https://www.cpc.ncep.noaa.gov/products/predictions/threats/threats.php)
                - Week 2
        - Stratosphere/Troposphere (GDAS/CPC):
            - [https://www.cpc.ncep.noaa.gov/products/stratosphere/strat-trop/](https://www.cpc.ncep.noaa.gov/products/stratosphere/strat-trop/)
        - Intraseasonal anomalies:
            - [https://www.cpc.ncep.noaa.gov/products/intraseasonal/](https://www.cpc.ncep.noaa.gov/products/intraseasonal/)

    - WPC:
        - [https://www.wpc.ncep.noaa.gov/](https://www.wpc.ncep.noaa.gov/)
            - features QPF (rain) also
            - see also "Forecasting Tools" above and right of the chart for more products
            - and also "Forecasts & Analyses" from the menu drop down
            - (many products)

    - [https://iridl.ldeo.columbia.edu/maproom/Global/Atm_Circulation/Monthly_Vpot.html?P=250](https://iridl.ldeo.columbia.edu/maproom/Global/Atm_Circulation/Monthly_Vpot.html?P=250)
        - Anomaly analysis based on historical data (Monthly, Daily, Seasonal and Wind, SST, GPH)
        - Monthly Velocity Potential Anomaly (250, 925) (last month)


    - [https://realearth.ssec.wisc.edu/](https://realearth.ssec.wisc.edu/)
        - Lots of satellite products to view as layers (global)
        - VIIRS image viewer for NPP (super high resolution):
            - [https://cimss.ssec.wisc.edu/viirs/imagery-viewer/?satellite=npp](https://cimss.ssec.wisc.edu/viirs/imagery-viewer/?satellite=npp)

    - [https://www.windy.com/](https://www.windy.com/)
        - famous visualizations for many models including expensive ones!

    - CMC forecast model visualization:
        - [https://eccc-msc.github.io/msc-animet](https://eccc-msc.github.io/msc-animet)
        - used for rain rates but has many other visualizations possible

<a name="gribdata"/>

## Data (gribs)
- [https://www.nco.ncep.noaa.gov/pmb/products/](https://www.nco.ncep.noaa.gov/pmb/products/)
    - (Master list?) NOAA data products
        - most useful list of links if you want to process data yourself for your own analysis
- [https://nomads.ncep.noaa.gov/](https://nomads.ncep.noaa.gov/)
    - Also has a good description of the model if you click on it under "Data set"
    - Mirrors select other model data (ie NAVGEM)
- [https://nrlgodae1.nrlmry.navy.mil/cgi-bin/datalist.pl?generate=summary](https://nrlgodae1.nrlmry.navy.mil/cgi-bin/datalist.pl?generate=summary)
    - (huge archive for model grib data NAVGEM/COAMPS/NOGAPS/FNMOC)
- [https://registry.opendata.aws/noaa-gefs/](https://registry.opendata.aws/noaa-gefs/)
    - GEFS gribs going back to 2017 (updated near real time)
        - See wastebook/gefs-aws.ipynb and hot-july/gefs/auto-download-aws.py
- [https://confluence.ecmwf.int/display/DAC/ECMWF+open+data%3A+real-time+forecasts](https://confluence.ecmwf.int/display/DAC/ECMWF+open+data%3A+real-time+forecasts)
- [https://opengribs.org/en/gribs](https://opengribs.org/en/gribs)
- [https://luckgrib.com/models/gefs/](https://luckgrib.com/models/gefs/)

- Short list of public models data sources:
    - GFS
        - [https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod](https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod)
    - ECM
        - [https://data.ecmwf.int/forecasts](https://data.ecmwf.int/forecasts)
    - CMC
        - [http://hpfx.collab.science.gc.ca](http://hpfx.collab.science.gc.ca)
    - NAV
        - [https://nomads.ncep.noaa.gov/pub/data/nccf/com/fnmoc/prod](https://nomads.ncep.noaa.gov/pub/data/nccf/com/fnmoc/prod)
        - Note: NAVGEM also has its own site (with a massive archive) but only has select? split gribs (not including everything in the NOAA mirror?)

- NOAA list of gridded data archives:
    - [https://www.ready.noaa.gov/archives.php](https://www.ready.noaa.gov/archives.php)

- PSL gridded data (historical up to today)
- [https://psl.noaa.gov/data/gridded/](https://psl.noaa.gov/data/gridded/)

- GEMPAK public data (a weather data archive):
    - [http://129.186.185.35/data/ldm/](http://129.186.185.35/data/ldm/)

- Documentation:
    - GFS:
        - [https://www.nco.ncep.noaa.gov/pmb/products/gfs/](https://www.nco.ncep.noaa.gov/pmb/products/gfs/)
            - under "Inventory"
                - ANL is analysis, FH = forecast hour from initialization time
    - for gribs params (raw format info only):
        - [https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/grib2_table4-2.shtml](https://www.nco.ncep.noaa.gov/pmb/docs/grib2/grib2_doc/grib2_table4-2.shtml)
    - CMC:
        - [https://eccc-msc.github.io/open-data/msc-data/nwp_gdps/readme_gdps_en/#access](https://eccc-msc.github.io/open-data/msc-data/nwp_gdps/readme_gdps_en/#access)
        - [https://eccc-msc.github.io/open-data/msc-data/nwp_gdps/readme_gdps-datamart_en/](https://eccc-msc.github.io/open-data/msc-data/nwp_gdps/readme_gdps-datamart_en/)

<a name="other"/>

## Other hazards:
- Tornadoes data (reports aggregated from internet):
    - [https://eswd.eu/cgi-bin/eswd.cgi](https://eswd.eu/cgi-bin/eswd.cgi)

- Volcanoes (observations):
    - [https://volcview.wr.usgs.gov/vv-gui/](https://volcview.wr.usgs.gov/vv-gui/)
        - VolcView - Satellite images of volcanoes)
    - [https://volcview.wr.usgs.gov/ashcam-gui/](https://volcview.wr.usgs.gov/ashcam-gui/)
        - Ashcam - "recent" webcam images of volcanoes

## Climate
- Makiko Sato & James Hansen's Global Temperature page:
    - [https://www.columbia.edu/~mhs119/Temperature/](https://www.columbia.edu/~mhs119/Temperature/)
- Global Tippping points:
    - [https://global-tipping-points.org/](https://global-tipping-points.org/)
    - [https://www.theguardian.com/environment/2023/dec/06/earth-on-verge-of-five-catastrophic-tipping-points-scientists-warn        - ](https://www.theguardian.com/environment/2023/dec/06/earth-on-verge-of-five-catastrophic-tipping-points-scientists-warn        - )
- Yale climate connections (link is only to specific topic: climate effect on storms):
    - [https://yaleclimateconnections.org/topic/eye-on-the-storm/](https://yaleclimateconnections.org/topic/eye-on-the-storm/)
- Sea ice:
    - PIOMAS (extent and arctic volume)
        - [http://psc.apl.uw.edu/research/projects/arctic-sea-ice-volume-anomaly/](http://psc.apl.uw.edu/research/projects/arctic-sea-ice-volume-anomaly/)
    - Sea ice extent:
        - [https://ads.nipr.ac.jp/vishop/#/extent](https://ads.nipr.ac.jp/vishop/#/extent)
    - NESDIS:
        - [https://www.star.nesdis.noaa.gov/socd/lsa/SeaIce/DataProducts/products_SeaIce.php](https://www.star.nesdis.noaa.gov/socd/lsa/SeaIce/DataProducts/products_SeaIce.php)
    - Copernicus (useful for many other things):
        - [https://cds.climate.copernicus.eu/](https://cds.climate.copernicus.eu/)

<a name="strato"/>

## High altitude weather and climate
- High altitude Zonal
    - [https://ozonewatch.gsfc.nasa.gov/meteorology/NH.html](https://ozonewatch.gsfc.nasa.gov/meteorology/NH.html)
        - Winds (Click on wind), also ozone, temperature, potential vorticity, etc

- Stratosphere observations (very detailed)
    - [https://stratobserve.com/](https://stratobserve.com/)

<a name="misclinks"/>

## Other sites with useful data products
- NESDIS catalog:
    - [https://www.star.nesdis.noaa.gov/portfolio/index.php](https://www.star.nesdis.noaa.gov/portfolio/index.php)
- OSPO main site (catalog of products and satellite outages/status):
    - [https://www.ospo.noaa.gov/](https://www.ospo.noaa.gov/)

<a name="satarchive"/>

## Satellite imagery archive
- Satellite Imagery Archive (SDS):
    - [https://inventory.ssec.wisc.edu/inventory/](https://inventory.ssec.wisc.edu/inventory/)
    - DOCUMENTATION:
        - [https://edc.occ-data.org/goes16/gdal/](https://edc.occ-data.org/goes16/gdal/)
        - [https://noaa-goes16.s3.amazonaws.com/Version1.1_Beginners_Guide_to_GOES-R_Series_Data.pdf](https://noaa-goes16.s3.amazonaws.com/Version1.1_Beginners_Guide_to_GOES-R_Series_Data.pdf)
        - [https://docs.opendata.aws/noaa-goes16/cics-readme.html](https://docs.opendata.aws/noaa-goes16/cics-readme.html)
        - CODE:
            - [https://github.com/HamedAlemo/visualize-goes16/blob/main/visualize_GOES16_from_AWS.ipynb](https://github.com/HamedAlemo/visualize-goes16/blob/main/visualize_GOES16_from_AWS.ipynb)

- Satellite look up (details, facts on current and historical satellites):
    - [https://space.oscar.wmo.int/satellites/view/meteosat_11](https://space.oscar.wmo.int/satellites/view/meteosat_11)

<a name="radararchive"/>

## Radar archive
- LEVEL2 radar data archive from nexrad on AWS (tricky to use without packages):
    - [https://s3.amazonaws.com/noaa-nexrad-level2/index.html#2023/11/15/KAMX/](https://s3.amazonaws.com/noaa-nexrad-level2/index.html#2023/11/15/KAMX/)

<a name="random"/>

## Random sites related to weather, climate
- [https://coolwx.com/](https://coolwx.com/)

<a name="expnotes"/>

## experimental personal projects (don't use!) and random notes:
- notebooks and programs (python3):
    - [https://github.com/JRPdata/nhc_errors](https://github.com/JRPdata/nhc_errors)
        - experimental notebook on intensification OFCL errors
        - analysis of RI for OFCL (reproduction)
        - calculating current probabilities automatically on NHC OFCL forecasts based on intensification data
    - [https://github.com/JRPdata/cyclone_climatology](https://github.com/JRPdata/cyclone_climatology)
        - do statistical predictions based on IB data (uses other packages so requires setup)
        - requires coding for each question (see examples)
    - [https://github.com/JRPdata/wastebook](https://github.com/JRPdata/wastebook)
        - lots of random collections
    - [https://github.com/JRPdata/cyclone_genesis](https://github.com/JRPdata/cyclone_genesis)
        - a tropical cyclone classifier/tracker -- includes download scripts
        - based on Robert Hart's model genesis work but no where as refined
        - not purely single process. requires minimum ~7-10 gb of storage even when keeping models for only 2 days
        - hopefully useful as reference
    - [https://jrpdata.github.io/cyclone_genesis_charts/](https://jrpdata.github.io/cyclone_genesis_charts/)
        - temporary output for experimental tracking from the above cyclone_genesis program (updated randomly whenever I am using it)

- insights:
    - [https://gist.github.com/deeplycloudy/7b8412094c7a249d19b771374f312750](https://gist.github.com/deeplycloudy/7b8412094c7a249d19b771374f312750)
        - referenced some of deeplycloudy's comments and work when writing code for vorticity calculations
            - it seems that relative vorticity calculations for gempak don't account for differences in map projection distances in gridded data
                - see cyclone-genesis notebook in JRPDATA and relevant discussions on metview python packge development (github? can't remember where I read it)
                    - confirmed that they do produce different vorticity calculations (Robert Hart's FSU site appears to use 0.5 deg GFS and the same vorticity calculations as GEMPAK (fortan?))

- software:
    - metview (not the python package below)
        - have to build and configure everything from scratch (time consuming)
        - lets you examine and plot gribs (gribs have to be in relative folder (create a symlink))
            - plotting is a mixed bag but it does have useful histograms for discovering extrema
        - good for debugging when writing programs that work on grib data

- packages:
    - [https://metview.readthedocs.io/en/latest/](https://metview.readthedocs.io/en/latest/)
