Unicorn Hat daemon
=====================

Unicorn Hat daemon is a simple C program that listen on a Unix socket in
`/var/run/unicornd.socket` and accepts command to set the leds of the Unicorn
Hat so that you can run the daemon as root and your programs as normal
user.

It can handle only one connection at a time.

`make install` will install the daemon.

```
sudo make install
sudo service unicorn start
sudo service unicorn stop
```

To set the daemon to start at boot run `sudo update-rc.d unicorn defaults`

The daemon makes the `pi` user the owner of the `/var/run/unicornd.socket`.

### Protocol
The protocol is simple: each command is composed of a code (the command you want
to execute) and its possible arguments.

You need to first connect to the Unix socket and the send a struct that describe
the command.

##### set brightness

```c
struct {
	uint8_t code; // set to 0
	double  val;
};
```

##### set pixel

```c
struct {
	uint8_t code; // set to 1

	pos_t pos;
	col_t col;
};
```

where `pos_t` is a struct like this:

```c
struct {
	uint8_t x;
	uint8_t y;
};
```

and where `col_t` is a struct like this:

```c
struct {
	uint8_t r;
	uint8_t g;
	uint8_t b;
};
```

##### set all pixels

```c
struct {
	uint8_t code; // set to 2

	col_t pixels[64];
};
```

##### show

```c
struct {
	uint8_t code; // set to 3
};
```

### examples
See the Ruby and Perl test clients
