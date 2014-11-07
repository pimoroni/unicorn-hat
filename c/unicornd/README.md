Unicorn Hat daemon
=====================

Unicorn Hat daemon is a simple C program that listen on a Unix socket in
`/var/run/unicornd.socket` and accepts command to set the leds of the Unicorn
Hat so that you can run the daemon as root and your programs as normal
user.

It can handle only one connection at a time.

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

	uint8_t x;
	uint8_t y;

	uint8_t r;
	uint8_t g;
	uint8_t b;
};
```

##### show

```c
struct {
	uint8_t code; // set to 2
};
```

### examples
See the Ruby test client
