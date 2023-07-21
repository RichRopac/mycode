#!/usr/bin/env python3
"""All the ASCII images
   showing in the game"""

#import the color variables from color.py
from color import *

# Map for standing in front of the Mansion
map_entrance = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##   {purple}\
Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}                         ##                  ##                   #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#                     ##                           ##              #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}################     #############################
                                 |     |
                                 |  {yellow}X  {green}|{white}
"""

# Map for standing in the Fouyer
map_fouyer = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##{purple}\
   Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}                         ##                  ##                   #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#                     ##            {yellow}X              {green}##              #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}##################################################{white}
"""

# Map for standing in the Library
map_library = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##{purple}\
   Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}                         ##                  ##                   #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#                     ##                           ##      {yellow}X{green}       #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}##################################################{white}
"""

# Map for standing in the Reception Room
map_reception = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##{purple}\
   Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}                         ##                  ##                   #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#           {yellow}X{green}         ##                           ##              #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}##################################################{white}
"""

# Map for standing in the Living Room
map_living = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##{purple}\
   Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}           {yellow}X{green}             ##                  ##                   #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#                     ##                           ##              #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}##################################################{white}
"""

# Map for standing in the Dining Room
map_dining = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##{purple}\
   Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}                         ##        {yellow}X{green}         ##                   #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#                     ##                           ##              #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}##################################################{white}
"""

# Map for standing in the Kitchen
map_kitchen = f"""
{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}###{blue}---{green}#######\
{blue}---{green}###{blue}---{green}############{blue}---{green}###{blue}---{green}#######
#                         ##                                       #
{blue}|{green}                         ##                  ##                   #
#   {purple}   Living Room        {green}##{purple}\
   Dining Room    {green}##      {purple}Kitchen      {blue}|{green}
{blue}|{green}                         ##                  ##         {yellow}X{green}         #
#                                             ##                   #
##   ###############################################################
##   ###############################################################
#                     ##                           ##              #
#                     ##                           ##              #
{blue}|{purple}    Reception Room               Fouyer                Library    {blue}|{green}
#                     ##                           ##              #
{blue}|{green}                     ##                           ##              {blue}|{green}
###{blue}---{green}###{blue}---{green}###{blue}---{green}##################################################{white}
"""

banner = red+"""

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


            ░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
            ░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
            ░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
            ░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
            ░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
            ░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░

███╗░░░███╗██╗░░░██╗██████╗░██████╗░███████╗██████╗░  ███╗░░░███╗░█████╗░███╗░░██╗░██████╗░█████╗░███╗░░██╗
████╗░████║██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔══██╗  ████╗░████║██╔══██╗████╗░██║██╔════╝██╔══██╗████╗░██║
██╔████╔██║██║░░░██║██████╔╝██║░░██║█████╗░░██████╔╝  ██╔████╔██║███████║██╔██╗██║╚█████╗░██║░░██║██╔██╗██║
██║╚██╔╝██║██║░░░██║██╔══██╗██║░░██║██╔══╝░░██╔══██╗  ██║╚██╔╝██║██╔══██║██║╚████║░╚═══██╗██║░░██║██║╚████║
██║░╚═╝░██║╚██████╔╝██║░░██║██████╔╝███████╗██║░░██║  ██║░╚═╝░██║██║░░██║██║░╚███║██████╔╝╚█████╔╝██║░╚███║
╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░╚════╝░╚═╝░░╚══╝
  """+white+"""
"""
