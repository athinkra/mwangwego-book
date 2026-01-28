#!/usr/bin/perl -w

binmode(STDIN, ":utf8");
binmode(STDOUT, ":utf8");
binmode(STDERR, ":utf8");
use utf8;
use strict;
use open ':encoding(utf-8)';

main:
{
	while( <> ) {
		tr/\x{F0000}-\x{F0040}/\x{16E00}-\x{16E40}/;
		print;
	}
}
