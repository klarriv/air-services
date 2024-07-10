from .constants import pi

def Elbow_centerline_length(dia, clr, tan1, tan2, angle=90):
    return 2*pi*dia*clr*(angle/360)+tan1+tan2