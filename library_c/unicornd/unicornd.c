/*
 * Copyright (C) 2014 jibi <jibi@paranoici.org>
 *
 */

#include <signal.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#include <sys/socket.h>
#include <sys/stat.h>
#include <sys/types.h> 
#include <sys/un.h>

#include "ws2811.h"

#define TARGET_FREQ    WS2811_TARGET_FREQ
#define GPIO_PIN       18
#define DMA            10

#define WIDTH          8
#define HEIGHT         8
#define LED_COUNT      (WIDTH * HEIGHT)

ws2811_t ledstring =
{
    .freq = TARGET_FREQ,
    .dmanum = DMA,
    .channel =
    {
        [0] =
        {
            .gpionum    = GPIO_PIN,
            .count      = LED_COUNT,
            .invert     = 0,
            .brightness = 55,
            .strip_type = WS2811_STRIP_GRB,
        }
    }
};

static inline
int
get_pixel_pos(uint8_t x, uint8_t y)
{
	int map[8][8] = {
		{7 ,6 ,5 ,4 ,3 ,2 ,1 ,0 },
		{8 ,9 ,10,11,12,13,14,15},
		{23,22,21,20,19,18,17,16},
		{24,25,26,27,28,29,30,31},
		{39,38,37,36,35,34,33,32},
		{40,41,42,43,44,45,46,47},
		{55,54,53,52,51,50,49,48},
		{56,57,58,59,60,61,62,63}
	};

	return map[x][y];
}

static inline
void
set_pixel_color(int pixel, int r, int g, int b)
{
    ledstring.channel[0].leds[pixel] = (r << 16) | (g << 8) | b;
}


static inline
void
clear_led_buffer(void)
{
    int i;

    for(i = 0; i < LED_COUNT; i++){
        set_pixel_color(i, 0, 0, 0);
    }
}

static inline
void
set_brightness(int b)
{
    ledstring.channel[0].brightness = b;
}

static inline
void
show(){
    ws2811_render(&ledstring);
}

static inline
void
unicornd_exit(int status)
{
	clear_led_buffer();
	show();

	ws2811_fini(&ledstring);

	exit(status);
}

static inline
void
init_unicorn_hat(void)
{
	int i;
	struct sigaction sa;
	/* All terminating signals, as described by 'man 7 signal'. */
	static const int term_signals[] = {
		/* POSIX.1-1990 */
		SIGHUP,
		SIGINT,
		SIGQUIT,
		SIGILL,
		SIGABRT,
		SIGFPE,
		SIGKILL,
		SIGSEGV,
		SIGPIPE,
		SIGALRM,
		SIGTERM,
		SIGUSR1,
		SIGUSR2,
		/* POSIX.1-2001 */
		SIGBUS,
		SIGPOLL,
		SIGPROF,
		SIGSYS,
		SIGTRAP,
		SIGVTALRM,
		SIGXCPU,
		SIGXFSZ,
	};

	for (i = 0; i < sizeof(term_signals)/sizeof(term_signals[0]); i++) {
		memset(&sa, 0, sizeof(sa));
		sa.sa_handler = unicornd_exit;
		sigaction(term_signals[i], &sa, NULL);
	}

	setvbuf(stdout, NULL, _IONBF, 0);

	if (ws2811_init(&ledstring) < 0) {
		exit(1);
	}

	clear_led_buffer();
	set_brightness(20);
}

#define SOCK_PATH "/var/run/unicornd.socket"

#define	UNICORND_CMD_SET_BRIGHTNESS 0
#define	UNICORND_CMD_SET_PIXEL      1
#define	UNICORND_CMD_SET_ALL_PIXELS 2
#define	UNICORND_CMD_SHOW           3
#define	UNICORND_CMD_CLEAR          4

#define recv_or_return(socket, buf, len, flags) \
{                                               \
	int _ret;                               \
	_ret = recv(socket, buf, len, flags);   \
                                                \
	if (_ret <= 0) {                        \
		close(socket);                  \
		return;                         \
	}                                       \
}

typedef struct col_s {
	uint8_t r;
	uint8_t g;
	uint8_t b;
} col_t;

typedef struct pos_s {
	uint8_t x;
	uint8_t y;
} pos_t;

static
int
setup_listen_socket(void)
{
	int listen_socket;
	int ret;
	socklen_t len;
	struct sockaddr_un local;

	listen_socket = socket(AF_UNIX, SOCK_STREAM, 0);
	if (listen_socket == -1) {
		fprintf(stderr, "cannot create unix socket");
		exit(1);
	}

	unlink(SOCK_PATH);

	local.sun_family = AF_UNIX;
	strcpy(local.sun_path, SOCK_PATH);
	len = strlen(local.sun_path) + sizeof(local.sun_family);

	ret = bind(listen_socket, (struct sockaddr *) &local, len);
	if (ret == -1) {
		fprintf(stderr, "cannot bind socket");
		exit(1);
	}

	chmod(SOCK_PATH, 0777);

	ret = listen(listen_socket, 4);
	if (ret == -1) {
		fprintf(stderr, "cannot listen on socket");
		exit(1);
	}

	return listen_socket;
}

static
int
do_accept(int listen_socket) {
	struct sockaddr_un client;
	int client_socket;
	socklen_t len;

	len = sizeof(client);

	client_socket = accept(listen_socket, (struct sockaddr *)&client, &len);
	if (client_socket == -1) {
		fprintf(stderr, "cannot accept client connection");
		exit(1);
	}

	return client_socket;
}

static
void
handle_client(int client_socket) {
	uint8_t cmd;

	char bright;

	pos_t pos;
	col_t col;

	col_t pixels[64];
	
	int x, y;

	while (true) {
		recv_or_return(client_socket, &cmd, sizeof(char), 0);

		switch (cmd) {
			case UNICORND_CMD_SET_BRIGHTNESS:

				recv_or_return(client_socket, &bright, sizeof(char), 0);

				set_brightness(bright);
				break;

			case UNICORND_CMD_SET_PIXEL:

				recv_or_return(client_socket, &pos, sizeof(pos_t), 0);
				recv_or_return(client_socket, &col, sizeof(col_t), 0);

				set_pixel_color(get_pixel_pos(pos.x, pos.y), col.r, col.g, col.b);
				break;

			case UNICORND_CMD_SET_ALL_PIXELS:
				recv_or_return(client_socket, &pixels, 64 * sizeof(col_t), 0);

				for (x = 0; x < 8; x++) {
					for (y = 0; y < 8; y++) {
						col_t *col = &pixels[x * 8 + y];
						set_pixel_color(get_pixel_pos(x, y), col->r, col->g, col->b);
					}
				}

				break;

			case UNICORND_CMD_SHOW:

				show();
				break;

			case UNICORND_CMD_CLEAR:

				clear_led_buffer();
				break;
				
			default:

				close(client_socket);
				return;
		}
	}
}

int
main(void)
{
	int listen_socket, client_socket;

	init_unicorn_hat();
	listen_socket = setup_listen_socket();

	while (true) {
		client_socket = do_accept(listen_socket);

		if (client_socket != -1) {
			handle_client(client_socket);
		}
	}

	return 0;
}

