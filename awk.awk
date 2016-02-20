#!/usr/bin/awk -f
BEGIN {
	FS=": "
	ping=""
	download=""
	upload=""
	share=""
}
{
    if(NR == 5){
        ping=$2
		print "Got ping"
    } else if ( $1 == "Download" ) {
        download=$2
		print "Got Download"
    } else if ( $1 == "Upload" ) {
        upload=$2
		print "Got Upload"
        FS=" "
    } else if ( $1 == "Share") {
        share=$3
    }
}
END {
	system("python tweeting-twitter.py "ping download upload share)
}
