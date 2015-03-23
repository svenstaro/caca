# caca - Copy And Convert Audio

A very simple one-shot parallel audio converter that behaves a lot like cp.

The way it behaves is such as that when a directory structure is given (and -r is used) it will recurse into it and copy and files it finds but convert FLAC files on the fly while it does so. It will not overwrite existing files unless called with -f.

It is meant for providing large collections of mixed files in a specific format.
