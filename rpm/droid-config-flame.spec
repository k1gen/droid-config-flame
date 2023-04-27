%define device flame
%define vendor google

%define vendor_pretty Google
%define device_pretty Pixel 4

# Community HW adaptations need this
%define community_adaptation 1

%define android_version_major 11

%define pixel_ratio 1.75
%define icon_res 1.75

# Device-specific ofono configuration
Provides: ofono-configs
Obsoletes: ofono-configs-mer

# Device-specific bluez5 configuration
Provides: bluez5-configs
Obsoletes: bluez5-configs-mer

%include droid-configs-device/droid-configs.inc
%include patterns/patterns-sailfish-device-adaptation-flame.inc
%include patterns/patterns-sailfish-device-configuration-flame.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

