#!/usr/bin/perl -w
use strict;
use utf8;

my @Bases = (
	"a",
	"ba",
	"cha",
	"da",
	"fa",
	"ga",
	"gha",
	"ha",
	"ja",
	"zha",
	"ka",
	"la",
	"ma",
	"na",
	"nya",
	"pa",
	"ra",
	"sa",
	"sha",
	"ta",
	"tsa",
	"psa",
	"va",
	"wa",
	"za",
	"dza",
	"dhla",
	"hla",
	"xa",
	"qa",
	"tha"
);

main:
{
	for my $base (@Bases) {
		for my $masisi ( "emwa", "ima", "ota", "uyu" ) {
			print "sub $base-mwangwego $masisi by $base-$masisi ;\n";
		}
		print "\n";
	}
}
