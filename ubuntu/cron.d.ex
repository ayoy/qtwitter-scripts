#
# Regular cron jobs for the qtwitter package
#
0 4	* * *	root	[ -x /usr/bin/qtwitter_maintenance ] && /usr/bin/qtwitter_maintenance
