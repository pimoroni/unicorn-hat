package Unicorn;

use strict;
use warnings;
use IO::Socket::UNIX;

my $UNICORND_SOCKET_PATH        = "/var/run/unicornd.socket";
my $UNICORND_CMD_SET_BRIGHTNESS = 0;
my $UNICORND_CMD_SET_PIXEL      = 1;
my $UNICORND_CMD_SET_ALL_PIXELS = 2;
my $UNICORND_CMD_SHOW           = 3;

sub set_all_pixels
{
    my $self = shift;
    my $command = pack "C*", $UNICORND_CMD_SET_ALL_PIXELS, @_;
    $self->{socket}->send($command);
}

sub clear
{
    my $self = shift;
    $self->set_all_pixels((0,0,0) x 64);
}

sub set_pixel
{
    my $self = shift;
    my $command = pack "CCCCCC", $UNICORND_CMD_SET_PIXEL, @_;
    $self->{socket}->send($command);
}

sub show
{
    my $self = shift;
    my $command = pack "C", $UNICORND_CMD_SHOW;
    $self->{socket}->send($command);
}

sub set_brightness
{
    my $self = shift;
    my $brightness = shift;
    my $command = pack "CC", $UNICORND_CMD_SET_BRIGHTNESS, $brightness;
    $self->{socket}->send($command);
}

sub new
{
    my ($class) = @_;
    my $socket = IO::Socket::UNIX->new(
        Peer => $UNICORND_SOCKET_PATH,
        Type => SOCK_STREAM(),
    );
    return bless {
        socket => $socket,
    }, $class;
}

1;
