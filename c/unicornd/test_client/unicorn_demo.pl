#!/usr/bin/perl
use strict;
use warnings;
use Unicorn;

my $u = Unicorn->new();
$u->set_brightness(20);
$u->clear();
$u->set_pixel(2, 2, 255, 0, 0);
$u->set_pixel(4, 4, 0, 255, 0);
$u->set_pixel(6, 6, 0, 0, 255);
$u->show;

sleep(3);

my @pixels;
for my $x (1..8)
{
    for my $y (1..8)
    {
        my $z = ($x + $y) % 3;
        if($z == 0)
        {
            push @pixels, (255, 0, 0);
        } elsif($z == 1) {
            push @pixels, (0, 255, 0);
        } elsif($z == 2) {
            push @pixels, (0, 0, 255);
        }
    }
}
$u->set_all_pixels(@pixels);
$u->show;

#sleep(6);
#$u->clear;
#$u->show;

