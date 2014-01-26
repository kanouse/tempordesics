## The Tempordesic Calendar

As a perennial calendar with a static structure (4x13x7+1), the same Tempordesic Calendar can be used for every year. Simplifies relative date calculations and reference date contexts.

### Annual period division

- Each year is divided into four (4) even quarters:
    1. The first quarter begins on the Northward Equinox (the Vernal Equinox in the Northern Hemisphere) and is referred to verbosely as "Boreal" in reference to the Northward progression of the solar apex.
    2. The second quarter begins on the Northern Solstice (the Summer Solstice in the Northern Hemisphere) and is referred to verbosely as "Perigee" in reference to the periapsis point in Earth's proximity to the sun.
    3. The third quarter begins on the Southward Equinox (the Autumnal Equinox in the Northern Hemisphere) and is referred to verbosely as "Austral" in reference to the Southward progression of the solar apex.
    4. The fourth quarter begins on the Southern Solstice (the Winter Solstice in the Northern Hemisphere) and is referred to verbosely as "Apogee" in reference to the apoapsis point in Earth's proximity to the sun.
- Each quarter is divided into thirteen (13) even weeks
- Each week is divided into seven (7) days
- Every year begins with a "New Year Day" which is does not fall into a week. Notation for New Year Day is y/0/0/0 (In a civil context this could be viewed as an additional day of respite between Saturday and Sunday.)
- There are leap years which add an additional day to the end of the calendar. (More below.)

### Numeric Notation
    
The format for numeric representation of Tempordesic Dates is: _[Year]/[Quarter]/[Week]/[Day]_. For casting in variables the string format is: _y/q/w/d_

### Verbose Notation

Verbose terms exist for quarter and day segments:

- Quarters 1-4 are *Boreal*, *Perigee*, *Austral*, and *Apogee* respectively. Traditional terms such as Spring, Summer, Fall and Winter are avoided to allow for common reference in Northern and Southern Hemispheres.
- Days 1-7 are *Sunday*, *Monday*, *Tuesday*, *Wednesday*, *Thursday*, *Friday*, and *Saturday* respectively.

The verbose form of a tempordesic date is [Quarter] [Year], [Day] [Week]. Some examples:

- *Boreal 2011, Monday 7* for 2011/1/7/2
- *Apogee 1996, Thursday 12* for 1996/4/12/5

### Point of reference with the Gregorian Calendar

y/1/1/1 is the Spring Equinox and roughly corresponds to March 20. Year 1, day 1 of the Tempordesic Calendar (1/1/1/1) is referenced as March 21, 1 A.D. in the Gregorian Calendar, the Spring Equinox of that year. Day 0 (1/0/0/0), the first New Year Day, March 20, 1 A.D..

*Note about Year One*: In attempting to recalibrate perspectives on a common calendar it's tempting to also revisit the notion of Anno Domini and the Christian context for "year one". While perhaps it is a more culturally enlightened objective, changing or resetting our position in the timeline of years does not bring civil or logistical benefit to the process of calendar reform but rather creates an unnecessary barrier to adoption.

### Sync Days / Leap Years

Earth orbits the Sun once every 365 + 0.2425 days. The 0.2425 add up, so we need synchronization days to maintain seasonal alignment. Traditional leap year rules apply to the Tempordesic Calendar, the leap day is added at the end of the last week of the last quarter (y/4/13/8). Sample code for leap year calculation:

    def is_leap_year(year):
        if (year % 400) == 0:
            return True
        elif (year % 100) == 0:
            return False
        elif (year % 4) == 0:
            return True
        else:
            return False


### Similarities to The World Season Calendar

It is worth noting that the overall construct is similar to the World Season Calendar (WSC), a 4x91 perennial calendar proposed by Isaac Asimov, with a couple of key distinctions. The WSC begins its four quarter sequence (quarter A) at the Southern Solstice, December 21. (By starting at the Equinox, the Tempordesic Calendar is retaining a hemispheric neutrality.) In addition the WSC numbers days in a quarter 1-91 whereas the Tempordesic Calendar cycles seven day periods over 13 weeks and incorporates the week reference into the notation. For more information about the World Season Calendar a couple of related links below:

- Will Shipman's "Scientific Time" page has a good overview of the WSC (and some other interesting notes.)
- General Entry at Citizendia
