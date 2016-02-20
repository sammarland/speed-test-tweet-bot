# Twitter Speed Test Bot

This twitter bot will tweet when the speed drops below a specified speed.

## How to run
Install the 3 required python modules by running

    pip install twitter
    pip install tinyurl

To run the script make sure you're in the directory with the files and then run:

    speedtest-cli --share --secure | awk -f awk.awk


