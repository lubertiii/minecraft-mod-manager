#File for determining if the minecraft version to be run is compatible to the version of installed mods
#Dependencies
#allows usage of SpecifierSet which evaluates version compatibility properly from version formats
from packaging.specifiers import SpecifierSet
#allows usage of Version which turns a string into a version that can be recognized by SpecifierSet
from packaging.version import Version
#allows usage of RegEx for finding specific patterns of strings
import re

#Function
def versionCompatible(compatible_version: list, minecraft_version: str):
    #initialize a list that compiles all evaluated compatibility(True or False) of each mod
    compatible_list = []
    #initialize minecraft_version inside Version for it to be recognized by SpecifierSet
    version_requirement = Version(minecraft_version)
    #iterate through each version compatibility of compatible version list
    for each_compatible_version in compatible_version:
        #identify the variant of unsupported format and clean it according to standards of SpecifierSet, store inside clean_compatible_version
        clean_compatible_version = identifyVariant(each_compatible_version)
        #recheck if version format is already clean, if not, clean it again
        if '~' in clean_compatible_version:
            #repeat identifying variant of unsupported format and clean it again
            clean_compatible_version = identifyVariant(clean_compatible_version)
        #initialize the clean version inside SpecifierSet to standardize it and allow for correct version compatibility evaluation
        standardized_compatible_version = SpecifierSet(clean_compatible_version.replace(" ", ","), prereleases= True)
        #Evaluate if desired version of minecraft is compatible with each mod inside .minecraft/mods folder
        if version_requirement in standardized_compatible_version:
            compatible_list.append(True)
        else:
            compatible_list.append(False)

    return compatible_list

def identifyVariant(each_compatible_version: str):
    #get versions with (-alpha., -beta.)
    pre_release_1 = re.search(r"-(alpha|beta)\.", each_compatible_version, re.IGNORECASE)
    #get versions with (-rc.)
    pre_release_2 = re.search(r"-rc\.*", each_compatible_version)
    #get versions with (1.20.x or 26.3.x)
    x_variant = re.search(r"\d{1,2}\.\d{1,2}\.x", each_compatible_version, re.IGNORECASE)
    #get versions with(-0)
    hyphen_zero_variant = '-0' in each_compatible_version
    #get versions with (1.20.1- or 26.3-)
    hyphen_variant = '-' in each_compatible_version
    #get versions with (*)
    asterisk_variant = '*' in each_compatible_version
    #get versions with (~)
    tilde_variant = '~' in each_compatible_version
    #get versions with (~) and characters
    tilde_with_char = re.search(r"(rc|a|b)\d*", each_compatible_version, re.IGNORECASE)
    #get versions with accepted format
    normal_variant = each_compatible_version.startswith('>')

    if pre_release_1:
        #replace -alpha. to a, -beta. to b
        appropriate_format = each_compatible_version.replace(pre_release_1.group(), pre_release_1.group()[1])
    elif pre_release_2:
        #replace -rc. to rc
        appropriate_format = each_compatible_version.replace(pre_release_2.group(), "rc")
    elif x_variant:
        #replace version from either 1.20.x to 1.20.*, 26.3.x to 26.3.*
        appropriate_format = f"=={x_variant.group().strip('x')}*"
    elif hyphen_variant:
        #replace version from 1.20.1- to 1.20.1, 26.3- to 26.3
        appropriate_format = each_compatible_version.replace('-', 'a' if hyphen_zero_variant else 'a1')
    elif asterisk_variant:
        #replace version from * to empty string
        appropriate_format = ''
    elif tilde_variant:
        if tilde_with_char:
            #get version number only
            current_version = each_compatible_version.strip('~').replace(tilde_with_char.group(), '')
            #get pre release characters (a, b, rc)
            pre_release_format = re.sub(r"[^a-zA-Z]", '', each_compatible_version)
        else:
            #get version number only
            current_version = each_compatible_version.strip('~')
        #get the upper version limit
        version_limit = re.sub(r"\d+$", lambda version: str(int(version.group()) + 1), current_version)
        #replace version from ~1.21.1rc0 to >=1.21.1rc0 <1.21.2a0, ~26.3 to >=26.3a0 <26.4a0 or
        #replace version from ~1.21.1 to >=1.21.1a0 <1.21.2a0, ~26.3 to >=26.3a0 <26.4a0
        appropriate_format = f">={current_version}{pre_release_format}0 <{version_limit}a0" if tilde_with_char else f">={current_version}a0 <{version_limit}a0"
    elif normal_variant:
        #do not replace anything
        appropriate_format = each_compatible_version
    else:
        #check if there is already an existing '=' in version number and apply additional equal symbols to correctly format the version
        if '=' in each_compatible_version:
            #replace version from =1.21.1 to ==1.21.1, =26.3 to ==26.3
            appropriate_format = f"={each_compatible_version}"
        else:
            #replace version from 1.21.1 to ==1.21.1, 26.3 to ==26.3
            appropriate_format = f"=={each_compatible_version}"

    return appropriate_format
