class Values:
    # Demo Mode has slow scrolling to see where you are on the page better.
    # However, a regular slow scroll takes too long to cover big distances.
    # If the scroll distance is greater than SSMD, a slow scroll speeds up.
    SSMD = 900  # Smooth Scroll Minimum Distance (for advanced slow scroll)


class JQuery:
    VER = "3.6.0"
    MIN_JS = "https://cdnjs.cloudflare.com/ajax/libs/jquery/%s/jquery.min.js" % VER
